# Power Port Labeling & Rail Diagnostics

Before powering the board with high-current batteries, verify the voltage rails and write physical labels near each port.

---

## ⚡ Power Port Map (VERIFY)

Ensure the following terminals read the expected values under no-load conditions:

| Port Identifier | Silk Screen Label | Expected Voltage | Current Limit (Est) | Purpose | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BAT_IN** | `BAT` / `Vin` / `12V` | 9.6V - 12.6V | 10A Max (Fuse) | Main input from battery pack | `VERIFY` |
| **5V_OUT** | `5V` | 5.0V ± 0.2V | `VERIFY` (e.g., 3A) | Logic sensors / external modules | `VERIFY` |
| **12V_OUT**| `12V` | Equal to `BAT_IN` | `VERIFY` (e.g., 2A) | High-voltage accessories (Lidar) | `VERIFY` |
| **PI_PWR** | `5V` (GPIO headers) | 5.1V ± 0.1V | `VERIFY` (e.g., 3A-5A) | Power feed to Raspberry Pi 5 | `VERIFY` |

---

## 🔍 Visual Checks

1. **Short Circuit Check:** Before inserting a battery, measure resistance between `BAT_IN (+)` and `BAT_IN (-)` using a multimeter. Ensure it is not shorted ($>100\,\text{k}\Omega$).
2. **Capacitor Inspection:** Check for bloated, damaged, or reverse-soldered electrolytic capacitors on the primary power input lines.
3. **Trace Check:** Ensure no solder bridges exist across the power switch contacts or screw terminals.
