fruits={'Apple': 2,'orange': 14,'pineapple': 31,'watermelon' : 61,'Grapes' : 10}
l=list(fruits.items())
l.sort()
print('ascending order: ', l)
l=list(fruits.items())
l.sort(reverse=True)
print('descending order is: ', l)