number = input("Enter a number: ")
power = len(number)
total = 0

for digit in number:
    total += int(digit) ** power

if total == int(number):
    print("Yes, it is an Armstrong number!")
else:
    print("No, it is not.")