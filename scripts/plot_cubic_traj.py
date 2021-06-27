#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from AR_week4_test.msg import cubic_traj_coeffs

def callback(data):
    rospy.loginfo('Output %s' % data)

def listener():
    rospy.init_node('client_listener', anonymous=True)
    rospy.Subscriber('client_chatter', cubic_traj_coeffs, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
