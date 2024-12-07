def myfunction1(st,en):
    if (st<=en):
        print(st)
        myfunction1(st+1,en)
    else:
        return
   
def myfunction2(st,en):
    if (st<=en):
        print(en)
        myfunction2(st,en-1)
    else:
        return

print("THIS CODE WILL PROVIDE A SEQUENCE OF NUMBER")
s=int(input("ENTER THE STARTING NUMBER: "))
e=int(input("ENTER THE ENDING NUMBER: "))
myfunction1(s,e)
myfunction2(s,e)
 

