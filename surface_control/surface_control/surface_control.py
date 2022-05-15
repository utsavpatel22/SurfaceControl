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
            '/nav2_bt_message',
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
    
    cap = cv2.VideoCapture("/home/gamma-surface/serving_ws/src/surface_control/surface_control/test.mp4")
    is_video = True
    while True:
        if obj.is_changed:
            if obj.last_message == "Waiting for 7 seconds":
                img = cv2.imread("/home/gamma-surface/serving_ws/src/surface_control/surface_control/golden_2.jpeg")
                is_video = False

            elif obj.last_message == "Wait is over":
                cap = cv2.VideoCapture("/home/gamma-surface/serving_ws/src/surface_control/surface_control/test.mp4")
                is_video = True
            obj.is_changed = False

        if not is_video:
            cv2.imshow("Display",img)
            rclpy.spin_once(obj, timeout_sec=0.01)
            cv2.waitKey(10)
        else:
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow("Display", frame)
                rclpy.spin_once(obj, timeout_sec=0.01)
                cv2.waitKey(1)
            else:
                print("Video got over")
                cap = cv2.VideoCapture("/home/gamma-surface/serving_ws/src/surface_control/surface_control/test.mp4")
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