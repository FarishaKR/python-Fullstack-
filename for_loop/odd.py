limit = int(input("enter the limit:"))
print(f"odd number up to the limit{limit}:")
for i in range(1, limit+1):
     if i % 2 != 0:
         print(i)
    
