seat_numbers = [101, 105, 112, 120, 130, 145, 150, 162, 175, 190]

target_seat = 130


def binary_search(seats, target):
    low = 0
    high = len(seats) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if seats[mid] == target:
            return mid, steps
        elif seats[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1, steps


def recursive_binary_search(seats, target, low, high, steps=1):
    if low > high:
        return -1, steps

    mid = (low + high) // 2

    if seats[mid] == target:
        return mid, steps
    elif seats[mid] > target:
        return recursive_binary_search(seats, target, low, mid - 1, steps + 1)
    else:
        return recursive_binary_search(seats, target, mid + 1, high, steps + 1)


def main():
    print("--- MY TRAIN SEAT FINDER ---")
    print(f"Seat List: {seat_numbers}")
    print(f"Target Seat: {target_seat}\n")

    # Testing Iterative Search
    index, steps = binary_search(seat_numbers, target_seat)
    print(f"Iterative Binary Search: Found seat {target_seat} at index {index} in {steps} step(s).")
    
    print("\n[Space & Time Complexity - Iterative]")
    print("• Time Complexity: O(log n) because the search space is cut in half each step.")
    print("• Space Complexity: O(1) auxiliary space because it uses a fixed set of variables (low, high, mid).\n")

    rec_index, rec_steps = recursive_binary_search(seat_numbers, target_seat, 0, len(seat_numbers) - 1)
    print(f"Recursive Binary Search: Found seat {target_seat} at index {rec_index} in {rec_steps} step(s).")

    print("\n[Space & Time Complexity - Recursive]")
    print("• Time Complexity: O(log n) as each function call halves the remaining data.")
    print("• Space Complexity: O(log n) due to call stack usage, since each recursive call adds a frame to memory.\n")

    print("=" * 45)
    print("COMPLEXITY LADDER (Fastest to Slowest)")
    print("=" * 45)
    print("1. O(1)      - Constant: Direct lookups (e.g., list indexing by position)")
    print("2. O(log n)  - Logarithmic: Binary search (halving the problem size)")
    print("3. O(n)      - Linear: Linear search (checking seats one by one)")
    print("4. O(n²)     - Quadratic: Nested loops (e.g., checking all seat pairs)")
    print("=" * 45)

if __name__ == "__main__":
    main()