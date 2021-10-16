# Students
# Haniya Maqsood (CS-19018)
# Haleema Afshan (CS-19023)
# Rumaisa Maryam (CS-19024)
# from abc import ABCMeta, abstractmethod
# class Super(metaclass=ABCMeta):
#     def delegate(self):
#         self.action()
#     @abstractmethod
#     def action(self):
#         pass
# class Sub(Super):
#     pass
#
# x = Sub()
# x.action()
#### Question 1####
## Answer
# This will produce an error because an object of abstract class can't be instantiated until it's subclass provide
# an proper implementation of abstract method.

##### Question # 2
# from abc import ABCMeta, abstractmethod
# class Super(metaclass=ABCMeta):
#     def delegate(self):
#         self.action()
#     @abstractmethod
#     def action(self):
#         pass
# class Sub(Super):
#     pass
#     def action(self):
#         print('I\'m a sub class I can instantiate')
# x = Sub()
# x.action()
### Question # 3
# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     def __init__(self,n,s):
#         self.noOfWheel = n
#         self.speed = s
#     @abstractmethod
#     def print_func(self):
#         print(f'I have {self.noOfWheel} wheels')
#         print(f'I have {self.speed} speed')
#
# class Truck(vehicle):
#     def __init__(self,n,s,f,a):
#         super().__init__(n,s)
#         self.fuel = f
#         self.space =a
#     def print_func(self):
#         print('******* Truck details ********')
#         super().print_func()
#         print(f'I have {self.fuel} fuel')
#         print(f'I have {self.space} to accomodate')
#         print()
# class Car(vehicle):
#     def __init__(self,n,s,d,g):
#         super().__init__(n,s)
#         self.door = d
#         self.gears =g
#     def print_func(self):
#         print('******* Car details *******')
#         super().print_func()
#         print(f'I have {self.door} doors')
#         print(f'I have {self.gears} in my car')
#         print()
# class Cycle(vehicle):
#     def __init__(self,n,s,b,h):
#         super().__init__(n,s)
#         self.brake = b
#         self.horn =h
#     def print_func(self):
#         print('****** Cycle details ********')
#         super().print_func()
#         print(f'I have {self.brake} to stop the cycle')
#         print(f'I have {self.horn} to give a signal to padestarian ')
#         print()
#
#
# t = Truck(4,'20m/s','CNG','seven')
# c = Cycle(2,'2m/s','handbreak','horn bell')
# C = Car(4,'4m/s',4,'seven')
# t.print_func()
# c.print_func()
# C.print_func()

### Question # 4
from abc import ABC , abstractmethod
class basicOperation(ABC):
    def __init__(self,a=0,b=1):
        self.a = a
        self.b = b
    @abstractmethod
    def Mathematical_Operation(self):
        pass

class Addition(basicOperation):
    def __init__(self,a,b):
        super().__init__(a,b)
    def Mathematical_Operation(self):
        super().Mathematical_Operation()
        print('Addition: ',(self.a+self.b))

class Subtraction(basicOperation):
    def __init__(self,a,b):
        super().__init__(a,b)
    def Mathematical_Operation(self):
        super().Mathematical_Operation()
        print('Subtraction: ',(self.a-self.b))

class Multiplication(basicOperation):
    def __init__(self,a,b):
        super().__init__(a,b)
    def Mathematical_Operation(self):
        super().Mathematical_Operation()
        print('Multiplication: ',(self.a*self.b))

class Division(basicOperation):
    def __init__(self,a,b):
        super().__init__(a,b)
    def Mathematical_Operation(self):
        super().Mathematical_Operation()
        if self.b != 0:
            print('Division: ',(self.a/self.b))
        else:
            print('Invalid value , divisor is 0')
a = Addition(2,4)
a.Mathematical_Operation()
s = Subtraction(4,2)
s.Mathematical_Operation()
m = Multiplication(2,4)
m.Mathematical_Operation()
d = Division(4,2)
d.Mathematical_Operation()

