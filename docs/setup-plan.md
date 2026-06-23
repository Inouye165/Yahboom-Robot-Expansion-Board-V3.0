# Phased Robot Bring-up Plan

This setup plan outlines the progressive development and safety checks required to bring the Yahboom Robot Expansion Board V3.0 and Raspberry Pi 5 platform online.

---

## 📅 Phases Overview

```mermaid
gantt
    title Bring-up Phases
    dateFormat  X
    axisFormat %d
    section Bring-up
    Phase 0: Documentation & Safety  :active, p0, 0, 3
    Phase 1: Board-Only Power Test  : p1, after p0, 2d
    Phase 2: Pi Communication       : p2, after p1, 3d
    Phase 3: One Motor Lifted       : p3, after p2, 2d
    Phase 4: Four Motors Lifted     : p4, after p3, 2d
    Phase 5: Ground Driving         : p5, after p4, 3d
    Phase 6: ROS2 Architecture      : p6, after p5, 5d
```

---

## 🛠️ Step-by-Step Breakdown

### Phase 0 — Documentation & Safety
* **Objective:** Establish reference manuals, safety labels, and verify wiring harness pinouts.
* **Tasks:**
  * Download official PDFs, schematics, and example codes from the official repository (record links in [Source Links](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/source-links.md)).
  * Place research screenshots into `external-info/screenshots/`.
  * Physically print and attach labels to the board ports.
  * Verify input power ports vs accessory output ports.
  * Measure and verify motor/encoder connector pins with a multimeter to ensure they match the reference pinout in [Wiring and Pinouts](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/wiring-and-pinouts.md).

### Phase 1 — Board-Only Power Test
* **Objective:** Confirm board power regulator integrity without loading.
* **Tasks:**
  * Install an inline fuse (3A to 5A) on the battery positive wire.
  * Connect the battery to the board's main power input (ensure all motor/servo headers are empty).
  * Power on and inspect the board: watch for smoke, check for localized heat, listen for abnormal buzzer sounds, and observe status LEDs.
  * Measure accessory outputs: verify the 5V out and 12V out ports read correctly using a multimeter.

### Phase 2 — Raspberry Pi Communication
* **Objective:** Link the Raspberry Pi 5 to the STM32 board and establish serial communication.
* **Tasks:**
  * Power the Pi 5 separately (do not double-power it from the board's header yet).
  * Connect a USB cable from the Pi 5 to the board's CH340 serial bridge interface.
  * Run `lsusb` and `udevadm` to verify the chip is detected.
  * Copy and enable the udev rule from [99-yahboom-ros-board.rules.example](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/software/udev/99-yahboom-ros-board.rules.example).
  * Test communication using python-rosmaster or basic serial scripts to fetch battery voltage or firmware version.

### Phase 3 — One Motor Test
* **Objective:** Verify a single motor channel's PWM control and encoder direction.
* **Tasks:**
  * Setup the robot chassis on blocks so all wheels are suspended off the ground.
  * Plug in a single motor (e.g., Channel 1 / M1).
  * Run a safety check stub and small test script to command a low PWM value for 1-2 seconds.
  * Confirm the wheel rotates forward and the encoder count increases in the positive direction.
  * Be ready to pull power immediately if it runs away.

### Phase 4 — Four Motor Test Lifted
* **Objective:** Calibrate and verify all four motor channels simultaneously in a suspended configuration.
* **Tasks:**
  * Plug in all four motors.
  * Keep wheels lifted.
  * Command a low speed to all motor channels.
  * Verify correct individual wheel rotation direction (Front-Left, Rear-Left, Front-Right, Rear-Right).
  * Check that encoder values correspond to physical movement on all 4 channels.

### Phase 5 — Ground Driving
* **Objective:** Test mechanical and power stability under load.
* **Tasks:**
  * Place the robot on the floor in an open space.
  * Run slow forward/backward commands.
  * Monitor battery voltage drop and watch for motor controller heating.
  * Test teleoperation using a controller or keyboard interface.

### Phase 6 — ROS2 Integration
* **Objective:** Deploy full ROS2 logic and sensor-based localization.
* **Tasks:**
  * Bring up the ROS2 node on the Pi 5 to parse `/cmd_vel` commands into serial packets for the board.
  * Subscribe to the board's telemetry and publish IMU data on `/imu/data_raw` and encoder feedback on `/odom`.
  * Tune motor controller PID settings.
  * Add LiDAR nodes, SLAM (`slam_toolbox`), and navigation planners (`Nav2`).
