m1={}
n=int(input("ENTER NUMBER OF ELEMENT: "))

for i in range(0,n):
    a,b = input("ENTER THE KEY VALUE PAIR DATA:").split()
    m1[a]=[b]

print(m1)
m1[4]=['vikas']
print(m1)