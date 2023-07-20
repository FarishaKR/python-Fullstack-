num = int(input("enter the limit:"))
print(f"sum of numbers up to {num}:")
sum = 0
for i in range(num+1):
    sum += i
print(sum)
