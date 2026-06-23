# Power and Safety Guide

This document defines the strict safety procedures and power limitations required to avoid damaging the Yahboom Robot Expansion Board V3.0 or the Raspberry Pi 5.

---

## ⚡ Essential Power Rules

> [!CAUTION]
> Failure to follow these guidelines can result in permanent hardware damage, smoke, or fire. A previous motor driver board has already been damaged on this project.

1. **Dedicated Power Input:**
   * Apply battery or external power **ONLY** to the marked battery input terminals.
   * Verify the polarity with a multimeter **BEFORE** switching on the power source or plugging in any battery.
2. **Accessory Ports are OUTPUTS Only:**
   * Treat all auxiliary 5V and 12V ports on the board strictly as **outputs** unless official manuals explicitly state otherwise.
   * **Do not backfeed power** into the board via these accessory ports.
3. **No Double-Powering the Raspberry Pi 5:**
   * Do not power the Raspberry Pi 5 through its USB-C port while it is also connected to the Yahboom Board's power delivery interface (SBC power headers).
   * Double-powering can destroy the Raspberry Pi 5's power delivery circuitry or create dangerous ground loops.
4. **Fusing:**
   * **Always** install an inline fuse on the positive lead of the 12V battery prior to connecting it to the expansion board.
   * **Start with a low fuse rating:** Use a **3A to 5A fuse** during initial bring-up and motor testing. Do not use a 15A fuse, as it will allow enough current to destroy components before blowing.
5. **Physical Labeling:**
   * Physically label all cables, batteries, and board ports before powering up the system.

---

## 🚀 Phased Safety Testing Protocol

To minimize risk, execute the board tests in these incremental phases:

* **Phase 1: No Motors Connected**
  * Power the board with the inline fuse installed and zero actuators plugged in.
  * Check for heat build-up, abnormal smells, smoke, or buzzer errors.
  * Measure and verify the 5V and 12V output ports using a multimeter.
* **Phase 2: Single Motor, Wheels Lifted**
  * Connect **only one motor** to its channel.
  * Ensure the robot chassis is physically lifted on blocks so the wheel turns freely.
  * Command a low-speed PWM for a very short duration (1-2 seconds).
  * Be ready to physically disconnect the power source immediately if the motor runs away or draws excessive current.
* **Phase 3: All Motors, Lifted**
  * Connect all motors, keeping the wheels off the ground.
  * Execute low-speed commands to check individual motor directions and encoder count alignment.
* **Phase 4: Ground Driving**
  * Perform initial ground tests on a smooth, open surface at low speeds.
  * Monitor the temperature of the motor driver chips after brief runs.

---

## ⚠️ Motor & Encoder Wiring Hazard

> [!WARNING]
> Quadrature encoder motors use 6-pin connections carrying both low-power signals (Encoder A/B, VCC, GND) and high-power motor lines (Motor +, Motor -).
> If these pins are misaligned or swapped, 12V motor power could be bridged directly into the STM32's 3.3V/5V logic pins, instantly destroying the microcontroller.
> **Never trust pre-assembled cables without verifying the pinout matches the table in [Wiring and Pinouts](file:///c:/Users/inouy\electronics-project-hub\driver-boards\Yahboom_Robot_Expansion_Board_V3.0/docs/wiring-and-pinouts.md).**

---

## 🏷️ Printable/Copyable Port Labels

Copy or print these labels to mark the board's connectors during bring-up:

```text
[ 12V BATTERY INPUT ]  <- Main board power supply (Red/Black screw terminals)
[ 5V OUT ONLY ]        <- Auxiliary 5V supply for external low-power sensors
[ 12V OUT ONLY ]       <- Auxiliary 12V supply for high-power devices (e.g., Lidar)
[ PI POWER OUT ]       <- SBC header to power Raspberry Pi 5
[ MOTOR OUT ]          <- High-current output to DC Motors
[ ENCODER ]            <- Quadrature encoder feedback signal pins
[ SERVO ]              <- PWM or Serial servo connector arrays
```
