# detection3d_to_object
ROS2 Node that remaps a Detection3DArray msg to an ObjectList msg.

# Initialize the node
command: <b>ros2 run detection3D_to_object detector</b>

The node is subscribed to: <b>/bbox topic</b>
</br>
</br>
The /bbox topic is being published by the TAO-Pointpillar Node which is of type  <b>vision_msgs/msg/Detection3DArray</b>
</br>
</br>
This node publish to: <b>/object_list</b>
</br>
</br>
The /object_list topic is of type  <b>cwm_msgs/msg/ObjectList</b>
