# Troubleshooting Guide

This document lists known issues, root causes, and verification steps for common problems with the Yahboom Robot Expansion Board V3.0 and Raspberry Pi 5 platform.

---

## 🚨 Power & Hardware Issues

### 1. Board beeps low battery even with 12V adapter connected
* **Description:** The buzzer sounds continuously or periodically, warning of a low-voltage battery state.
* **Causes:**
  * Some 12V wall adapters experience severe voltage sag under load, dropping below the board's low-voltage threshold (typically around 9.6V to 10V).
  * The voltage-detection divider circuit on the board is out of calibration.
* **Resolution:** 
  * Switch to a high-current battery (e.g., 3S LiPo) or a regulated bench power supply capable of supplying at least 3A-5A at 12V.
  * Measure the voltage at the input terminal block with a multimeter while the buzzer is active.

### 2. Raspberry Pi 5 not powering correctly
* **Description:** The Pi 5 fails to boot, boots into low-power throttling mode, or experiences random restarts.
* **Causes:**
  * The Raspberry Pi 5 requires up to 5V/5A power delivery. The onboard buck converter might only supply 5V/3A, triggering a low-power warning.
  * Thin or long power wires from the board to the Pi GPIO headers are causing voltage drops.
* **Resolution:**
  * Verify the gauge of the power wires. Use short, high-quality jumper wires.
  * If throttling persists, power the Raspberry Pi 5 directly from an official USB-C Power Supply and disconnect the Pi power lines from the Yahboom board. 
  * > [!WARNING]
    > Remember to remove the board-to-Pi power jumpers before plugging in the external USB-C supply. Do not power from both sources.

### 3. Onboard components or motor drivers heat up rapidly
* **Description:** The motor driver ICs or the STM32 chip become hot to the touch.
* **Causes:**
  * Motor windings are shorted or the motor is stalled.
  * Encoder VCC/GND wires are swapped, shorting the logic rail to ground.
* **Resolution:**
  * Power down the board immediately.
  * Unplug all motor connectors and check resistance across the motor terminals and encoder leads.

### 4. USB port mechanically fragile
* **Description:** The Micro-USB or USB-C port on the board feels loose or disconnects during movement.
* **Causes:**
  * Poor mechanical strain relief on the board's connector.
* **Resolution:**
  * Use a right-angle USB cable and secure it to the robot chassis using zip ties or a 3D-printed cable clamp to prevent physical stress on the port.

---

## 🔌 Communication & Flashing Issues

### 1. Serial device not found / COM port changes between boots
* **Description:** The host computer or Pi 5 cannot open the serial port or the serial port changes names (e.g., from `/dev/ttyUSB0` to `/dev/ttyUSB1`).
* **Causes:**
  * Other USB serial devices (e.g., LiDAR or GPS) are plugged in, causing arbitrary device allocation order by the Linux kernel.
* **Resolution:**
  * Implement and enable the custom udev rule located in [99-yahboom-ros-board.rules.example](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/software/udev/99-yahboom-ros-board.rules.example).
  * Use the symlink `/dev/ttyUSB_ROSBOARD` instead of `/dev/ttyUSB0` in your software nodes.

### 2. MCUISP / FlyMCU flashing issues
* **Description:** Flashing new firmware to the STM32 via USB fails.
* **Causes:**
  * Boot configuration jumpers are in the wrong positions.
  * Reset/Boot control signals are not properly managed by the CH340 RTS/DTR lines.
* **Resolution:**
  * Confirm the BOOT0 and BOOT1 jumper placements on the board. Usually, BOOT0 must be jumped to VCC for programming, and returned to GND for standard boot execution.

---

## ⚙️ Actuator & Encoder Issues

### 1. Motor spins in the wrong direction
* **Description:** Commanding a forward movement causes one or more wheels to spin backwards.
* **Resolution:** Swap the physical motor lead pins (M+ and M-) in the connector, or invert the motor direction coefficient in your software driver file.

### 2. Encoder count reversed
* **Description:** The motor spins forward, but the encoder returns a decreasing/negative value.
* **Resolution:** Swap the Encoder A and Encoder B signal wires on the connector, or invert the multiplier constant in the driver configuration.

### 3. Motor does not stop / Runaway
* **Description:** The motor continues to spin even after speed commands are stopped.
* **Causes:**
  * Closed-loop PID controller is experiencing positive feedback due to reversed encoder polarity.
  * No watchdog timeout is implemented in the STM32 firmware.
* **Resolution:**
  * Lift the wheels off the ground, check if the encoder count goes up when moving forward. If it goes down, it triggers positive feedback (speeding up to catch the target). Fix encoder polarity.
