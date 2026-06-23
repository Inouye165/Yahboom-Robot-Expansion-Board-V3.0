# Python Rosmaster Library (`software/python-rosmaster/`)

This directory is designated for the core Python communication driver used to interface with the Yahboom STM32 board over serial.

## Expected Contents

* **`RosmasterV3.py` (Future addition):** The main communication class provided by Yahboom or custom-written. It handles building command frames (pack bytes) and unpacking incoming data frames (battery voltage, encoders, IMU registers).
* **`serial_test.py` (Future addition):** A simple script to verify connection parameters (baud rate, device port) and print telemetry outputs.
