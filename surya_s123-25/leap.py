c=int(input("enter the current yr"))
f=int(input("enter the fianl year"))
print("leap years are:")
for i in range(c,f):
    if(i%4==0) and (i%100!=0):
        print(i)