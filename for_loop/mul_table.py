num = int(input("enter the number:"))
print(f"multiplication table of {num}:")
mul = 0
for i in range(1, 11):
        mul = num * i
        print(f"{num} * {i} = {mul}")
        mul = 0
    
