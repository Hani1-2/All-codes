###Slide 7
##
# from abc import ABC, abstractmethod
#
# class Polygon(ABC):
#    @abstractmethod
#    def noOfSides(self):
#        pass
#
# class Square(Polygon):
#    def noOfSides(self):
#        print('I have 4 sides')
#
# class Triangle(Polygon):
#    def noOfSides(self):
#        print('I have 3 sides')
#
# #a=Polygon()
# b=Square()
# b.noOfSides()
# c=Triangle()
# c.noOfSides()


###Slide 8
##
##from abc import ABC, abstractmethod
##
##class Polygon(ABC):
##    @abstractmethod
##    def noOfSides(self):
##        print('I am a type of polygon')
##
##class Square(Polygon):
##    def noOfSides(self):
##        super().noOfSides()
##        print('I have 4 sides')
##
##b=Square()
##b.noOfSides()


###Slide 9
##
##from abc import ABC, abstractmethod
##
##class Polygon(ABC):
##    @abstractmethod
##    def noOfSides(self):
##        print('I am a type of polygon')
##    def shape(self):
##        print('I am a 2D shape')
##
##class Square(Polygon):
##    def noOfSides(self):
##        super().noOfSides()
##        print('I have 4 sides')
##
##b=Square()
##b.noOfSides()
##b.shape()


###Slide 11
##
# from collections import Container

# class OddContainer:
#    def __contains__(self, x):
#        if not isinstance(x, int) or not x % 2:
#            return False
#        return True
#
# num=OddContainer()
# print(1 in num)
# print(2 in num)
# print(237813 in num)
# print(isinstance(num,OddContainer))
# print(issubclass(OddContainer,Container))
# class EvenContainer:
#    def __contains__(self, x):
#        if not isinstance(x, int) or not x % 2:
#            return True
#        return False
#
# num=EvenContainer()
# print(1 in num)
# print(2 in num)
# print(237813 in num)
# print(isinstance(num,EvenContainer))
# print(issubclass(EvenContainer,Container))


###Slide 14, usig property function
##
# class Pencil():
#    def __init__(self, c='red'):
#        self.color=c
#        self.eraser = f'I can erase {self.color} pencil work' # thats why we used property b/c after changing color
#        # constructor will not run so self.eraser will not updated
#    def getColor(self):
#        return self.color
#    def setColor(self,c):
#        self.color=c
#    def delColor(self):
#        del self.color
#    COLOR=property(getColor,setColor,delColor,'I am a property')
#    # COLOR=property(getColor,setColor,None,'I am a property')
#
# a=Pencil()
# print(a.COLOR)
# print(a.eraser)
# a.COLOR='green'
# print(a.COLOR)
# print(a.eraser)
# print(help(a))
# del a.COLOR
#print(a.COLOR) #error


###Slide 14, using decorators
##
# class Pencil():
#    def __init__(self, c='red'):
#        self.color=c
#    @property
#    def COLOR(self):
#        'This is a property'
#        return self.color
#    @COLOR.setter
#    def COLOR(self,c):
#        self.color=c
#    @COLOR.deleter
#    def COLOR(self):
#        del self.color
#
# a=Pencil()
# print(a.COLOR)
# a.COLOR='green'
# print(a.COLOR)
# print(help(a))
##del a.COLOR
###print(a.COLOR) #error


###Slide 15
##
# from abc import ABC, abstractmethod,abstractproperty
# class Pencil(ABC):
#    def __init__(self, c='red'):
#        self.color=c
#        self.sharpner = f'I can sharp {self.color} pencil because I\'m a sharpner'
#    @abstractproperty
#    def COLOR(self):
#        'This is a property'
#        return self.color
#    @COLOR.setter
#    def COLOR(self,c):
#        self.color=c
#        self.sharpner = f'I can sharp {self.color} pencil because I\'m a sharpner'
#    @COLOR.deleter
#    def COLOR(self):
#        del self.color
# class child(Pencil):
#    COLOR='yellow'
#
#
# a=child()
# print(a.COLOR)
# print(a.sharpner)
# a.COLOR='green'
# print(a.sharpner)
# print(a.COLOR)
#
#
# class Pencil():
#    def __init__(self, c='red'):
#        self.color=c
#        self.sharpner = f'I can sharp {self.color} pencil because I\'m a sharpner'
#    @property
#    def COLOR(self):
#        'This is a property'
#        return self.color
#    @COLOR.setter
#    def COLOR(self,c):
#        self.color=c
#        self.sharpner = f'I can sharp {self.color} pencil because I\'m a sharpner'
#
#    @COLOR.deleter
#    def COLOR(self):
#        del self.color
# class child(Pencil):
#     pass
#
# a=child()
# print(a.COLOR)
# print(a.sharpner)
# a.COLOR='green'
# print(a.COLOR)
# print(a.sharpner)
# print(a.COLOR)

###Slide 17
##
# class Airplane():
#    def fly(self):
#        print("fly with fuel!")
#    def setNoOfPassengers(self,p):
#        self.noOfPassengers=p
#
# class Duck():
#    def fly(self):
#        print("fly with wings!!")
#    def swim(self):
#        print("swin in ponds!!")
#
# class Fish:
#    def swim(self):
#        print("fish swim in sea")
#
# def moves(x):
#    x.fly()
#
# a=Airplane()
# d=Duck()
# f=Fish()
# moves(a)
# moves(d)
##moves(f) #error
#
# class Bakery():
#     def __init__(self,c):
#         self.cake = c
#         self.flavour = f'The cake has a {self.cake} flavour'
#     @property
#     def CAKE(self):
#         'this is my cake factory'
#         return self.cake
#     @CAKE.setter
#     def CAKE(self,c):
#         self.cake = c
#         self.flavour = f'The cake has a {self.cake} flavour'
#     @CAKE.deleter
#     def CAKE(self):
#         del self.cake
#
# b = Bakery('Chocolate')
# print(b.flavour)
# b.CAKE = 'Strawberry'
# print(b.flavour)
# b.CAKE  = 'Red velvet'
# print(b.flavour)
# print(help(b))
# print(not(12%2))
