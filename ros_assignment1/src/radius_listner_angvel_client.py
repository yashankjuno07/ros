#!usr/bin/env python
#license removed from brevity
import rospy
from std_msgs.msg import Float32
from ros_assignment1.srv import pc
from ros_assignment1.srv import compute_ang_vel
from ros_assignment1.srv import compute_ang_velRequest
from ros_assignment1.srv import compute_ang_velResponse
from geometry_msgs.msg import Twist



def compute_angular_vel_req_func(radius):
    rospy.wait_for_service('pc_service')

    try:
        ang_velocity=rospy.ServiceProxy('compute_ang_vel',compute_ang_vel)
        resp=ang_velocity(radius)
        return resp.ang_vel
    except rospy.ServiceException as e :
        print("Service call fail %s"%e)

def call_back(msg):
    rospy.loginfo("Received radius : %f"%msg.data)
    rospy.loginfo("Sending radius= %f to server"%msg.data)
    s= compute_angular_vel_req_func(msg.data)
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate=rospy.Rate(5)
    while not rospy.is_shutdown():
        move=Twist()
        move.linear.x=1#since linear_vel=1
        move.linear.y=0
        move.linear.z=0
        move.angular.x=0
        move.angular.y=0
        move.angular.z=s
        pub.publish(move)
        rate.sleep()

def main():
    rospy.init_node('radius_listner_angvel_client',anonymous=True)
    rospy.Subscriber('radius',Float32,call_back)
    rospy.spin()
if __name__=="__main__":
    main()