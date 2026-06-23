# Yahboom Robot Expansion Board V3.0 Project Hub

This repository serves as the central reference workspace and development environment for the **Yahboom Robot Expansion Board V3.0** robot project. It contains setup notes, hardware specifications, safety checklists, wiring diagrams, copied research, test logs, ROS2 architecture plans, and software drivers.

---

## ⚠️ CRITICAL SAFETY WARNING

> [!CAUTION]
> **DO NOT POWER MOTORS UNTIL SAFETY CHECKLIST IS COMPLETE!**
> A motor driver board was previously damaged/smoked in this project. Do not assume motor wiring, encoder pinouts, or power ports are correct without manual verification using a multimeter.
> See the [Power and Safety Guide](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/power-and-safety.md) and the [Motor Test Checklist](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/hardware/motor-test-checklist.md) before connecting any batteries or motors.

---

## 🤖 System Architecture

This project is built for a 4-motor rover/tank/differential-style robot platform using a split-processing architecture:

```mermaid
graph TD
    SubHost[Raspberry Pi 5 Host] <-->|USB Serial | SubMCU[Yahboom STM32 Board]
    
    subgraph "Raspberry Pi 5 (High-Level Controller)"
        ROS2[ROS2 Jazzy / Iron / Humble]
        Nav2[Nav2 Navigation]
        SLAM[SLAM Mapping]
        Cam[Camera Feed]
        Lidar[Lidar Scanning]
        Web[Web Control / High-Level Logic]
    end

    subgraph "Yahboom STM32F103RCT6 (Low-Level Controller)"
        Motors[4x Encoder DC Motors]
        IMU[9-Axis IMU (ICM20948/MPU9250)]
        Servos[PWM Servos & Serial Bus Servos]
        Telemetry[Battery & Motor Telemetry]
        SBUS[SBUS Remote Control]
    end
```

### Main Components
* **Host Computer:** Raspberry Pi 5 running ROS2, camera, lidar, SLAM, Nav2, Wi-Fi, web control, and high-level robot logic.
* **Low-Level Controller:** Yahboom Robot Expansion Board V3.0 with an onboard **STM32F103RCT6** MCU. It handles motor control, encoder reading, IMU data acquisition, servos, battery/motor telemetry, and low-level real-time timing.
* **Communication Interface:** USB Serial (CH340 chipset) bound to a stable device name via udev rule: `/dev/ttyUSB_ROSBOARD`.

---

## 📂 Project Structure

* [docs/](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/README.md) - Cleaned-up, summarized project documentation and plans.
* [hardware/](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/hardware/README.md) - Wiring, pinout, connector, and safety verification notes.
* [software/](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/software/README.md) - Source code, drivers, ROS2 packages, and udev rules.
* [logs/](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/logs/README.md) - Test logs, serial output captures, and issue tracking.
* [external-info/](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/external-info/README.md) - Copied reference notes, listing info, official datasheets, and screenshots.
* [scripts/](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/scripts/README.md) - Utility scripts, safety check stubs, and helpers.

---

## 🚦 Project Setup Status Checkboxes

* [ ] **Phase 0: Documentation & Safety Verification**
  * [ ] Port labeling complete
  * [ ] Multimeter verification of motor/encoder pinouts
  * [ ] Safety checklist verified
* [ ] **Phase 1: Board-Only Power Test**
  * [ ] Fuse installed (3A to 5A)
  * [ ] Board powered on (no motors, no Pi)
  * [ ] 5V and 12V outputs measured and verified
* [ ] **Phase 2: Raspberry Pi Communication**
  * [ ] USB connection established
  * [ ] udev rule configured (`/dev/ttyUSB_ROSBOARD`)
  * [ ] Board communication verified via serial test
* [ ] **Phase 3: Single Motor Lifted Test**
  * [ ] Motor direction matches PWM command
  * [ ] Encoder count direction matches rotation
* [ ] **Phase 4: Four Motor Lifted Test**
  * [ ] Complete mechanical/electrical lift setup
  * [ ] All 4 channels tested and direction verified
* [ ] **Phase 5: Ground Driving Test**
  * [ ] Low-speed drive tests
  * [ ] Current draw and thermal monitoring
* [ ] **Phase 6: ROS2 Integration**
  * [ ] `/cmd_vel` motor control
  * [ ] `/imu/data_raw` and `/odom` publishing
  * [ ] Navigation and SLAM mapping

---

## 🔗 Quick Access Links

* **Overview:** [docs/board-overview.md](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/board-overview.md)
* **Safety Rules:** [docs/power-and-safety.md](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/power-and-safety.md)
* **Wiring Table:** [docs/wiring-and-pinouts.md](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/wiring-and-pinouts.md)
* **Setup Plan:** [docs/setup-plan.md](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/setup-plan.md)
* **Official Sources:** [docs/source-links.md](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/source-links.md)
