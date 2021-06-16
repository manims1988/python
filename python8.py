
# dict1={'one':1,'two':2,3:'three'}

# dict1['phone']=9628
# print(type(dict1))
# print(dict1)
# print(dict1['one'])
# print(dict1.keys())
# print(dict1.values())
# print(dict1.get(3))
# print(dict1.get('phone'))
# print(dict1.get('phone','FCUK'))
# print(dict1.update({'name':'rob','office':'infinite'}))
# print(dict1)
# for i, j in dict1.items():
#     print(i,j)


# for x in range(10):
#     if x > 5:
#         break
#     print(x)

# else:
#     print('all done')

# string1='i love python'
# print(string1[::-1])
# print(string1[::1])
# print(string1[-50:-1])
# # print(string1.__reversed__())
# r=reversed(string1)
# out=''.join(r)
# print(out)
# for i in r:
#     print(i,end='')

# import threading

# def show():
#     for i in range(10):
#         print('child thread')

# t=threading.Thread(target=show)
# t=threading.Thread.start(self=t)
# t.start()

# for i in range(10):
#     print('main thread')




# print(threading.currentThread().getName())
# print(threading.current_thread().)
# threading.main_thread()


# import time
# print(time.time())
# print(time.localtime())
# time.sleep(10)
# print(time.time())
# print(time.thread_time())
# print(time.ctime(time.time()))

# import datetime

# print(datetime.date(2021,9,2))
# print(datetime.datetime.now())
# print(datetime.date.today())

# from threading import *
# import threading
# import time

# class Aqua(threading.Thread):
#     def run(self):
#         for i in range(5):
#             print('child thread-1')

# class Libra(threading.Thread):
#     def run(self):
#         for i in range(5):
#             print('child thread-2')

# t1=Aqua()
# t2=Libra()
# t1=threading.Thread(target=Libra)
# t2=threading.Thread(target=Aqua)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('bye')

# x=[(i,j) for i in 'abcd' for j in range(4)]
# print(x)
# mylist=[k*k for k in x ]
# print(mylist)
# y=map(lambda v: v*v,x)
# print(y)
# name=['bruce','tom','kai','lee']
# color=['red','black','yellow','white']
# print(zip(name,color))
# kode = {name:color for name,color in zip(name,color)}
# print(kode)
# kode1=[x if x==3 else x*x for x in range(1,6)]
# print(kode1)
# v=[1,2,3,4]
# kode3=[m*4 for m in v]
# print(kode3)

# def avg(n1,n2,m3):
#     x=10
    # print(n1)
    # print(n2)
    # print(m3)
    # print(x)
    # return (n1+n2+m3)/x
# x=3
# def dvd():
#     # global x
#     # x=10
#     global x
#     x=x+1
#     print('from dvd',x)
#     return 

# def cdrom():
    # x=5
#     print('from cdrom',x)
 # cdrom()
# dvd1=dvd()
# print(dvd1)
# avg1=avg(5,6,7)
# print(avg1)
# var=10
# def fun():
        # var=var+1
#         print(var)
#         return
# fun()
# sum1=lambda v1,v2: v1+v2
# print(sum1(3,4))
# def fun(**var):
#     print(var)
#     print(type(var))
# fun(one=1,two=2,three=3,four=4,five=5)
# x=10
# def fun():
#     global x
#     print('1st inside fun',x)
#     x=20
#     print('inside fun',x)
#     def inner():
        # global x
        # print('before value',x)
        # x=30
#         print('innermost value',x)
#     inner()
# fun()
# print('inside main fun',x)
# x=10
# def outer():
#     x=20
#     print('outer',x)
#     def inner():
#         global x
#         x=30
#         print('inner',x)
#     print('another outer',x)
#     inner()
#     print('outer version-3',x)

# outer()
# print('main',x)

# import threading

# class One(threading.Thread):
#     def run(self):
#         for i in range(1,6):
#             print(f'one thread-{i}')

# class Two(threading.Thread):
#     def run(self):
#         for i in range(1,6):
#             print(f'two thread-{i}')

# t1=One()
# t2=Two()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('bye')


# class Coffee:
#     def __init__(self,temp) -> None:
#         self.temp=temp

#     def hot(self):
#         if self.temp > 40:
#             raise ValueError
#         elif self.temp < 40:
#             raise TypeError
#         else:
#             print('coffee is OK')

# c1=Coffee('31')
# c1.hot()
# def hello(func):                                                                                            
#     def inner():                                                                                            
#         print("Hello ")                                                                                     
#         func()                                                                                              
#     return inner                                                                                            
# def name():                                                                                                 
#     print("Alice")                                                                                                                                                                                    
# obj = hello(name)                                                                                           
# obj() 
def hello():
    print('this is hello function')

hi=hello
hi()
print('==================')
def first(msg):
    print(msg)
first("Hello from first")
second = first
second("Hello from second")
print('=====================')
def jade(func):
    def amber():
        print('this is decoration') 
        print(func())
    return amber  

def outer(func):
    def inner():
        makemeupper=func()
        return makemeupper.upper()
    return inner

@jade
@outer
def talk():
    return 'hello world'

talk()

print('==================')
def added(x):
    return x+x
def subract(y):
    return y-1
def division(z):
    return z/2
def operator(func,variable):
    result=func(variable)
    print(result)

operator(division,4)
print('=========================')
def outer():
    def inner():
        print('inner function')
    return inner 

new=outer()
new()
print('=========================')

def fun1():
    print('this is fun1')

def fun2(jake):
    print('this is fun2')
    jake()

def fun3(pounce):
    print('this is fun3')
    pounce(fun1)

fun3(fun2)
print('=========================')
def hello(name):
    return f'hello {name}'
def hi(name):
    return f'hi {name}'
def hellohi(name):
    return name('bob')

print(hellohi(hello))
print('=========================')



def simple():
    print()
print('=========================')
print('=========================')
print('=========================')


# import copy
# class Book:
#     def __init__(self,title,author) -> None:
#         self.title=title
#         self.author=author
#     def display(self):
#         return f'book name is {self.title} and author is {self.author}'

# mybook=Book('Java','javadeveloper')
# print(mybook.display())
# newbook=copy.copy(mybook)
# print(newbook.display())
# newbook.title='python'
# newbook.author='pythondeveloper'
# print(newbook.display())

import copy
class Book:
    def __init__(self,title,author) -> None:
        self.title=title
        self.author=author
    def display(self):
        return f'book name is {self.title} and author is {self.author}'

mybook=Book('Java','javadeveloper')
newbook=Book('python','Real Python')
book_list=[mybook,newbook]
new_book_list=copy.deepcopy(book_list)
new_book_list[1].author='corey schafer'
print(new_book_list[1].display())
print(book_list[1].display())
