f = open("demo.txt","r")
max1 = 0
max_word =" "
list1 =[]

for line in f:
    for word in line.split():
        print(word)
        if(max1 <= len(word)):
            max1 = len(word)
            max_word = word
            list1.append(word)
            
print(f"longest words in file is: {list1}")
