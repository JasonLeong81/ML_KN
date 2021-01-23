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

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print(ZeroDivisionError)
# except Exception as e:
#     print(e)
# else:
#     print('All Good')
# finally:
#     print('End')

# class Error(Exception):
#     pass
# class Empty(Error):
#     pass
# xx = input('Enter a number: ')
# try:
#     if xx:
#         print(xx)
#     else:
#         raise Empty
# except Empty:
#     print('Error')

### Public, Private, and Protected...all are not restricted in python, just a reminder for experienced developers ######################3
class Car(): # all class variables are protected (only can be overwritten from subclasses)
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
v = Car(1,2,3)
# print(dir(v)) # look at the last three elements
# print(v._b)
# v._b = 1
# print(v._b)
class Car(): # all class variables are public
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
vv = Car(1,2,3)
# print(dir(vv)) # look at the last three elements
# print(vv.b)
# vv.b = 1
# print(vv.b)
class Car(): # all class variables are private (cannot be accessed from anywhere)
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
vvv = Car(1, 2, 3)
# print(dir(vvv)) # look at the last three elements
# print(vvv.__b)
# vvv.__b = 1
# print(vvv.__b)




































