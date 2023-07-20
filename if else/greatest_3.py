num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greatest")
else:
    if num2 > num3:
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")
