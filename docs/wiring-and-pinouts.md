# Wiring and Pinouts Guide

This document describes how to verify motor and encoder wiring before applying power to the Yahboom Robot Expansion Board V3.0.

---

## 🔍 Pre-Power Wiring Verification Note

> [!IMPORTANT]
> **EVERY motor/encoder connector must be verified manually before power-on.**
> Do not trust that the colors of wire assemblies match standard conventions or that the pre-installed connector headers are correctly aligned.

---

## 🎛️ Motor / Encoder Pinout Reference Table

Standard quadrature encoder motor cables usually use a 6-pin JST interface. The connection details are mapped below:

| Pin Name | Pin Description | Function | Target Board Connection |
| :--- | :--- | :--- | :--- |
| **Motor +** (M+) | Motor Power Positive | Drives the DC Motor (PWM-controlled) | Motor Controller Output |
| **Motor -** (M-) | Motor Power Negative | Drives the DC Motor (PWM-controlled) | Motor Controller Output |
| **Encoder VCC** | Encoder Sensor Power | Powers the Hall effect sensors (usually 3.3V or 5V) | MCU Logic VCC (3.3V/5V) |
| **Encoder GND** | Encoder Ground | Common ground reference for sensors | MCU Logic GND |
| **Encoder A** (CLK) | Channel A output | Phase A square wave signal | STM32 Timer Input (PA/PB/PC) |
| **Encoder B** (DT) | Channel B output | Phase B square wave signal | STM32 Timer Input (PA/PB/PC) |

---

## ⚡ Multimeter Wire Identification Checklist

Before plugging a new motor into the board, follow this step-by-step procedure to identify and confirm the wires:

1. **[ ] Disconnect all power:** Ensure the battery is completely disconnected from the board and motors are unplugged.
2. **[ ] Identify Motor Windings (Motor + and Motor -):**
   * Put the multimeter in resistance (Ohms) mode.
   * Measure pairs of pins on the motor's connector.
   * The two motor coil pins (Motor + and Motor -) will show a low resistance (typically $2\,\Omega$ to $30\,\Omega$ depending on the motor).
   * All other pin combinations (connected to the encoder) should register as open circuit or extremely high resistance.
3. **[ ] Identify Encoder Ground (GND):**
   * Keep the motor unplugged.
   * Switch the multimeter to continuity/diode mode or resistance mode.
   * Check the resistance between the encoder pins and the motor's metallic casing or the ground pins of the encoder chip if visible.
   * On the expansion board side, locate the ground pins on the 6-pin connector by checking continuity against the board's main negative power input terminal.
4. **[ ] Identify Encoder VCC:**
   * On the expansion board side, identify the logic supply pin (typically 3.3V or 5V) on the 6-pin connector.
   * Measure continuity from that pin to the STM32 VCC rail or 3.3V/5V onboard regulators.
   * On the motor side, identify VCC by locating the pin that links to the supply pad of the Hall sensor IC.
5. **[ ] Identify Encoder A & B Signals:**
   * These lines are typically pulled high on the board.
   * Verify they connect to STM32 input pins and show high resistance to GND and VCC.
