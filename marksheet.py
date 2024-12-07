list=[]
n= int(input("ENTER THE NUMBER OF SUBJECTS:"))

j=1
for i in range (0,n):
    print("ENTER MARKS OF SUBJECT ",j," :" )
    a=int(input())
    list.append(a)
    j=j+1

print("MARKS:",list)

sum=0
for i in range (0,n):
    sum = sum + list[i]

avg = float(sum / n)

print("AVERAGE:",avg)

if(avg<33 and avg>=0):
    print("FAIL AND GRADE F")

elif(avg>=33 and avg<60):
    print("PASS AND GRADE C")

elif(avg>=60 and avg<80):
    print("PASS AND GRADE B")

elif(avg>=80 and avg<90):
    print("PASS AND GRADE A")

elif(avg >=90 and avg<=100):
    print("PASS AND GRADE A+")

else:
    print("INVALID MARKS INPUT")
   