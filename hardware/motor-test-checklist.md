# Motor Test Checklist

This checklist must be reviewed and checked off before **every** test involving active motor control.

---

## 📋 Pre-Test Checklist

- [ ] **Battery Voltage Checked:** Ensure the battery voltage is within the safe operational range of the board (typically 9.6V - 12.6V for a 3S LiPo). Do not overcharge or use excessive voltage.
- [ ] **Inline Fuse Installed:** A 3A to 5A inline fuse is wired in series with the positive battery terminal.
- [ ] **Polarity Checked:** The positive (red) and negative (black) battery lines are correctly connected to the board terminals. Verified with a multimeter.
- [ ] **Motor Plug Pinout Verified:** Motor and encoder wires have been validated using the multimeter checklist in the [Wiring and Pinouts Guide](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/docs/wiring-and-pinouts.md).
- [ ] **Pi Powered from One Source Only:** The Raspberry Pi 5 is powered via either its USB-C port OR the Yahboom board interface, **NEVER** both simultaneously.
- [ ] **Chassis Lifted (Wheels Off Ground):** The robot chassis is securely supported on blocks or a stand so that all driving wheels can rotate freely without contact with the floor/bench.
- [ ] **Speed Limits Active:** The software command speeds are restricted to low values (e.g., < 15% maximum PWM or low RPM limits) for initial runs.
- [ ] **Test Duration Restricted:** Initial commands should run the motors for no more than 1 to 2 seconds to verify control.
- [ ] **Emergency Stop Ready:** Your hand is physically positioned on the power switch or the battery connector plug, ready to cut power immediately if abnormal behavior occurs.
- [ ] **Post-Test Thermal Audit:** After the test run, power down the system and touch the motor driver chips on the board to check for localized heat build-up.
