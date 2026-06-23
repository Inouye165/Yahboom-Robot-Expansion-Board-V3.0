# Screenshots Directory (`external-info/screenshots/`)

This directory is intended for manually captured screenshots of schematics, port layouts, manufacturer specifications, or web research.

## Naming Suggestions

To keep the repository clean and navigable, please name your screenshot images using the following conventions:

* **Board Layouts / Pin Diagrams:**
  * Format: `board_pinout_<view>.png` (e.g., `board_pinout_top.png`, `board_pinout_m1_m4_detail.png`)
* **Wiring Schematics:**
  * Format: `wiring_<component>_to_<component>.png` (e.g., `wiring_motor1_to_driver.png`, `wiring_pi5_to_stm32_serial.png`)
* **Official Specs / Manual Snaps:**
  * Format: `ref_<topic>_specification.png` (e.g., `ref_imu_register_map.png`, `ref_tb6612_current_ratings.png`)
* **Test Logs / GUI Graphs:**
  * Format: `test_log_<topic>_chart.png` (e.g., `test_log_motor_response_pid.png`)

---

*Note: Avoid committing large uncompressed BMP or TIFF files. Standard compressed PNG or WebP images are preferred. If files exceed 10MB, do not track them directly; consider Git LFS.*
