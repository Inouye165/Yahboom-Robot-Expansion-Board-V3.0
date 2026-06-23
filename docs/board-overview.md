# Yahboom Robot Expansion Board V3.0 Overview

This document outlines the hardware features, interfaces, and core specifications of the Yahboom Robot Expansion Board V3.0.

---

## 🎛️ Core Specifications

* **Low-Level Microcontroller:** **STM32F103RCT6**
  * Core: ARM 32-bit Cortex-M3
  * CPU Frequency: 72 MHz
  * Flash Memory: 256 KB
  * SRAM: 48 KB
  * Purpose: Real-time motor PWM control, quadrature encoder decoding, servo signal generation, sensor polling, and host communication.
* **Onboard IMU (Inertial Measurement Unit):** 9-axis sensor.
  * > [!WARNING]
    > **Hardware Discrepancy (VERIFY):** Official V3.0 documentation points to the **ICM20948** 9-axis IMU, but older materials and codebases mention the **MPU9250**. 
    > **Action Item:** Inspect the physical chip package or run a register-checking utility script to verify the exact model.
* **Host Computer Support:** Specifically designed to interface with single board computers, optimized here for the **Raspberry Pi 5**.

---

## 🔌 Interface & Peripheral Breakdown

### 1. Actuator Interfaces
* **4x Encoder DC Motor Ports:**
  * Supported channels: Motor 1, Motor 2, Motor 3, Motor 4.
  * Integrated quadrature encoder feedback.
* **PWM Servo Interfaces:**
  * Support for standard 3-pin PWM servos (5V signal level).
* **Serial Bus Servo Interfaces:**
  * Support for daisy-chained serial bus servos (e.g., LX-15D or similar bus protocols).

### 2. Communication Interfaces
* **USB-to-Serial Port:**
  * Onboard CH340 chip. Connects to the host PC/Raspberry Pi for data exchange.
* **CAN Bus Interface:**
  * For industrial-style differential serial communication.
* **SBUS Interface:**
  * For RC receiver input (e.g., Flysky, Futaba receivers).

### 3. Power Distribution & SBC Interface
* **Raspberry Pi Power Delivery:**
  * The board can supply power to the Raspberry Pi through designated pins, but power configuration must be carefully checked (see [Power and Safety Guide](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/power-and-safety.md)).

---

## 🤖 ROS1 / ROS2 Materials Compatibility

Although this board has robust ROS1 and ROS2 example packages, it is **not** a MicroROS/ESP32 board. It does not possess onboard Wi-Fi. 
* All ROS2 node execution, networking, and high-level computation occur on the **Raspberry Pi 5**.
* The STM32 board behaves strictly as a dumb serial executor/peripheral node responding to commands over USB serial.
