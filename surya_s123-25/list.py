list1 = [-1,0,1,-3,5,6,-4,-6]
print("list1:",list1)
print("positive integers")
for num in list1:
    if num >= 0:
        print(num)
list2 = [2,32,34,78,4,8,16]
print("list:",list2)
print("square of the  list")
for n in list2:
    print(n**2)
V=['a','e','i','o','u']
word=input("enter the word")
s=[i for i in word if i in V ]
print (s)
word = input("enter the word")
j=[ord(x) for x in  word]
print(j)