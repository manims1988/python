import datetime
import random

outside_class = ['rust','spice','chili','imperial']

class Trapartist:

    inside_class = {'yale':4567,'olympic':9201,'prussian':2049}

    def __init__(self,name) -> None:
        self._name = name 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, maroon):
        self._name = maroon

    @staticmethod
    def teal():
        today=datetime.datetime.today()
        now=datetime.datetime.now().hour
        urpickis = random.choice(outside_class)
        print(f'date is {today} and hour is {now} and your pick is {urpickis}')

    @classmethod
    def navy(cls):
        return cls.inside_class

crimson = Trapartist('Rosey')
print(crimson.name)
crimson.name = 'Ross'
print(crimson.name)
crimson.teal()
print(crimson.navy())

print('###################################################################################################################################################')
class Testme:

    def __init__(self,var) -> None:
        self.__var=var

    def show(self):
        return f'from show method : {self.__var}'
    
    def set_val(self,value):
        self.__var = value

    def get_val(self):
        return f'from get_var method : {self.__var}'

checkme=Testme(30)
print(checkme.show())

checkme.set_val(89)
print(checkme.get_val())
print(checkme.show())

print('###################################################################################################################################################')

class Bering:

    def __init__(self, age) -> None:
        self.__age = age

    def display(self):
        return f'age from display is {self.__age}'

    def set_val(self, instance_obj):
        self.__age = instance_obj

    def get_val(self):
        return self.__age

    def del_val(self):
        del self.__age 

    age = property(get_val,set_val,del_val)

caspian = Bering(40)
caspian.age=70
print(caspian.display())

caspian.set_val(60)
print(caspian.get_val())
print(caspian.display())

print('###################################################################################################################################################')

class Colorful:

    def __init__(self, choice) -> None:
        self.__choice = choice 

    def maui(self):
        return f'default color is {self.__choice}'

    @property
    def color(self):
        return self.__choice

    @color.setter
    def color(self, urchoice):
        self.__choice = urchoice

    @color.deleter
    def color(self):
        del self.__choice

mychoice = Colorful('Pink')
print(mychoice.maui())
mychoice.color = 'coral'
print(mychoice.color)
print(mychoice.maui())

    
    

        
