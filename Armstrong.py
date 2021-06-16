print('this is for checking Armstrong number')
number=input('enter a number: ')
output=[int(i) for i in str(number)]
answer=[]
local=0
for j in range(len(output)):
    answer.append(output[j]**3)
    temp=answer[j]
    local=local+temp
if local == int(number):
    print('Armstrong')
else:
    print('Not Armstrong')

# print(output)
# print(map(int,str(number)))
# number_split= map(int,str(number))
# print(number_split)


