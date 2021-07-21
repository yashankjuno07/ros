#!usr/bin/env python
#license removed from brevity
import rospy
from rospy.exceptions import ROSInterruptException
from std_msgs.msg import String
from ros_a1.msg import name_pub
def name_func():
    pub1_name=rospy.Publisher('name',String,queue_size=10)
    rospy.init_node('name_talker',anonymous=True)
    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
       
       name="Yashank"
       rospy.loginfo(name)
       pub1_name.publish(name)
       rate.sleep()
    

if __name__=="__main__":
    try:
        name_func()
    except rospy.ROSInterruptException():
        pass  