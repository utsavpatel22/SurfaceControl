import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
import time


class RobotStatusSubscriber(Node):

    def __init__(self):
        super().__init__('robot_status_subscriber')
        self.node = rclpy.create_node("Surface_node")
        self.subscription = self.create_subscription(
            String,
            '/robot_status',
            self.robot_status_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.is_changed = False
        self.last_message = ""
        
    def robot_status_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        if self.last_message == msg.data:
            self.is_changed = False
        else:
            self.is_changed = True
            self.last_message = msg.data


def show_image_video(obj):
    cv2.namedWindow("Display", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Display", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    img =  cv2.imread("/home/gamma-surface/serving_ws/src/surface_control/surface_control/golden.jpg")
    while True:
        if obj.is_changed:
            if obj.last_message == "HI":
                img = cv2.imread("/home/gamma-surface/serving_ws/src/surface_control/surface_control/golden_2.jpeg")

        cv2.imshow("Display",img)
        rclpy.spin_once(obj, timeout_sec=0.01)
        cv2.waitKey(10)
    cv2.destroyAllWindows()




def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = RobotStatusSubscriber()
    show_image_video(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()