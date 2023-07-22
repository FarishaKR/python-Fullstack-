f = open("demo.txt","r")
max1 = 0
count = 0
max_word =" "
org_list =[]
rep_li =[]
notrep_li=[]

#to get the words from file
for line in f:
    for word in line.split():
        org_list.append(word)
print(org_list)  

#to get the list of repeated words(rep_li)
for i in range(len(org_list)):
    for j in range(i+1,len(org_list)):
         if org_list[i]==org_list[j]:
             if  org_list[i] not in rep_li:
                rep_li.append(org_list[i])
print(rep_li)

#to get the count of repeated words:
for a in rep_li:
    for b in org_list:
        if a==b:
            count+=1
    print(a, "count", count)
    count= 0
