#!usr/bin/env python
#license removed from brevity
import rospy
from ros_assignment1.srv import pc
from ros_assignment1.srv import pcRequest
from ros_assignment1.srv import pcResponse
import math
import time

def handler_pc(req):
    rospy.loginfo("I have received : %f %f"%(req.first_coordinate,req.second_coordinate))
    time.sleep(5)
    if req.to_polar ==1:
        r = ( req.first_coordinate** 2 +  req.second_coordinate** 2) ** .5
        theta = math.degrees(math.atan2(req.second_coordinate,req.first_coordinate))
        resp=pcResponse(r,theta)
        return resp
    else:
        x= req.first_coordinate*(math.cos(req.second_coordinate))
        y=req.first_coordinate*(math.sin(req.second_coordinate))
        resp=pcResponse(x,y)
        return resp   

def main():
    rospy.init_node('pc_server',anonymous=True)
    s=rospy.Service('pc_service',pc,handler_pc)
    print("Ready to do conversions")
    rospy.spin()
    

if __name__=="__main__":
    try:
        main()
    except rospy.ROSInterruptException():
        pass  