#!/usr/bin/env python
from __future__ import print_function
from AR_week4_test.srv import compute_cubic_traj, compute_cubic_trajResponse
import rospy
import numpy 

def polynomial_calculation(a):
    matrix = numpy.array([[1, a.t0, a.t0**2, a.t0**3],
                          [0, 1, 2*a.t0, 3*a.t0**2],
		          [1, a.tf, a.tf**2, a.tf**3],
                          [0, 1, 2*a.tf, 3*a.tf**2]])
    matrix_transpose = numpy.transpose(matrix)
    calc = numpy.array([[a.p0],
                     [a.v0],
                     [a.pf],
                     [a.vf]])
    x = numpy.dot(matrix_transpose, calc)

    rospy.loginfo(x[0], x[1], x[2], x[3])
    return compute_cubic_trajResponse(x[0], x[1], x[2], x[3])

def poly_trajectory_server():
    rospy.init_node('poly_trajectory_server')
    service = rospy.Service('poly_trajectory', compute_cubic_traj, polynomial_calculation)
    rospy.spin()

if __name__ == "__main__":
    poly_trajectory_server()
