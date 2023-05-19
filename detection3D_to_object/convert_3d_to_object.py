import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32
from vision_msgs.msg import Detection3DArray
from cwm_msgs.msg import Object
from cwm_msgs.msg import ObjectList
from cwm_msgs.msg import ObjectState
from cwm_msgs.msg import ObjectCategory
from tf_transformations import euler_from_quaternion


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.publisher_ = self.create_publisher(ObjectList, 'object_list', 10)
        self.subscription = self.create_subscription(
            Detection3DArray,
            'bbox',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        detected_object_list = ObjectList()
        detected_object_list.header = msg.header
        for index, detection in enumerate(msg.detections):
    	     #print(f"DETECTED_OBJECT:{index}....DETECTION_BBOX_SIZE_X:{detection.bbox.size.x}")
    	     #print(f"DETECTED_OBJECT:{index}....DETECTION_BBOX_SIZE_Y:{detection.bbox.size.y}")
    	     #print(f"DETECTED_OBJECT:{index}....DETECTION_BBOX_SIZE_Z:{detection.bbox.size.z}")
    	     #print(f"DETECTED_OBJECT:{index}....DETECTION_CENTER_GRAVITY_X:{detection.bbox.center.position.x}")
    	     #print(f"DETECTED_OBJECT:{index}....DETECTION_CENTER_GRAVITY_Y:{detection.bbox.center.position.y}")
    	     #print(f"DETECTED_OBJECT:{index}....DETECTION_CENTER_GRAVITY_Z:{detection.bbox.center.position.z}")
    	     detected_object = Object()
    	     
    	     detected_object.length = detection.bbox.size.x
    	     detected_object.width = detection.bbox.size.y
    	     detected_object.height = detection.bbox.size.z
    	     detected_object.x_centroid = detection.bbox.center.position.x
    	     detected_object.y_centroid = detection.bbox.center.position.y
    	     detected_object.z_centroid = detection.bbox.center.position.z
    	     
    	     detected_object.stamp = detection.header.stamp
    	     
    	     detected_object_state = ObjectState()
    	     #position
    	     detected_object_state.x  = detection.bbox.center.position.x
    	     detected_object_state.y  = detection.bbox.center.position.y
    	     detected_object_state.z  = detection.bbox.center.position.z
    	     #orientation
    	     orientation_q = detection.bbox.center.orientation
    	     orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    	     (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
    	     detected_object_state.yaw = yaw
    	     
    	     detected_object.state = detected_object_state
    	     
    	     #category
    	     object_category = ObjectCategory()
    	     object_category.category = ObjectCategory().PERSON
    	     
    	     detected_object.category_list.append(object_category)
    	     
    	     #Wrap    	     
    	     detected_object_list.dynamic_object_list.append(detected_object)
    	     
        #self.get_logger().info('Object: "%s"' % object_test)
        #self.get_logger().info('ObjectList: "%s"' % object_list_test)
        
        
        print(f"DETECTED_OBJECT_list: {detected_object_list}")
        
        self.publisher_.publish(detected_object_list)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
