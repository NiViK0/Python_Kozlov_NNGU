from functools import reduce
#print(list(map(reduce(lambda a, b: a + b, [23, 21, 45, 98]))))

d = reduce(lambda x,y: x+y, map(lambda x:x+x, filter(lambda x: (x>=3), (1,2,3,4))))
print(list(filter(lambda x: (x>=3), (1,2,3,4))))
print(list(map(lambda x:x+x, filter(la)))) 
