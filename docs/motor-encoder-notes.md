# DC Motor and Encoder Calibration Notes

This document provides details on configuring, calibrating, and logging motor and encoder feedback parameters.

---

## ⚙️ Channels and Physical Connections

The Yahboom Robot Expansion Board V3.0 supports **4 independent encoder DC motor channels**:
* **M1:** Left-Front Motor (standard 4WD configuration)
* **M2:** Left-Rear Motor
* **M3:** Right-Front Motor
* **M4:** Right-Rear Motor

> [!WARNING]
> Do not assume a 6-pin encoder plug is wired correctly just because it fits into the header socket. Always double-check wire alignments.

---

## 🔄 Direction and Encoder Polarities

For proper closed-loop control (PID speed control and odometry calculations), motor drive direction and encoder pulse directions must match:

1. **Forward Command Check:**
   * Sending a positive speed command to a motor channel should cause the corresponding wheel to rotate in the physical forward direction.
2. **Encoder Sign Correlation:**
   * A forward rotation **must** produce a positive-increasing encoder step count.
3. **Corrective Actions:**
   * If a motor spins backwards but the encoder counts positively: Invert the motor leads (swap Motor + and Motor -) or invert the PWM signal in software.
   * If the motor spins forwards but the encoder counts negatively: Swap the Encoder A and Encoder B signals on the connector, or invert the encoder logic scale factor in the software/driver configuration.

---

## 📊 Motor Specifications Log (VERIFY)

Fill out this log for the chosen motor hardware before conducting high-speed or heavy-load testing.

| Parameter | Specifications / Value | Notes |
| :--- | :--- | :--- |
| **Rated Voltage** | `VERIFY` (e.g., 12V DC) | |
| **No-load Current** | `VERIFY` (e.g., 120mA) | Motor current with wheels off the ground |
| **Loaded Current** | `VERIFY` (e.g., 800mA) | Average current during normal ground driving |
| **Stall Current** | `VERIFY` (e.g., 3.2A) | Current drawn when motor shaft is locked (high risk!) |
| **Gear Reduction Ratio** | `VERIFY` (e.g., 1:30 or 1:45) | Mechanical gearbox ratio |
| **Encoder PPR (Pulses Per Rev)** | `VERIFY` (e.g., 11 PPR) | Pulses per rotation of the motor armature |
| **Encoder CPR (Counts Per Rev)** | `VERIFY` (e.g., 44 CPR) | Total quadrature transitions per rotation ($PPR \times 4$) |
| **Wheel Diameter** | `VERIFY` (e.g., 65mm or 80mm) | Required for odometry calculations |
