double=lambda x : x * 2
add=lambda x,y:x+y
product=lambda x,y,z:x*y*z 

print(double(10))
print(add(3,4))
print(product(1,2,3))

mylist=[1,2,3,4,5,6]
saveme=map(lambda x : x * 2, mylist)
print(list(saveme))

mylist1=[9,8,7,6,5]
mylist2=[1,2,3,4,5]
printme=map(lambda x,y:x+y,mylist1,mylist2)
mylist3=list(printme)
print(mylist3)

mytuple1=(1,2,3,4,5,6,7,8,9,10)
showme=filter(lambda x : x % 2 == 0, mytuple1)
print(tuple(showme))

displayme=filter(lambda x : True if x > 5 else False, mytuple1)
print(tuple(displayme))

from functools import reduce
verizon=reduce(lambda x,y : x+y,mytuple1)
print(verizon)

this is additional code