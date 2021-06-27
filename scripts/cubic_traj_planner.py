#!/usr/bin/env python
import rospy
from AR_week4_test.msg import cubic_traj_params, cubic_traj_coeffs
from AR_week4_test.srv import compute_cubic_traj, compute_cubic_trajRequest

def callback(data_value):
    rospy.wait_for_service('polynomial_trajectory')
    try:
        poly_trajectory = rospy.ServiceProxy('polynomial_trajectory', compute_cubic_traj)
        initialize = compute_cubic_trajRequest(data_value.p0, data_value.pf, data_value.v0, data_value.vf, data_value.t0, data_value.tf)
        soln = poly_trajectory(initialize)

        publish = rospy.Publisher('client_chatter', cubic_traj_coeffs, queue_size=10)
        publish.publish(soln.a0, soln.a1, soln.a2, soln.a3, data_value.t0, data_value.tf)

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", cubic_traj_params, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
