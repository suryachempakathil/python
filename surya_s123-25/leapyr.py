c = int(input("enter the year"))
f = int(input("enter the final year"))
print("leap year are:")
for i in range (c,f):
    if (i%4==0) and (i%100!=0) or (i%400==0):
       print(i)