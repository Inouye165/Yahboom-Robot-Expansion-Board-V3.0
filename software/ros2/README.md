# ROS2 Packages (`software/ros2/`)

This directory is designated for the ROS2 colcon workspace, hosting packages to bridge high-level ROS2 topics with the low-level serial protocol.

## Expected Structure

* **`src/yahboom_ros_board_bridge/` (Future addition):** A custom ROS2 package containing:
  * A node subscribing to `/cmd_vel` and converting it to serial packets for the STM32 board.
  * A node reading serial data and publishing:
    * `/imu/data_raw` (IMU sensor frames)
    * `/odom_raw` (Raw encoder ticks or velocity state)
    * `/voltage` (Battery health)
