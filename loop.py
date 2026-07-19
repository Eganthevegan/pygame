n = 5
total = n * (n + 1) // 2
#step 1

# loop run n times
for round_num in range(1, n + 1):
    total += round_num

# nested loop way
for round_num in range(1, n + 1):
    # outer loop

    # inner loop
    for point in range(1, round_num + 1):
        total += 1

print(total)