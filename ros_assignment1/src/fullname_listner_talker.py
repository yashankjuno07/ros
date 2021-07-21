#!usr/bin/env python
from os import strerror
import rospy 
from std_msgs.msg import String
from ros_a1.msg import name_pub

pub = rospy.Publisher('fullname',String,queue_size=10)



    
            


def call_back1(msg):
    rospy.loginfo(msg.data)
    name_rec= msg.data
    return name_rec
    

def call_back2(msg):
    rospy.loginfo(msg.data)
    surname_rec= msg.data
    return surname_rec
    
    


rospy.init_node('fullname_listner_talker',anonymous=True)
sub1=rospy.Subscriber('name',String,call_back1)
ob1=call_back1()
sub2=rospy.Subscriber('surname',String,call_back2)
ob2=call_back2()
while not rospy.is_shutdown():
    joint="%s %s"%(ob1,ob2)
    pub.publish(joint)