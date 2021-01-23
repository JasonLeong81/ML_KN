def hello(*args,**kwargs):
    print(args)
    print(kwargs)
# hello(1,2,3,4,5,x=6)
l = [1,2,3]
x = {'2':2}
# hello(*l,**x)

def addition(a,b):
    return a + b
# print(addition(1,1))
addition = lambda a,b:a+b
# print(addition(1,1))

def even(x):
    return x%2==0 and x != 0
# print(even(2))
l1 = list(range(0,11))
# print(list(map(even,l1))) # uses lazy loading # Lazy loading is a concept where we delay the loading of object until the point where we need it.

# print(list(filter(even,l1)))
# print(list(filter(lambda x:x%2==0 and x != 0,l1)))

# Iterables -> all elements are stored in memory
# Iterators -> not all elements inside list is stored in memory location, only when we call next
# l1 = iter(l1)
# print(next(l1)) # only when we execute this line, 0 will get stored in memory
# print(next(l1))

import pyforest # lazy imports
# df = pd.read_csv('titanic_train.csv')
# print(df.head())
# print(active_imports())












































