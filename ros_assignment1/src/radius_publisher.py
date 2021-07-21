#!usr/bin/env python
#license removed from brevity
import rospy
import sys
from std_msgs.msg import Float32




def main():
    rospy.init_node('radius_publisher',anonymous=True)
    pub=rospy.Publisher('radius',Float32,queue_size=10)
    rate=rospy.Rate(5)
    while not rospy.is_shutdown():
           if len(sys.argv)==2:
                 rad=sys.argv[1]
           else :
               print("%s [radius]"%sys.argv[0]) 
               sys.exit(1)    
           pub.publish(rad)
           rate.sleep()


if __name__=="__main__":
     main()