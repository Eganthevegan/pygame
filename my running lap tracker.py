# ================================
# RUNNING LAP TRACKER PROGRAM
# ================================
# Topics Covered:
# - Algorithms & Pseudocode
# - Time & Space Complexity
# - Comparing 3 Solutions to One Problem

# Problem Overview:
# A runner earns points on each lap completed:
# Lap 1 = 1 pt, Lap 2 = 2 pts, Lap 3 = 3 pts, ... up to Lap n.
# Objective: Calculate total points earned after n laps using 3 approaches.

laps = 5

print("================================")
print("  RUNNING LAP TRACKER PROGRAM   ")
print("================================")
print("Total Laps:", laps)
print()


# ------------------------------------------------
# APPROACH 1 - FORMULA SOLUTION
# ------------------------------------------------
# Algorithm Idea:
# Compute total points directly using the math formula n * (n + 1) / 2.
#
# Pseudocode:
# START
#    SET total = laps * (laps + 1) / 2
#    PRINT total
# END
#
# Time Complexity: O(1)
# Space Complexity: O(1)

total_formula = laps * (laps + 1) // 2

print("Approach 1: Formula Solution")
print("Total Points:", total_formula)
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")
print()


# ------------------------------------------------
# APPROACH 2 - SINGLE LOOP SOLUTION
# ------------------------------------------------
# Algorithm Idea:
# Initialize total to 0, then add each lap number iteratively.
#
# Pseudocode:
# START
#    SET total = 0
#    FOR current_lap FROM 1 TO laps DO
#        total = total + current_lap
#    PRINT total
# END
#
# Time Complexity: O(n)
# Space Complexity: O(1)

total_loop = 0
loop_counter = 0

for current_lap in range(1, laps + 1):
    total_loop += current_lap
    loop_counter += 1

print("Approach 2: Single Loop Solution")
print("Total Points:", total_loop)
print("Step Count:", loop_counter)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print()


# ------------------------------------------------
# APPROACH 3 - NESTED LOOP SOLUTION
# ------------------------------------------------
# Algorithm Idea:
# For every lap, add 1 point one at a time using an inner loop.
#
# Pseudocode:
# START
#    SET total = 0
#    FOR current_lap FROM 1 TO laps DO
#        FOR pt FROM 1 TO current_lap DO
#            total = total + 1
#    PRINT total
# END
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

total_nested = 0
nested_counter = 0

for current_lap in range(1, laps + 1):
    for pt in range(1, current_lap + 1):
        total_nested += 1
        nested_counter += 1

print("Approach 3: Nested Loop Solution")
print("Total Points:", total_nested)
print("Step Count:", nested_counter)
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
print()


# ------------------------------------------------
# EFFICIENCY ANALYSIS & SUMMARY
# ------------------------------------------------

print("================================")
print("  EVALUATING ALGORITHM EFFICIENCY")
print("================================")
print("1. Formula Solution: Fastest — executes in 1 constant math operation.")
print("2. Single Loop Solution: Moderate — scales linearly with lap count.")
print("3. Nested Loop Solution: Slowest — execution grows quadratically.")
print()
print("Space Complexity Note:")
print("All approaches run in O(1) space as memory usage stays constant.")
print()
print("Optimal Solution: Formula Solution")
print("Reason: O(1) time complexity guarantees maximum performance regardless of n.")
print("================================")