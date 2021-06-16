# class NotFoundYourFile(Exception):
#     def __init__(self,msg):
#         self.msg=msg

# f=None
# try:
#     f=open('hello1.go','r')
# except:
#     print('except')
#     raise NotFoundYourFile('pls choose other file')
# else:
#     print(f.read())
# finally:
#     if f is not None:
#         f.close()
#         print('finally')

# with open('hello.go','r') as f:
    # f.write('this is append line\n')
    # print(f.read(4))
    # print(f.readline(10))
    # print(f.readlines()[4])
    # for i in f:
    #     print(i)
# x=5
# def fun():
#     x=1
#     print('outer x is ',x)
#     def fun1():
        # global x
        # print('after global x is ',x)
#         x=2
#         print('inner x is ',x)
#     fun1()

# fun()
# print('another x is',x)
# x=3
# print('main x is ',x)
# class Car:
#     def __init__(self,speed,color) -> None:
#         self.__speed=speed 
#         self.__color=color 
#         self.__maxspeed=200
#         self.__name='Q4'
    
#     @property
#     def show(self):
#         print(f'speed is {self.__speed} and color is {self.__color}')
#         print(f'speed is {self.__maxspeed} and name is {self.__name}' )
#     @show.setter
#     def show(self,value1):
#         __speed,__color=value1.split(' ')
#         self.__speed=__speed
#         self.__color=__color

#     def set_val(self,value):
#         self.__maxspeed=value
    
#     def get_val(self):
#         return self.__maxspeed

# bmw=Car(100,'red')
# audi=Car(120,'black')
# audi.show = '160 white'
# bmw.set_val(201)
# print(bmw.get_val())
# print(audi.show)
# y=10
# def inner():
#     y=20
#     def innermost():
#         nonlocal y
#         y=y+1
#         print('y is',y)
#     innermost()
# inner()
# print('main y is',y)
    # global y
    # z=4
    # def innermost():
    #     nonlocal z
    #     x=6
    #     print('innermost x is',x)
        
        # z=z+1
        # print('innermost z is',z)
        # y=y+2
        # print('innermost y is',y)
    # y=y+1
#     innermost()
#     print('inner z is',z)
#     print('inner y is',y)
# inner()
# print('outside y is',y)
# def outer():
#     x=4
#     def inner():
#         nonlocal x
#         x=x+4
#         return x
#     return inner
# a=outer()
# print(a())
# def fun1():
#     print('from fun1')
#     print(5+15)
# def fun2(fake):
#     print('from fun2')
#     print(20+5)
#     fake()
# def fun3(pounce):
#     print('from fun3')
#     print(40+5)
#     pounce(fun1)
# fun3(fun2)
# def outer(func):
#     def inner():
#         str1=func()
#         return str1.upper()
#     return inner
# @outer
# def str1():
#     return 'good morning'
# print(str1())
# a=outer(str1)
# print(a())
# def two(func):
#     def three(x,y):
#         if y == 0:
#             return 'given value is zero'
#         return func(x,y)
#     return three 
# @two
# def one(a,b):
#     return a/b
# print(one(4,2))
# def type_check(correct_type):
#     def check(old_function):
#         def new_function(arg):
#             if (isinstance(arg, correct_type)):
#                 return old_function(arg)
#             else:
#                 print("Bad Type")
#         return new_function
#     return check

# @type_check(int)
# def times2(num):
#     return num*2

# print(times2(2))
# times2('Not A Number')

# @type_check(str)
# def first_letter(word):
#     return word[0]

# print(first_letter('Hello World'))
# first_letter(['Not', 'A', 'String'])

# def make_bold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped

# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# def make_underline(fn):
#     def wrapped():
#         return "<u>" + fn() + "</u>"
#     return wrapped
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return "hello world"
# print(hello()) ## returns "<b><i><u>hello world</u></i></b>"

# def shout(text):
#     return text.upper()
# print(shout('hello'))
# voice=shout
# print(voice('welcome'))
# def case1(fn):
#     def innercase1(text):
#         return fn(text).upper()
#     return innercase1
# def case2(fn):
#     def innercase2(text):
#         return fn(text).lower()
#     return innercase2
# @case1
# def display(text):
#     return text
# @case2
# def show(text):
#     return text
# print(display('Hello World'))
# print(show('Hello World'))
# import datetime
# import time

# class Student:
#     raise_amount=1.04
#     bus_fees=100
#     school_fees=1000
#     def __init__(self,age,name,school) -> None:
#         self.age=age
#         self.name=name
#         self.school=school
#     def method1(self):
#         return 'name is {} studying at {} has age {}'.format(self.name,self.school,self.age)
#     def method2(self):
#         total_fees = self.school_fees + self.bus_fees
#         return total_fees
#     def __repr__(self) -> str:
#         return 'Student({},{},{})'.format(self.age,self.name,self.school)
#     def __str__(self) -> str:
#         return f'{self.name} {self.school}'
#     @classmethod
#     def method3(cls,value):
#         name,school,age=value.split('-')
#         return cls(age,name,school)
#     @staticmethod
#     def workday(day):
#         if datetime.datetime.weekday(day) == 5 or datetime.datetime.weekday(day) == 6:
#             return 'weekened'
#         return True
# class Teacher(Student):
#     raise_amount=2.90
#     school_fees=2000
#     bus_fees=200
#     def __init__(self, age, name, school, lunch,sal) -> None:
#         super().__init__(age, name, school)
#         self.lunch=lunch
#         self.sal=sal
#     def show(self):
#         return 'today lunch is {}'.format(self.lunch)
#     def hike(self):
#         total_hike=int(self.sal * Teacher.raise_amount)
#         return total_hike

# class Pricipal(Student):
#     def __init__(self, age, name, school,emp=None) -> None:
#         super().__init__(age, name, school)
#         if emp is None:
#             self.emp = []
#         else:
#             self.emp=emp
#     def add_emp(self,val):
#         if val not in self.emp:
#             self.emp.append(val)
#     def remove_emp(self,val1):
#         if val1 in self.emp:
#             self.emp.remove(val1)
#     def list_emp(self):
#         for emp1 in self.emp:
#             print(emp1.method1())

# stu1=Student(12,'jeorge','MAVMM')
# stu2=Student(13,'rama','SBHSS')
# dev1=Teacher(23,'rama','SBHSS','maggi',3000)
# dev2=Teacher(25,'Yola','VHBHSS','noodle',4000)
# pri1=Pricipal(31,'mohan','SBHSS',[dev1,dev2])
# print(pri1)
# class Employee:
#     def __init__(self,fname,lname,pay) -> None:
#         self.fname=fname
#         self.lname=lname
#         self.pay=pay
#         # self.email=fname + '.' + lname + '@email.com'
#     @property
#     def email(self):
#          return f'{self.fname}.{self.lname}@email.com'
#     @property
#     def fullname(self):
#         return f'{self.fname} {self.lname}'

#     @fullname.setter
#     def fullname(self,name):
#         fname,lname=name.split('-')
#         self.fname=fname
#         self.lname=lname

# emp1=Employee('jegan','mohan',3000)
# emp1.fname='ram'
# emp1.fullname='veera-mohan'
# print(emp1.fullname)

# class Parent:
#     def __init__(self) -> None:
#         print(Parent.__name__)
#         print(Parent.mro())
# class Grandparent:
#     def __init__(self) -> None:
#         print(Grandparent.__name__)
#         print(Grandparent.mro())
# class Child(Grandparent,Parent):
#     def __init__(self) -> None:
#         Parent.__init__(self)
#         Grandparent.__init__(self)
#         print(Child.__name__)
#         print(Child.mro())
# child=Child()
# class Salary:
#     def __init__(self,pay,bonus) -> None:
#         self.pay=pay 
#         self.bonus=bonus
#     def total_salary(self):
#         annual_salary = (self.pay*12) + self.bonus
#         return annual_salary
# class Employee:
#     def __init__(self,name,age,pay,bonus) -> None:
#         self.name=name
#         self.age=age
#         self.class_object=Salary(pay,bonus)
#     def total_amount(self):
#         return self.class_object.total_salary()
# emp1=Employee('jim hawks',23,20000,300)
# print(emp1.total_amount())
# class Salary:
#     def __init__(self,pay,bonus) -> None:
#         self.pay=pay 
#         self.bonus=bonus
#     def total_salary(self):
#         annual_salary = (self.pay*12) + self.bonus
#         return annual_salary
# class Employee:
#     def __init__(self,name,age,salary) -> None:
#         self.name=name
#         self.age=age
#         self.class_object=salary
#     def total_amount(self):
#         return self.class_object.total_salary()
# salary=Salary(20000,300)
# emp1=Employee('jim hawks',23,salary)
# print(emp1.total_amount())
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Size(Shape):
#     def __init__(self,side) -> None:
#         self.__side=side
#     def area(self):
#         return self.__side * self.__side
#     def perimeter(self):
#         return self.__side * 4

# triangle=Size(5)
# print(triangle.area())
# triangle.__side=6
# print(triangle.area())
# for i in range(5):
#     for j in range(1,i+1):
#         print('\n',j,'\n',end=' ')
class Listiteration:
    def __init__(self,b) -> None:
        self.b=b
        self.index=-1
    def __iter__(self):
        return self 

    def __next__(self):
        self.index = self.index + 1
        return self.b[self.index]

a=[1,2,3,4,5,6,7,8,9]
takeme=Listiteration(a)
it=iter(takeme)
print(next(it))
print(next(it))
print(next(it))

