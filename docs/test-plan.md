# System Test Plan

This document establishes the testing protocols to validate the robot's hardware interface, serial communication, telemetry accuracy, motor controls, and ROS2 integration.

---

## 📋 General Testing Safety Requirements

> [!CAUTION]
> Never test the robot with the wheels on the ground unless you have already verified wheels-off-ground control, speed limits, and emergency stop overrides.

Every test run must follow the safety checks described in the [Motor Test Checklist](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/hardware/motor-test-checklist.md).

---

## 🧪 Test Procedures

### Test 1: Onboard Sensor Check
* **Objective:** Verify IMU and battery voltage output.
* **Environment:** Lifted configuration, USB connected.
* **Steps:**
  1. Boot the board and connect to a serial monitor.
  2. Query board telemetry parameters (battery voltage).
  3. Rotate the board by hand to verify accelerometer and gyroscope outputs update dynamically.
* **Expected Outcome:** Telemetry registers a stable voltage matching multimeter readings, and IMU data changes cleanly with movement.

### Test 2: Single Motor Directional Control
* **Objective:** Confirm motor M1-M4 direction and encoder polarity match.
* **Steps:**
  1. Follow the [Motor Test Checklist](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/hardware/motor-test-checklist.md).
  2. Command Motor 1 forward at low speed.
  3. Verify physical rotation is forward.
  4. Verify encoder counts increase.
  5. Repeat for Motors 2, 3, and 4.

### Test 3: udev Rule Verification
* **Objective:** Ensure the OS registers the serial driver board consistently.
* **Steps:**
  1. Unplug the board's USB cable from the Pi 5.
  2. Run `ls -l /dev/ttyUSB*` (should not show the bound symlink).
  3. Plug the board's USB back in.
  4. Run `ls -l /dev/ttyUSB_ROSBOARD`.
* **Expected Outcome:** The symlink `/dev/ttyUSB_ROSBOARD` is resolved pointing to the correct ttyUSB index (e.g. `/dev/ttyUSB0`).

### Test 4: Emergency Stop Response
* **Objective:** Ensure the board halts motors if the serial link drops or host script exits.
* **Steps:**
  1. Suspend the robot wheels.
  2. Command constant forward rotation to all motors.
  3. Unplug the USB serial cable from the Raspberry Pi.
* **Expected Outcome:** The board's safety watchdog triggers, halting all motor outputs within 500ms.
