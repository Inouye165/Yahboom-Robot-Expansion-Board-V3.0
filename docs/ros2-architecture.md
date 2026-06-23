# ROS2 Control Architecture

This document describes the distribution of processes and nodes across the robot platform, detailing the communication path and topic design.

---

## 🔀 Component Breakdown

```
+-------------------------------------------------------+
|                 Raspberry Pi 5 Host                   |
|  - High-Level Processing, Localization & Mapping       |
|                                                       |
|  +------------------+          +-------------------+  |
|  |     ROS2 Nav2    |          |     SLAM Toolbox  |  |
|  +------------------+          +-------------------+  |
|  +------------------+          +-------------------+  |
|  |   Camera Node    |          |     Lidar Node    |  |
|  +------------------+          +-------------------+  |
|  +-------------------------------------------------+  |
|  |                 ROS2 Hardware Node              |  |
|  +-------------------------------------------------+  |
+---------------------------+---------------------------+
                            |
                     (USB Serial Link)
                            |
+---------------------------v---------------------------+
|          Yahboom STM32 Board (Low-Level Controller)   |
|  - Real-time hardware control loop                    |
|                                                       |
|  +------------------+          +-------------------+  |
|  |  Motor PWM/PID   |          |  Encoder Reading  |  |
|  +------------------+          +-------------------+  |
|  +------------------+          +-------------------+  |
|  |  IMU Reading     |          |  Servo Control    |  |
|  +------------------+          +-------------------+  |
+-------------------------------------------------------+
```

### Raspberry Pi 5 (High-Level Controller)
The Raspberry Pi 5 runs standard Linux and handles complex, CPU-intensive tasks:
* **Operating System:** Ubuntu Server (configured with ROS2 Jazzy, Iron, or Humble).
* **High-Level Control Logic:** Navigation (`Nav2`), SLAM mapping, sensor drivers (LiDAR and camera), web control servers, and Wi-Fi teleoperation.
* **ROS2 Drivers:** Interprets sensor values and computes target velocities, sending raw speed directives to the STM32 board.

### Yahboom STM32 Board (Low-Level Controller)
The STM32F103RCT6 MCU acts as a real-time hardware interface:
* **Motor Control:** Processes wheel velocity commands and executes closed-loop PID control via PWM.
* **Feedback:** Decodes quadrature encoders and polls the 9-axis onboard IMU.
* **Peripherals:** Controls PWM/serial bus servos and monitors board voltage/current telemetry.
* **Timing:** Maintains a deterministic control loop (typically 50-100Hz) to prevent motor runaways.

---

## 🔌 Connection & Serial Binding

* **Interface:** USB to Serial connection using the board's Micro-USB/USB-C interface connected to one of the USB 3.0 ports on the Raspberry Pi 5.
* **udev Rule:** A custom rule binds the CH340 USB serial bridge vendor/product ID to `/dev/ttyUSB_ROSBOARD` (or `/dev/myserial`). This ensures consistent naming across reboots (see [udev rules folder](file:///c:/Users/inouy\electronics-project-hub\driver-boards\Yahboom_Robot_Expansion_Board_V3.0/software/udev/README.md)).

---

## 📡 Expected ROS2 Topics

The following topics will be registered and verified:

| Topic | Message Type | Direction (Pi 5 Perspective) | Description |
| :--- | :--- | :--- | :--- |
| `/cmd_vel` | `geometry_msgs/msg/Twist` | **Publish** | Speed commands (linear/angular velocities) |
| `/imu/data_raw` | `sensor_msgs/msg/Imu` | **Subscribe** | Raw accelerometer and gyroscope data from onboard IMU |
| `/imu/mag` | `sensor_msgs/msg/MagneticField` | **Subscribe** | Magnetometer readings (if supported/verified) |
| `/vel_raw` or `/odom_raw` | `geometry_msgs/msg/TwistStamped` | **Subscribe** | Unfiltered velocity feedback decoded from encoders |
| `/voltage` | `std_msgs/msg/Float32` | **Subscribe** | Battery level telemetry for monitoring low-power conditions |
| `/odom` | `nav_msgs/msg/Odometry` | **Publish** | Calculated wheel odometry (after fuse/localization) |
| `/scan` | `sensor_msgs/msg/LaserScan` | **Publish** | Lidar distance readings for SLAM (produced by Pi-connected Lidar) |
| `/tf` / `/tf_static` | `tf2_msgs/msg/TFMessage` | **Bi-directional** | Transformation tree mapping coordinates (odom -> base_link) |
