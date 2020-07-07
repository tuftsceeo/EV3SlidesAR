#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep


def motors_move_pw(motors):
        print (motors)
        print (motors[0])
        list_motors=motors[0]
        for k, v in motors[0].items():
                print(k, v)
                if int(v)>0:
                        m = LargeMotor(k)
                        if(m.connected):
                                print(m.connected)
                                m.run_forever(speed_sp=v)
                                sleep(5)
                                m.stop(stop_action="hold")
                                # to make extra sure the motors have stopped:
                               
                                sleep(5)
                        else:
                                return (str(0))
        return (str(1))

def set_motor(command):
        large_motors=[];
        medium_motors=[];
        try:
                power = int(command['speed'])
                num_motors=len(command['port'])
                
                if command['typeId'] == "LargeMotor":
                        for i, v in enumerate (command['port']):
                                
                                large_motors.append(LargeMotor(v)); #assert large_motors[i].connected   

                if command['typeId']== "MediumMotor":
                       
                        for i, v in enumerate (command['port']):
                                large_motors.append(MediumMotor(v)); #assert medium_motors[i].connected
                if(command['stopmode'] ==""):
                        command['stopmode']="brake"
                if command['command'] == "1":#run_forever
                        length=len(large_motors)
                        for i in range(length):
                                large_motors[i].run_forever(speed_sp=power)
                        sleep(1)
                if command['command'] =="2":#run_to_abs_pos use positive ([0-900]) for speed_sp (negatives values to run reverse are ignore). 
                                        #For run reverse, use a negative value for position_sp rather than for speed_sp
                        for i in range(len(large_motors)):
                                large_motors[i].run_to_abs_pos(position_sp=command['position'], speed_sp=power, stop_action=command['stopmode'])
                        sleep(1)
                if command['command'] =="3":#run_to_rel_pos
                        for i in range(len(large_motors)):
                                large_motors[i].run_to_rel_pos(position_sp=command['position'], speed_sp=power, stop_action=command['stopmode'])
                        sleep(1)
                if command['command'] == '4':#run_timed
                        for i in range(len(large_motors)):
                                large_motors[i].run_timed(time_sp=command['time'], speed_sp=power, stop_action=command['stopmode'])
                        for i in range(len(large_motors)):
                                large_motors[i].wait_while("running")
                        sleep(1)
                if command['command'] =="5":#run_direct is controlled by duty_cicle_sp (not speed_sp)
                                        # negative values of duty_cicle_sp causes the motor to rotate inverse
                        for i in range(len(large_motors)):
                                large_motors[i].run_direct(duty_cycle_sp=power)
                        sleep(1)
                if command['command'] == "6":#stop Stop any of the run commands before they are complete using the command specified by stop_action.
                        for i in range(len(large_motors)):
                                large_motors[i].stop(stop_action=command['stopmode'])
                if command['command'] == "7":#reset. Resets all of the motor parameter attributes to their default values. 
                                                                                #This will also have the effect of stopping the motor.
                        for i in range(len(large_motors)):
                                large_motors[i].reset()
                if command['command'] == "switch_polarity":#switch_polarity
                        i.duty_cycle_sp(i.duty_cycle_sp * -1)
                if command['command'] == "8":
                        for motor in list_motors():
                                motor.stop(stop_action=value)
                return (str(1))
        except:
                return (str(0))
