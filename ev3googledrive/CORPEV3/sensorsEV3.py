#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

import paho.mqtt.client as mqtt

def publishToUnity(sensor_type, sensor_value):
        broker = "broker.hivemq.com"
        MQTT_Broker = broker

        client = mqtt.Client()
        client.connect(MQTT_Broker,1883,60)
        # print("Connected with local")

        # temp = [str(sensor_type), str(sensor_value)]
        payload = "{sensor}:{value}".format(sensor = sensor_type, value = sensor_value)
        print(payload)
        client.publish("topic/EV3ARProject", payload)
        # client.disconnect();

def read_sensor(sensor):
        print (sensor)
        print (sensor['name'])
        print (sensor['port'])
        # Connect EV3 color sensor
        cl = ColorSensor(sensor['port'])
        # Put the color sensor into COL-REFLECT mode
        # to measure reflected light intensity.
        # In this mode the sensor will return a value between 0 and 100
        cl.mode='COL-REFLECT'
        return (str(cl.value()))

# Implement Python Switch Case Statement using Class
def set_sensor(content):
        # print(content)
        rgb_raw=[]
        default="invalid"
        type=content['typeId']
        try:
                if(type=='Touch'):
                        port='in'+str(content['port'])
                        ts = TouchSensor(port)
                        print("touch sensor: " + str(ts.value()))
                        
                        publishToUnity(type, ts.value())

                        return str(ts.value())
                if(type=='Color'):
                        port='in'+str(content['port'])
                        cl = ColorSensor(port)
                        cl.mode=content['modeId']
                        if(cl.mode=="RGB-RAW"):
                                rgb_raw.append(cl.value(0))
                                rgb_raw.append(cl.value(1))
                                rgb_raw.append(cl.value(2))
                                print("Color Raw: " + str(rgb_raw))
                                
                                publishToUnity(type, rgb_raw)

                                return rgb_raw

                        else:
                        
                                return cl.value()
                if(type=='Gyro'):
                        port='in'+str(content['port'])
                        gy = GyroSensor(port)
                        gy.mode=content['modeId']
                        print("Gryo sensor: " + str(gy.value()))
                        
                        publishToUnity(type, gy.value())

                        return gy.value()
                if(type=='Ultrasonic'):
                        port='in'+str(content['port'])
                        us=UltrasonicSensor(port)
                        us.mode=content['modeId']
                        print("Ultrasonic sensor: " + str(us.value()))

                        publishToUnity(type, us.value())

                        return us.value()
                if(type=='Infrared'):
                        port='in'+str(content['port'])
                        ir = InfraredSensor(port)
                        ir.mode=content['modeId']
                        print("Infrared sensor: " + str(ir.value()))

                        publishToUnity(type, ir.value())

                        return ir.value()
        except:
                return ("ko")


class SensorTypeSwitch:

        def get_SensorValue(self, typeId):
                default = "Incorrect typeId"
                if (typeId=="lego-ev3-touch"):
                        new_typeId="touch"
                if (typeId=="lego-ev3-color"):
                        new_typeId="color"
                if (typeId=="lego-ev3-gyro"):
                        new_typeId="gyro"
                if (typeId=="lego-ev3-ir"):
                        new_typeId="infrared"
                if (typeId=="lego-ev3-us"):
                        new_typeId="ultrasonic"
                return getattr(self, 'case_' + str(new_typeId), lambda: default)()

        def case_touch(self):
                ts = TouchSensor()
                return ts.value()
        def case_color(self):
                cl = ColorSensor()
                print(c1, c1.value())
                return cl.value()
        def case_gyro(self):
                gy = GyroSensor()
                return gy.value()
        def case_ultrasonic(self):
                us=UltrasonicSensor()
                return us.value()
        def case_infrared(self):
                ir = InfraredSensor()
                return ir.value()

