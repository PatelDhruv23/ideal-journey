list=[]
n= int(input("ENTER THE NUMBER OF ELEMENTS:"))

for i in range (0,n):
    a=int(input("ENTER THE ELEMENT VALUE:"))
    list.append(a)


for i in range (0,len(list)):

    for i in range (0,len(list)-1): 

        if(list[i]>list[i+1]):
           list[i],list[i+1] = list[i+1],list[i]

print(list)

for i in range (0,len(list)):

    for i in range (0,len(list)-1): 

        if(list[i]<list[i+1]):
           list[i],list[i+1] = list[i+1],list[i]

print(list)


