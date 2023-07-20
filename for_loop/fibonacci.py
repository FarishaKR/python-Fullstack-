num = int(input("enter the limit:"))
print(f"finonacci series:")
a = 0
b = 1
print(a)
print(b)
for i in range(2,num):
    c = a+b
    print(c)
    a = b
    b = c
