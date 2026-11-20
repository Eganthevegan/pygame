SWITCHES = [
    "Living Room Light",
    "Fan",
    "Air Conditioner",
    "Door Lock",
    "Garden Light",
    "Security Camera",
]


def main():
    state = 37
    bits = f"{state:06b}"

    on_count = bits.count("1")
    off_count = bits.count("0")

    first_set = (state & -state).bit_length()

    print("=== SMART SWITCH BIT MONITOR ===")
    print(f"State: {state} | Binary: {bits}")
    print(f"Set Bits (ON): {on_count} | Zero Bits (OFF): {off_count}")
    print(f"First Set Bit Position: {first_set}")
    print("\n--- Masks & Switch States ---")

    for idx, name in enumerate(SWITCHES):
        mask = 1 << idx
        is_on = bool(state & mask)
        label = "ON" if is_on else "OFF"
        print(f"Bit {idx} | Mask {mask:2d} ({mask:06b}) | {name}: {label}")

    print("\n=== SUMMARY ===")
    print(f"Value: {state} ({bits}) | ON: {on_count} | OFF: {off_count} | First ON: {first_set}")


if __name__ == "__main__":
    main()