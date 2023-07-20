num = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))

if num > num2 and num > num3:
    print(f"{num} is greatest")
else:
    if num2 > num3:
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")
