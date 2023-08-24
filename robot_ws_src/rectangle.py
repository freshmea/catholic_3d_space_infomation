import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class Turtlemove(Node):
    def __init__(self):
        super().__init__('turtlemove')
        self.time = self.create_timer(0.1, self.test_callback)
        self.time2 = self.create_timer(0.01, self.update)
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.speed = 0.0
        self.angular = 0.0
        self.ptime = time.time()

    def test_callback(self):
        msg = Twist()
        msg.linear.x = self.speed
        msg.angular.z = self.angular
        self.pub.publish(msg)
        
    def update(self):
        if time.time()-self.ptime < 3:
            self.speed = 0.15
            self.angular = 0.0
        elif time.time()-self.ptime < 4:
            self.speed = 0.0
            self.angular = 1.6
        else:
            self.ptime = time.time()
        msg = Twist()
        msg.linear.x = self.speed
        msg.angular.z = self.angular
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Turtlemove()
    try:
        rclpy.spin(node)
    except:
        # stop code
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        node.pub.publish(msg)
        
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()