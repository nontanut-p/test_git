import rclpy
from rclpy.node import Node
import numpy as np 
from std_msgs.msg import String

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose 

class TurtlesimCommand(Node):

    def __init__(self):
        super().__init__('TurtlesimCommand_Node')
        self.command_publisher = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.mysub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10 )
        timer_period = 0.1 # seconds
        self.timer = self.create_timer(timer_period,self.timer_callback)
        self.i = 0
        self.pose = Pose()
        self.goal = np.array([8.0,4.0])
        #self.pose_subscription = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
    def rand_goal(self):
        self.goal = np.random.randint(10,size = 2)
        print(self.goal)
    def pose_callback(self,msg):
        self.pose = msg

    def timer_callback(self):
        msg = self.control()
        self.command_publisher.publish(msg)

    def control(self):
        msg = Twist()
        current_position = np.array([self.pose.x,self.pose.y])
        dp = self.goal-current_position
        e = np.arctan2(dp[1],dp[0])-self.pose.theta
        K = 3.0
        w = K*np.arctan2(np.sin(e),np.cos(e))
        
        if np.linalg.norm(dp) > 0.1:
            v = 1.0
        else:
            v = 0.0
            print('000')
            self.rand_goal()

        msg.linear.x = v
        msg.angular.z = w
        return msg

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = TurtlesimCommand()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()