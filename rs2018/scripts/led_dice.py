#!/usr/bin/env python
import rospy
import roslib
import subprocess
from std_msgs.msg import String
import wiringpi as w
import time
import random

PIN_LED=25
OUTPUT=1

def callback(blink):
	if blink.data == ('go') :
		dice = random.randint(1, 6)
		print(dice)

		for i in range (dice) :
	 		w.digitalWrite(PIN_LED,1)
			time.sleep(0.5)
	 		w.digitalWrite(PIN_LED,0)
			time.sleep(0.5)

def led_blink():
	subprocess.check_call('gpio export 25 out',shell=True)
	rospy.init_node('led_dice_subscriber')
	w.wiringPiSetupSys()
	w.pinMode(PIN_LED,OUTPUT)
	rospy.Subscriber("blink",String,callback)
	rospy.spin()

if __name__=='__main__':
	led_blink()
