#1/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    pub2 = rospy.Publisher('new/chatter', String, queue_size=10)
    rate = rospy.Rate(10)
    start_time = rospy.get_time()
    end_time = start_time + 30
    change_pub = False
    constent_pub = "no object"
    while not change_pub and not rospy.is_shutdown():
        pub.publish("moving")
        rate.sleep
    while not rospy.is_shutdown():
        current_time = rospy.get_time()
        if current_time == end_time:
            constent_pub = "object"
            change_pub = True
        rate.sleep
    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass