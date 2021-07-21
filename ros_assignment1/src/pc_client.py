#!usr/bin/env python
#license removed from brevity
import rospy
from ros_assignment1.srv import pc
from ros_assignment1.srv import pcRequest
from ros_assignment1.srv import pcResponse
import sys


def convert_coord_req(x,y,topolar):
    rospy.wait_for_service('pc_service')

    try:
        new_coord=rospy.ServiceProxy('pc_service',pc)
        resp=new_coord(x,y,topolar)
        return (resp.first_converted_coordinate,resp.second_converted_coordinate)
    except rospy.ServiceException as e :
        print("Service call fail %s"%e)









if __name__=="__main__":
    if len(sys.argv)==4:
        x=float(sys.argv[1])
        y=float(sys.argv[2])
        topolar=int(sys.argv[3])       
    else:
        print("%s [x y to_polar]"%sys.argv[0])
        sys.exit(1)
    print("sending request to service")
    r,theta=convert_coord_req(x,y,topolar)
    print("The converted coordinates are %f %f"%(r,theta))