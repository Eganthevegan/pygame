# ================================
# MY QUIZ RESULT SEARCHER
# ================================
# Topics covered:
# Big-O, Omega, and Theta notation
# Analyzing O(1), O(n), and O(n^2) performance

# List storing student quiz scores
quiz_scores = [92, 84, 71, 65, 50, 99, 43, 88, 77, 95]

print("================================")
print("MY QUIZ RESULT SEARCHER")
print("================================")
print("Quiz Scores:", quiz_scores)


# --------------------------------
# PART 1 - O(1): Direct Access
# --------------------------------
# Retrieves the very first element directly by index.
# Runs in constant time regardless of how large the list grows.

first_score = quiz_scores[0]

print("\nPART 1: Direct Access")
print("First Student Score:", first_score)
print("Time Complexity: O(1)")
print("Theta Notation: Theta(1)")
print("Reason: Direct access takes one step.")


# --------------------------------
# PART 2 - O(n): Linear Search
# --------------------------------
# Scans through scores sequentially to locate a target value.
# Best Case: Target is at index 0.
# Average Case: Target is somewhere around the middle.
# Worst Case: Target is at the very end or missing entirely.

target_score = 95
steps = 0
found = False

print("\nPART 2: Linear Search")
print("Searching for score:", target_score)

for score in quiz_scores:
    steps = steps + 1

    if score == target_score:
        found = True
        print("Score found:", score)
        print("Steps Taken:", steps)
        break

if not found:
    print("Score not found.")
    print("Steps Taken:", steps)

print("Best Case: Omega(1)")
print("Average Case: Theta(n)")
print("Worst Case: Big-O(n)")
print("Reason: The program may need to check many scores.")


# --------------------------------
# PART 3 - O(n^2): Pair Comparison
# --------------------------------
# Evaluates every possible pair of scores using a nested loop.
# Total operations scale quadratically with the input size.

print("\nPART 3: Pair Comparison")
pair_steps = 0

for score1 in quiz_scores:
    for score2 in quiz_scores:
        pair_steps = pair_steps + 1

print("Total Pair Checks:", pair_steps)
print("Time Complexity: O(n^2)")
print("Reason: A nested loop compares every score with every other score.")


# --------------------------------
# PART 4 - Best, Average, Worst Case Demo
# --------------------------------

print("\nPART 4: Case Comparison")

best_case_score = 92
average_case_score = 50
worst_case_score = 95

print("Best Case Target:", best_case_score, "- Found near the beginning")
print("Average Case Target:", average_case_score, "- Found around the middle")
print("Worst Case Target:", worst_case_score, "- Found near the end")


# --------------------------------
# Final summary
# --------------------------------

print("\n================================")
print("ASYMPTOTIC ANALYSIS SUMMARY")
print("================================")
print("O(1): Direct access is fastest.")
print("O(n): Linear search grows with the number of scores.")
print("O(n^2): Nested loops grow much faster.")
print("Omega(1): Best case for search when the target is found first.")
print("Theta(1): Direct access always takes constant time.")
print("Big-O shows the upper/worst-case growth.")
print("================================")