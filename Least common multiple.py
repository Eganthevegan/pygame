num1 = int(input("Enter Largest number : "))
num2 = int(input("Enter Smallest number : "))

maximum = max(num1, num2)
lcm = maximum

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += 1

print(f"LCM is : {lcm}")