
def myfunction(n1,n2,n3):
    if(n3 == 1):
        add = n1 + n2
        return add
    elif(n3 == 2):
        sub = n1 - n2
        return sub
    else:
        print("INVALID INPUT!")
    
print("HERE IS A BASIC CALCULATOR")
num1=int(input("ENTER NUMBER 1:"))
num2=int(input("ENTER NUMBER 2:"))

print("PRESS '1' FOR ADDITION.")
print("PRESS '2' FOR SUBTRACTION.")
tsk=int(input("ENTER :"))

ans = myfunction(num1,num2,tsk)
if (tsk == 1):
    print("ADDITION IS : ",ans)

elif(tsk == 2):
    print("SUBTRACTION IS : ",ans)




