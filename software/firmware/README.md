# STM32 Firmware & Examples (`software/firmware/`)

This folder contains the firmware binary and source code projects for the Yahboom Robot Expansion Board V3.0 (onboard STM32F103RCT6 MCU).

## Folder Contents

* **`rosmaster_V3.5.1.hex`**: The precompiled factory firmware hex binary. If you ever need to restore the board to its factory settings, you can flash this binary directly.
* **[STM32_Firmware/](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/software/firmware/STM32_Firmware/)**: The complete factory firmware source code (V3.5.1). This is a **Keil uVision** project (`rosmaster.uvprojx`). It includes:
  * FreeRTOS real-time operating system scheduler.
  * Closed-loop PID motor velocity control.
  * IMU reader and registry map telemetry interface.
  * Servo command drivers (PWM and serial bus).
* **[STM32CubeIDE_Examples/](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/software/firmware/STM32CubeIDE_Examples/)**: Modular tutorial projects in **STM32CubeIDE** format (`.ioc`, `.project`) for validating individual board components:
  * `Motor/` and `Encoder/` - Actuator checks.
  * `Read_IMU/` - Accelerometer, gyro, and magnetometer registry polling.
  * `PwmServo/` and `Serial_Servo/` - Servo actuation.
  * `Serial/` - Host communication link.
  * `CAN/` - Controller area network communication.
  * `SBUS/` - Remote control receiver parsing.
  * `LED/` and `RGB_Strip/` - LED and light indicators.

---

## ⚡ Flashing the Firmware

### Method 1: Using the USB Serial Port (ISP)
The STM32F103RCT6 chip on this board supports an ISP (In-System Programming) bootloader over its serial pins.

1. **Prerequisites:**
   * Install the **CH340 driver** on your host PC.
   * Download a flashing utility like **FlyMCU** or **mcuisp** (available in the official downloads).
2. **Step-by-step Flashing:**
   * Connect the board's USB serial port (Micro-USB or USB-C) to your computer.
   * Open FlyMCU/mcuisp.
   * Load the [rosmaster_V3.5.1.hex](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/software/firmware/rosmaster_V3.5.1.hex) file.
   * Select the correct COM port (associated with CH340).
   * **Bootloader Mode Switch:** On the board, hold down the **BOOT0** button, press and release the **RESET** button, then release **BOOT0**.
   * In FlyMCU/mcuisp, select: `DTR low reset, RTS high enters BootLoader`.
   * Click **Start ISP** to begin programming.
   * Once complete, press the **RESET** button on the board to boot into the newly flashed firmware.

### Method 2: Using an ST-Link Debugger (SWD)
For active development and debugging:
* Connect the **SWD pins** (GND, SWCLK, SWDIO, 3.3V) on the board to an ST-Link v2 or v3 debugger.
* Open the project in Keil uVision or STM32CubeIDE and flash/debug directly.
