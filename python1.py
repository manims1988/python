import getpass

print('welcome to Mani ATM')
pin = getpass.getpass('enter your 4 digit pin number \n') 

mani_pin = 9876
chance = 0 
amount = 1000

while chance < 5:
    chance = chance + 1
    if chance == 4:
        print('used 3 transactions and exiting now')
        break
    if  mani_pin == int(pin):
        pass
    else:
        print('wrong pin')
        break

    pin_len = len(pin)
    if pin_len == 4:
        pass
    else:
        print('Dont enter more than 4 numbers')
        break

    try:
        pin == int(pin)
    except ValueError:
        print('enter only numbers')
        break
    
    # print('available amount before withdraw {}'.format(amount))
    acc = input('balance enquiry(b) or withdraw(w) \n')
    if acc == 'b':
        print('availale balance = ', amount)
    elif acc == 'w':
        money = int(input('enter the amount to withdraw \n'))
        if money <= amount:
            subract = amount - money
            print('available balance is {}'.format(subract))
            print('money withdrawn is {}'.format(money))
        else:
            print('please enter within your limit')
    else:
        print('enter correct option')
    con = input('do you want to continue y/n ?')
    if con == 'y':
        continue
    elif con == 'n':
        break 
    else:
        print('unknow value') 
print('Thanks for using mani atm')