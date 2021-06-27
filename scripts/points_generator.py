#!/usr/bin/env python
import rospy
import random
import numpy 
from std_msgs.msg import String
from AR_week4_test.msg import cubic_traj_params

def talker():
    publisher = rospy.Publisher('chatter', cubic_traj_params, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.05) 
    numbers = cubic_traj_params()
    while not rospy.is_shutdown():
        numbers.p0 = numpy.random.uniform(-10,10)
	numbers.pf = numpy.random.uniform(-10,10)
	numbers.v0 = numpy.random.uniform(-10,10)
	numbers.vf = numpy.random.uniform(-10,10)
	numbers.t0 = 0 
        dt = numpy.random.uniform(5,10)
	numbers.tf = numbers.t0 + dt
	rospy.loginfo(numbers)
	publisher.publish(numbers)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
