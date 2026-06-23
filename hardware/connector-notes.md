# Connector Specifications

This document catalogs connector pitches, shell styles, and wiring harnesses used on the Yahboom Robot Expansion Board V3.0.

---

## 🔌 Connector Specifications Table (VERIFY)

| Connector Purpose | Connection Type | Pitch (Spacing) | Common Part Name | Pin Count | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Motor & Encoder Channels** | JST-PH or JST-XH | `VERIFY` (e.g., 2.0mm PH) | JST-PH-6P | 6 | `VERIFY` |
| **PWM Servos** | Dupont Header | 2.54mm (0.1") | Male Pin Header | 3 | Confirmed |
| **Serial Bus Servos** | JST-PH | `VERIFY` (e.g., 2.0mm PH) | JST-PH-3P | 3 | `VERIFY` |
| **Main Battery Input** | Screw Terminal | `VERIFY` (e.g., 5.08mm) | KF301-2P | 2 | Confirmed |
| **USB Host Communication**| USB port type | N/A | Micro-USB / USB-C | N/A | `VERIFY` |
| **CAN Bus** | Terminal Block / JST | `VERIFY` | `VERIFY` | 2/4 | `VERIFY` |

---

## 🔍 Wire Assembly Verification Checklist
* Check the housing pin retention tab: ensure no crimped pins are slipping back out of the housing shell.
* Verify wire diameter (AWG): ensure motor power carrying wires (M+/M-) are thick enough (typically 22-24 AWG) to carry currents up to 3A without heating.
