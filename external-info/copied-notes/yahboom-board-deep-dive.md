# Yahboom Robot Expansion Board V3.0 Deep Dive

This document compiles technical research, forum notes, and specifications copied from official Yahboom sources and developer reviews.

---

## 📋 What is the Board?

The **Yahboom Robot Expansion Board V3.0** is an MCU-driven hardware breakout board designed for robotic platforms (specifically 2WD/4WD vehicles, Mecanum/Omni-wheel rovers, and tank chassis). It operates as a low-level actuator and sensor driver, providing high-power motor drivers and signal distribution, while offloading high-level OS-driven robot logic (like SLAM, ROS2, and computer vision) to an attached single-board computer (SBC) like a Raspberry Pi.

---

## ⚡ Technical Specifications & Hardware Features

* **Microcontroller:** STM32F103RCT6 (ARM Cortex-M3, 72MHz, 256KB Flash, 48KB SRAM).
* **Motor Control Capabilities:** 
  * Drives up to 4x encoder-equipped DC motors (using onboard dual H-bridges, typically TB6612FNG or similar).
  * Direct support for up to 4x PWM servos (5V output) and daisy-chained serial bus servos.
* **Onboard Sensor:** 9-axis IMU (gyroscope, accelerometer, and magnetometer).
  * *Notice:* Some references point to **MPU9250** and others to **ICM20948**. Physical verification is required.
* **External Communication Interfaces:** 
  * Micro-USB or USB-C (integrated CH340 chip) for serial communication to the host computer.
  * CAN bus terminal port.
  * SBUS port for standard hobby RC receivers.
* **Power Management:**
  * Supported power input: 9.6V to 12.6V (optimized for 3S Lithium battery packs).
  * Integrated buck/step-down converter to supply 5V to the host SBC (Raspberry Pi).

---

## 💻 Compatible Hosts & Configurations

* **Compatible Hosts:**
  * Raspberry Pi 4B and Raspberry Pi 5.
  * NVIDIA Jetson Nano / Jetson Orin Nano.
  * Desktop computers / laptops (for testing via direct USB serial).
* **Supported Drive Configurations:**
  * 4WD Differential / Skid-steer (4-motor).
  * Mecanum wheel configuration.
  * Omni-wheel (3-wheel or 4-wheel) configurations.
  * Crawler / Tank chassis (2-motor or 4-motor configurations).

---

## 🚀 Software & Getting Started Path

1. **Firmware:** The onboard STM32 is pre-flashed with Yahboom's firmware, which parses command bytes over the CH340 serial bridge and responds with telemetry frames (battery, encoder ticks, IMU registers).
2. **Library API:** Yahboom provides a Python library named `Rosmaster` (`RosmasterV3.py`) to abstract the serial command protocol.
3. **ROS Integration:** Yahboom hosts open-source packages for both ROS1 (Noetic) and ROS2 (Fumble/Humble/Galactic/etc.) that launch nodes on the host Pi, parsing `/cmd_vel` into serial commands and translating serial telemetry frames into standard ROS topics.

---

## ⚠️ Known Gotchas & Warnings

* **Power Backfeeding:** Do not power the Raspberry Pi via its USB-C port while it is plugged into the Yahboom expansion board's power pins.
* **Buzzer Alarm:** The buzzer is configured to beep loudly if voltage falls below approximately 9.6V. This alarm can trigger due to momentary voltage drops when motors are commanded to start too rapidly.
* **Chassis Ground Loops:** Ensure the metal chassis of the robot does not short the bottom of the PCB, which has exposed solder pads for motor driver terminals.

---

## 🔗 Key Reference Links

* **Tutorial Portal:** [https://www.yahboom.net/study/ROS-Driver-Board](https://www.yahboom.net/study/ROS-Driver-Board)
* **GitHub Repository:** [https://github.com/YahboomTechnology/ROS-robot-expansion-board](https://github.com/YahboomTechnology/ROS-robot-expansion-board)
