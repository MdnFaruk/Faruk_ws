#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random, math

def callback(data):
    vel_msg = Twist()
    pose = data
    d = math.sqrt(math.pow(10 - vel_msg.linear.x,2) + math.pow(10 - vel_msg.linear.y,2))
    
    if pose.x > 10:
        vel_msg.angular.z = 0
        vel_msg.linear.x = -2
        
    elif pose.x < 1:
        vel_msg.angular.z = 0
        vel_msg.linear.x = -2
         
    elif pose.y > 10:
        vel_msg.angular.z = 0
        vel_msg.linear.x = -2

    elif pose.y < 1:
        vel_msg.angular.z = 0
        vel_msg.linear.x = -2

    else: 
        vel_msg.angular.z = random.randint(1,10)
        vel_msg.linear.x = random.randint(0,10)
    
    if (d == 0):   
        vel_msg.angular.z = random.randint(1,10)
        vel_msg.linear.x = random.randint(0,10) 

    velocity_publisher.publish(vel_msg)                

rospy.init_node('turtlebot_auto', anonymous=True)
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose,callback)

while not rospy.is_shutdown():
    rospy.spin()
    rospy.Rate(10).sleep()