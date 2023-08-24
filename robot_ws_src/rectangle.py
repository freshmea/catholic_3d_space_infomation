import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Turtlemove(Node):
    def __init__(self):
        super().__init__('turtlemove')
        self.time = self.create_timer(0.1, self.test_callback)
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)

    def test_callback(self):
        msg = Twist()
        msg.linear.x = 0.15
        msg.angular.z = 0.5
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