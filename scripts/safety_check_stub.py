#!/usr/bin/env python3
import sys

def main():
    print("=" * 60)
    print(" ⚠️  YAHBOOM ROBOT BOARD BRING-UP: INTERACTIVE SAFETY CHECKLIST  ⚠️")
    print("=" * 60)
    print("Before starting hardware testing, you must manually confirm the following:")
    print("Refer to: docs/power-and-safety.md for details.")
    print("-" * 60)

    checklist = [
        ("FUSE", "Is a 3A to 5A inline fuse installed on the 12V battery positive lead?"),
        ("LIFT", "Are the robot wheels lifted completely off the ground/bench?"),
        ("POWER", "Is the battery input polarity verified and plugged into the correct terminal?"),
        ("PINOUT", "Has the motor & encoder pinout been validated with a multimeter?"),
        ("EMERGENCY", "Is an emergency disconnect/switch in arm's reach?"),
        ("HOST POWER", "Is the Raspberry Pi 5 powered from a single source only (not double-powered)?")
    ]

    for key, question in checklist:
        while True:
            response = input(f"[{key}] {question} (y/n): ").strip().lower()
            if response == 'y':
                break
            elif response == 'n':
                print("\n⛔ SAFETY AUDIT FAILED: Do not proceed. Fix this issue before testing.")
                sys.exit(1)
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    print("-" * 60)
    print("✅ Safety checks complete!")
    print("Ready for manual test only — no motor control implemented in this script yet.")
    print("=" * 60)

if __name__ == "__main__":
    main()
