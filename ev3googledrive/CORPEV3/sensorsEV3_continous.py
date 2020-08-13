#!/usr/bin/env python3.4

from ev3dev.ev3 import *
from time import sleep
import paho.mqtt.client as mqtt
import threading
from threading import Thread, Event



def publish2Unity(distance, gyro, touch, color):
        broker = "broker.hivemq.com"
        MQTT_Broker = broker

        client = mqtt.Client()
        client.connect(MQTT_Broker,1883,60)
        # print("Connected with local", distance, gyro, touch, color)

        # temp = [str(sensor_type), str(sensor_value)]
        payload = "{distance}:{gyro}:{touch}:{color}".format(distance = distance, gyro = gyro, touch = touch, color = color)
        # print(payload)
        client.publish("topic/EV3Sensors", payload)

def runInLoop():
	check = True
	while(check):
		cl = ColorSensor('in4')
		ts = TouchSensor('in3')
		gy = GyroSensor('in2')
		us = UltrasonicSensor('in1')

		cl.mode='COL-COLOR'
		
		time.sleep(0.1)
		publish2Unity(us.value(),gy.value(),ts.value(),cl.value())
