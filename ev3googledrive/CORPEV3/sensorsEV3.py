#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

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
        rgb_raw=[]
        default="invalid"
        type=content['typeId']
        try:
                if(type=='Touch'):
                        port='in'+str(content['port'])
                        ts = TouchSensor(port)
                        return ts.value()
                if(type=='Color'):
                        port='in'+str(content['port'])
                        cl = ColorSensor(port)
                        cl.mode=content['modeId']
                        if(cl.mode=="RGB-RAW"):
                                rgb_raw.append(cl.value(0))
                                rgb_raw.append(cl.value(1))
                                rgb_raw.append(cl.value(2))
                                return rgb_raw
                        else:
                                return cl.value()
                if(type=='Gyro'):
                        port='in'+str(content['port'])
                        gy = GyroSensor(port)
                        gy.mode=content['modeId']
                        return gy.value()
                if(type=='Ultrasonic'):
                        port='in'+str(content['port'])
                        us=UltrasonicSensor(port)
                        us.mode=content['modeId']
                        return us.value()
                if(type=='Infrared'):
                        port='in'+str(content['port'])
                        ir = InfraredSensor(port)
                        ir.mode=content['modeId']
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

