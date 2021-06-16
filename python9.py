# import datetime

# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Something is happening before the function is called.")
#         func(*args,**kwargs)
#         print("Something is happening after the function is called.")
#         return func(*args,**kwargs)
#     return wrapper

# @my_decorator
# def say_whee(name):
#     print("Creating greeting")
#     return f"Hi {name}"

# adam=say_whee
# print(adam.__name__)
# print(say_whee.__name__)
# print(adam('MI3'))

# class Infinite:
#     def __init__(self,net_pay) -> None:
#         self.total_earnings=131350
#         self.net_pay=net_pay
#         self.pf_tax_deductions=2000
#         self.monthly_tax_deductions=22672
#         self.CTC_Offered=1650000
#         self.Leave_Travel_Allowance=18000
#         self.PF_Employer_Contribution=21600
#         self.Mediclaim_And_PAP=23840
#         self.Gratuity=10368
#         self.Annual_Gross=1576200
#         self.Annual_CTC_Offered=1650008
#         self.Basic=18000
#         self.House_Rent_Allowance=9000
#         self.Educational_Allowance=200
#         self.Advance_Statutory_Bonus=3000
#         self.Infinite_Flexible_Benefit_Plan=101150

    
#     def monthly_earnings(self):
#         your_earnings = self.total_earnings - (self.pf_tax_deductions + self.monthly_tax_deductions)
#         return your_earnings

#     def yearly_compensation(self):
#         total_yearly_income = self.Annual_CTC_Offered - self.Annual_Gross
#         return total_yearly_income

#     def cannot_utilize(self):
#         self.total_amount_medi_gra = self.Mediclaim_And_PAP + self.Gratuity
#         return self.total_amount_medi_gra


# may=Infinite(108164)

# monthly=may.Annual_Gross/12
# print(monthly)
# monthwise=monthly-may.monthly_tax_deductions
# print(monthwise)
# print(may.cannot_utilize())
# print(may.monthly_earnings())

print('Generators')
print('----------')
print('example-1')
def simple_function():
    n=1
    print('initial value')
    yield n

    n=n+1
    print('2nd value')
    yield n

    n=n+2
    print('3rd value')
    yield n
temp=simple_function()

print(next(temp))
print(next(temp))
print(next(temp))

print('example-2')
def simple_function_one():
    n=1
    print('initial value')
    yield n

    n=n+1
    print('2nd value')
    yield n

    n=n+2
    print('3rd value')
    yield n

for temp in simple_function_one():
    print(temp)

print('example-3')

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

for char in rev_str("hello"):
    print(char)

print('example-4')

class LoudIterator():
    def __init__(self, data):
        print("\tNow in __init__")
        self.data = data
        self.index = 0
        print(self.data)

    def __iter__(self):
        print("\tNow in __iter__")
        return self

    def __next__(self):
        print("\tNow in __next__")
        if self.index >= len(self.data):
            print(
                f"\tself.index ({self.index}) is too big; exiting")
            raise StopIteration

        value = self.data[self.index]
        self.index += 1
        print(f"\tGot value {value}, incremented index to {self.index}")
        return value


for one_item in LoudIterator('abc'):
    print(one_item)



chooseme='abcdefghij'

iterateme=iter(chooseme)

for i in range(1,9):
    print(next(iterateme))

import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))


# fill in this function
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b
# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

sentence = "the quick brown fox jumps over the lazy dog"
word=sentence.split(' ')
word_length=len(word)
empty_dict={}
for i in range(word_length):
    check_me=word[i]
    twice_check=len(check_me)
    empty_dict[check_me]=twice_check
    
print(empty_dict)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
ans = []
list_compr = [len(word) for word in words if word != 'the']
print(list_compr)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [x for x in numbers if x > 0]
print(newlist)