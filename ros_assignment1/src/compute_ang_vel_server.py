#!usr/bin/env python
#license removed from brevity
import rospy
from ros_assignment1.srv import pc
from ros_assignment1.srv import compute_ang_vel
from ros_assignment1.srv import compute_ang_velRequest
from ros_assignment1.srv import compute_ang_velResponse
import time

def handler_ang_vel(req):
    rospy.loginfo("Recieved radius : %f"%req.radius)
    time.sleep(5)
    resp=compute_ang_velResponse(1/req.radius)#since linear_vel=1
    return resp


def main():
    rospy.init_node('compute_ang_vel_server',anonymous=True)
    s=rospy.Service('compute_ang_vel',compute_ang_vel,handler_ang_vel)
    print("Ready to do conversions")
    rospy.spin()

if __name__=='__main__':
    main()