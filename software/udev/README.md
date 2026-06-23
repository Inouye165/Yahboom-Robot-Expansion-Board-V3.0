# USB Serial Device Binding (udev)

To prevent the serial device path from changing names (e.g., from `/dev/ttyUSB0` to `/dev/ttyUSB1`) between reboots or hot-plugs, a udev rule must be used to bind the device's Vendor ID (ID Vendor) and Product ID (ID Product) to a static symbolic link (`/dev/ttyUSB_ROSBOARD`).

## Files

* **[99-yahboom-ros-board.rules.example](file:///c:/Users/inouy/electronics-project-hub/driver-boards/Yahboom_Robot_Expansion_Board_V3.0/software/udev/99-yahboom-ros-board.rules.example):** Example rule targeting the CH340 serial chip.

---

## 🛠️ How to Install and Activate

1. **Verify Vendor and Product IDs:**
   * Plug in the board's USB cable into the Raspberry Pi 5.
   * Run `lsusb` and locate the line for the CH340 device.
   * Format: `Bus XXX Device YYY: ID <idVendor>:<idProduct> CH340 ...`
   * To verify details via udevadm, run:
     ```bash
     udevadm info -a -n /dev/ttyUSB0
     ```
2. **Copy the rules file to system path:**
   * Copy the configuration file to `/etc/udev/rules.d/`:
     ```bash
     sudo cp 99-yahboom-ros-board.rules.example /etc/udev/rules.d/99-yahboom-ros-board.rules
     ```
3. **Reload udev daemon:**
   * Trigger the system to re-read rules and apply:
     ```bash
     sudo udevadm control --reload-rules
     sudo udevadm trigger
     ```
4. **Verify the Symlink:**
   * Run:
     ```bash
     ls -l /dev/ttyUSB_ROSBOARD
     ```
   * It should print a pointer link like `/dev/ttyUSB_ROSBOARD -> ttyUSB0`.
