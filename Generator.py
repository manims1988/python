def listiter(value):
    for i in value:
        yield i

mylist=[4,3,2,1]
iterme=listiter(mylist)
print(next(iterme))
print(next(iterme))
print(next(iterme))
print(next(iterme))
