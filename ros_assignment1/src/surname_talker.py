#!usr/bin/env python
#license removed from brevity
import rospy
from rospy.exceptions import ROSInterruptException
from std_msgs.msg import String
from ros_a1.msg import name_pub
def surname_func():
    pub2_surname=rospy.Publisher('surname',String,queue_size=10)
    rospy.init_node('surname_talker',anonymous=True)
    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
       
       surname="Dasrapuria"
       rospy.loginfo(surname)
       pub2_surname.publish(surname)
       rate.sleep()
    

if __name__=="__main__":
    try:
        surname_func()
    except rospy.ROSInterruptException():
        pass  