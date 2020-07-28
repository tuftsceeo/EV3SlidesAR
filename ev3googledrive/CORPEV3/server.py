
#!/usr/bin/env python3.4
from flask import Flask, request, jsonify, render_template, send_from_directory
from ev3dev.ev3 import *
from time import sleep
from motorsEV3 import *
from sensorsEV3 import *
from werkzeug.utils import secure_filename
import subprocess
from multiprocessing import Process
import os.path
import sys
import io
import threading
from threading import Thread, Event
import trace
import traceback
from importlib.machinery import SourceFileLoader
import traceback
import importlib
import json


# For handling process management for the IDE
processes = set([])

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# this directory contains the projects that can be accessed by the user
DIR_ROOT = APP_ROOT + '/Projects'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'py'])
# for saving file operations and allow collaborative coding
operations = {}
# process for user's program
p = None

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = DIR_ROOT


@app.route("/")
def home():
        return "Connected to Flask Server!"

def allowed_file(filename):
        return '.' in filename and \
                file_ext(filename) in ALLOWED_EXTENSIONS
#returns everything but dot
def file_ext(filename):
        return os.path.splitext(filename)[1][1:].lower()

#copy the python code to a file and execute on EV3
def run_code(content):
        #print (content)
        code=content['code']
        #print (code)
        filename="filecode.py"

        with open(DIR_ROOT+'/'+filename,'w') as fd:
                fd.write(code)
        try:
                check=subprocess.check_output(["python3",DIR_ROOT+'/'+filename],stderr=subprocess.STDOUT)
                data={"value":0}
        except subprocess.CalledProcessError as e:

                s=e.output
                error=s.split(b',')[1]
                error=str(error)
                data={"value":"1", "infoerror": error}
        return(jsonify(data))

#upload a file from local computer on ev3dev and executes it
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
        if request.method == 'POST':
                if 'file' not in request.files:

                        return '', INVALID
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method="post" enctype="multipart/form-data">
                <input type=file name=file>
                <input type=submit value=Upload>
        </form>
        '''
#upload a file sent as form-data on ev3dev and executes it      
@app.route('/API/V1/EV3dev/file', methods=['GET','POST'])
def run_file():

        content=(request.get_data())
        code=content.decode('utf-8')#converts the string received as bytes to a$
        code=code.rsplit("\n", 2)[0] #delete the 2 last lines od the string (ar$
        code='\n'.join(code.split('\n')[3:]) #delete the 3 first lines of the s$
        length=code.count('\n')
        filename="pruebafile.py"
        with open(DIR_ROOT+'/'+filename,'w') as fd:
                fd.writelines("%s" % line for line in code)
        check=subprocess.call(["python3",DIR_ROOT+'/'+ filename])
        return(str(check))

@app.route('/uploaded', methods=['GET', 'POST'])
def uploaded_file():
        return '''
        <!doctype html>
        <title>Uploaded the file</title>
        <h1> File has been Successfully Uploaded </h1>
        '''

@app.route('/file', methods=['GET', 'POST'])
def file():
        content = request.get_json()

        filename="pruebafile.py"
        with open(DIR_ROOT+'/'+filename,'w') as fd:
                check=subprocess.call(["python3",DIR_ROOT+'/'+ filename])
        data={"code":check, "infoerror":sys.exc_info()}
        return (jsonify(data))
@app.route('/Motors', methods=['POST'])
def motors_move():
        content = request.get_json()
        return(str(motors_move_pw(content)))

@app.route('/Sensors', methods=['POST'])
def read_sensors():
        content = request.get_json()
        sensor_value=read_sensor(content)
        print("You are here!")
        return (str(sensor_value))

@app.route('/API/V1/EV3dev/Ports')
def info_ports():
        data = {"portValues":[]}
        items=[]
        itemaux={}
        for motor in list_motors():
        # data to be sent to GoogleSlides
                itemaux= {"portId":motor.address, "typeId":motor.driver_name, "modeIp":motor.connected, "value":motor.speed}
                items.append(itemaux)

        for sensor in list_sensors():
                s = SensorTypeSwitch()
                itemaux= {"portId":sensor.address, "typeId":sensor.driver_name,"modeIp":sensor.mode, "value":s.get_SensorValue(sensor.driver_name)}
                items.append(itemaux)

        data["portValues"]=items

        return jsonify(data)

@app.route('/API/V1/EV3dev/Ports/<string:portId>')
def info_port(portId):
        data = {"portValue":[]}
        items=[]

        for motor in list_motors(address=portId):

        # data to be sent to GoogleSlides
                itemaux= {"portId":motor.address, "typeId":motor.driver_name, "modeIp":motor.connected, "value":motor.speed}
                items.append(itemaux)

        for sensor in list_sensors(address=portId):
                s = SensorTypeSwitch()

                itemaux= {"portId":sensor.address, "typeId":sensor.driver_name,"modeIp":sensor.mode,"value":s.get_SensorValue(sensor.driver_name)}
                items.append(itemaux)

        data["portValue"]=items
        return jsonify(data)

@app.route('/API/V1/EV3dev/command', methods=['POST'])
def read_command():
        content = request.get_json()
        sensor_val=[]
        if(int(content['command'])<8):# send commands motors
                return(set_motor(content))
        if(int(content['command'])==10):#read sensors
                sensor_value=set_sensor(content)
                # print("Sensor value: ", str(sensor_value))
                # Hack way to distingish color values from other sensors
                if (type(sensor_value) is int):
                        colors={0:'unknown', 1:'black', 2:'blue', 3:'green', 4:'yellow', 5:'red', 6:'white', 7:'brown'}
                        if (sensor_value in colors):
                                publishToUnity('Color', colors[sensor_value])
                
                return (str(sensor_value))
        if(int(content['command'])==15):#run code
                return (run_code(content))
        if(int(content['command'])==16): #graph
                t0=time.time()
                
                for i in range (int(content['time'])):
                        sensorValue=set_sensor(content)
                        if(sensorValue=="ko"):
                                return (str(sensorValue))
                        if(i==0):
                                sensorTime=0
                        else:
                                t1=time.time()
                                sensorTime=t1-t0
                                
                        sensor_val.append({'value':sensorValue,'time':sensorTime})
                        time.sleep(1)
                        
                return jsonify(sensor_val)

@app.route('/API/V1/EV3dev/seqcode', methods=['POST'])
def seq_code():

        content = request.get_json()

        for i in range (len(content)):
                res=set_motor(content[i])
                if(res=="0"):
                        return(str(0))
        return(str(1))


if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True, threaded=True)

