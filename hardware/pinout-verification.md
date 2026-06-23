# Pinout Verification Records

This document is a scratchpad to verify physical pin mappings on the Yahboom Robot Expansion Board V3.0.

> [!WARNING]
> Do not assume these mappings are correct. All entries must be verified using a multimeter or by inspecting the board's schematics and tracing board traces to the STM32F103RCT6 microcontroller.

---

## 🏎️ Motor and Encoder Mappings (VERIFY)

| Channel | Signal | Pin Color (Expected) | STM32 Pin (Target) | Status | Date Verified |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1** | Motor + | Red | `VERIFY` | UNKNOWN | |
| **M1** | Motor - | Black | `VERIFY` | UNKNOWN | |
| **M1** | Encoder VCC | Brown | `5V` or `3.3V` | UNKNOWN | |
| **M1** | Encoder GND | Blue | `GND` | UNKNOWN | |
| **M1** | Encoder A | Yellow | `VERIFY` | UNKNOWN | |
| **M1** | Encoder B | White | `VERIFY` | UNKNOWN | |
| **M2** | Motor + | - | `VERIFY` | UNKNOWN | |
| **M2** | Motor - | - | `VERIFY` | UNKNOWN | |
| **M2** | Encoder A | - | `VERIFY` | UNKNOWN | |
| **M2** | Encoder B | - | `VERIFY` | UNKNOWN | |
| **M3** | Motor + | - | `VERIFY` | UNKNOWN | |
| **M3** | Motor - | - | `VERIFY` | UNKNOWN | |
| **M3** | Encoder A | - | `VERIFY` | UNKNOWN | |
| **M3** | Encoder B | - | `VERIFY` | UNKNOWN | |
| **M4** | Motor + | - | `VERIFY` | UNKNOWN | |
| **M4** | Motor - | - | `VERIFY` | UNKNOWN | |
| **M4** | Encoder A | - | `VERIFY` | UNKNOWN | |
| **M4** | Encoder B | - | `VERIFY` | UNKNOWN | |

---

## 📟 Onboard Sensors (VERIFY)

* **IMU SCL Pin:** `VERIFY` (Typically STM32 I2C Pin PB6 or PB8)
* **IMU SDA Pin:** `VERIFY` (Typically STM32 I2C Pin PB7 or PB9)
* **IMU INT Pin:** `VERIFY`
* **Battery Telemetry ADC Pin:** `VERIFY`
