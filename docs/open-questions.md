# Open Questions & Verifications

This document tracks unresolved technical details that require physical hardware inspection, diagnostic testing, or documentation confirmation.

---

## ❓ Hardware & Wiring Questions

### 1. Which IMU is populated on the board?
* **Details:** Official V3.0 documentation specifies the **ICM20948** 9-axis IMU, but several sample libraries reference register maps or drivers for the **MPU9250**.
* **Impact:** The internal registers, I2C addresses, and calibration values differ significantly between these two sensors. The correct ROS2 IMU driver cannot be selected until this is resolved.
* **Verification Plan:** 
  * Inspect the marking on the physical IMU IC under a magnifying glass.
  * Run an I2C scan utility on the Raspberry Pi 5 to discover the sensor's address (0x68 or 0x69 for MPU9250; 0x68/0x69 for ICM20948 depending on AD0 pin, but ICM20948 has WHO_AM_I value 0xEA, whereas MPU9250 has WHO_AM_I value 0x71/0x73).

### 2. What is the safe motor current limit?
* **Details:** The onboard H-bridge motor driver chips (often TB6612FNG or similar dual H-bridges on Yahboom boards) have a maximum current limit (typically 1.2A continuous, 3.2A peak per channel).
* **Impact:** Exceeding these limits under load or stall conditions will cause the driver chips to overheat, trigger thermal shutdown, or smoke.
* **Verification Plan:**
  * Identify the exact motor driver IC model on the PCB.
  * Retrieve the datasheet for the driver chip and record the continuous/peak current ratings.
  * Measure the stall current of the motors at 12V before mounting them on the robot.

### 3. What is the exact specification of the motors?
* **Details:** Motor voltage, gear ratio, and encoder pulses-per-revolution (PPR) must be known.
* **Impact:** Required to configure the STM32 firmware's PID loop and the Raspberry Pi's odometry calculation node (`odom -> base_link`).
* **Verification Plan:**
  * Match the motor part numbers with online manufacturer listings or datasheets.
  * Perform a manual test: spin the motor exactly 1 full rotation and count the encoder pulses recorded in software.

---

## 🔌 Power Distribution Questions

### 1. Is the onboard 5V buck converter sufficient for the Raspberry Pi 5?
* **Details:** The Raspberry Pi 5 can draw up to 5A of current under peak loads. If the onboard 5V regulator only supports 3A (typical for Pi 3/4 shields), the Pi 5 will display low-voltage warnings.
* **Impact:** System instability, sudden shutdowns under high CPU/GPU loads (e.g., during SLAM navigation).
* **Verification Plan:**
  * Locate the 5V buck converter IC on the Yahboom board and check its rated output in the schematic or datasheet.
  * Monitor the Raspberry Pi's system log (`dmesg` or `journalctl`) for undervoltage events.
