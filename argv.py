# num = int(input('enter any no: '))
# emptylist=[]
# for _ in range(num):
#     emptylist.append(int(input()))

# print(sum(emptylist))

# import sys 
# print(sum(map(int, sys.argv[1:])))

# number=10

# if len(sys.argv) == 2:
#     number=int(sys.argv[1])
# for i in range(number):
#     print('hello world')



import argparse

if __name__=='__main__':
    parser=argparse.ArgumentParser (description='my first argv')

    args=parser.parse_args
    

