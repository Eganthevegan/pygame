total = int(input("Total days: "))
absent = int(input("Days absent: "))

attended = total - absent
percent = (attended / total) * 100

print("Attendance percentage:", percent)

if percent >= 75:
    print("You can take the exam.")
else:
    print("You cannot take the exam.")