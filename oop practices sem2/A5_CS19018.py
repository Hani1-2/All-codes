# ## Question 1
# class Polygon:
#     def __init__(self,n=0,l=[]):
#         self.noOfSides = n
#         self.sideLengthList = l
#     def perimeter(self):
#         peri = sum(self.sideLengthList)
#         return peri
#     @property
#     def length(self):
#         return self.noOfSides
#     @length.setter
#     def length(self, lengthofSides):
#         self.sideLengthList = lengthofSides
#
#     @length.deleter
#     def length(self):
#         print('delete the sides')
#         self.sideLengthList = []
#         self.noOfSides = 0
#
# p1 = Polygon()
# p1.sideLengthList = [9,10,11,12]
# print(p1.perimeter())
# del p1.length
# print(p1.sideLengthList)

## ques 2
# class Polygon:
#     def __init__(self,n=0,l=[]):
#         self.noOfSides = n
#         self.SideLengthList = l
#     def perimeter(self):
#         peri = sum(self.length)
#         return peri
#     @property
#     def length(self):
#         return self.SideLengthList
#     @length.setter
#     def length(self, lengthofSides):
#         self.SideLengthList = lengthofSides
#
#     @length.deleter
#     def length(self):
#         print('delete the sides')
#         self.SideLengthList = []
#         self.noOfSides = 0
#
# p1 = Polygon(2,[4,5])
# p1.length = [9,10,11,12]  ### yes it works on property
# print(p1.length)
# print(p1.perimeter())
# del p1.length
# print(p1.SideLengthList)

## Question # 3
# from abc import ABC, abstractmethod
# class Polygon(ABC):
#     def __init__(self,n=0,l=[]):
#             self.noOfSides = n
#             self.lengths = l
#     @abstractmethod
#     def perimeter(self):
#         print('the sum of all sides length is called perimeter')
#     @abstractmethod
#     def lengths(self):
#         pass
# class child(Polygon):
#     def __init__(self,l=[]):
#         super().__init__(l)
#         self.length = l
#     def lengths(self):
#         return self.length
#     def perimeter(self):
#         super().perimeter()
#         return (sum(self.length))
# p=child([12,13,14,15])
# print(p.perimeter())

### Question 5
# from abc import ABC, abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def __init__(self,n=4,l=[]):
#             self.noOfSides = n
#             self.Lengths = l
#     @abstractmethod
#     def Area(self):
#         print('Area')
# class Triangle(Polygon):
#     def __init__(self,l=[]):
#         super().__init__()
#         self.l = l
#     def Area(self):
#         super().Area()
#         return (.5*self.l[0]*self.l[1])
# base = 4
# height = 7
# p=Triangle([base,height])
# print(p.Area())

# ## Ques 4
# class Triangle(Polygon):
#     def __init__(self,n,l):
#         super().__init__(n,l)
#         self.length =l
#     def perimeter(self):
#         super().perimeter()
#         print('the perimeter of triangle is follows')
#         return sum(self.length)
#     def lengths(self):
#         return self.length
# #
# base=4
# height=7
# hypotenuse = ((base**2)+(height**2)**0.5)
# p=Triangle(3,[base, height, hypotenuse]) #calculate hypotenuse
# print(p.perimeter())

## ques 6
# class Rectangle(Polygon):
#     def __init__(self,l=[]):
#         super().__init__()
#         self.length = l
#
#     def perimeter(self):
#         super().perimeter()
#         print('the perimeter of rectangle is follows')
#         return (sum(self.length)*2)
#     def lengths(self):
#         return self.length
#     def Area(self):
#         return self.length[0]*self.length[1]
# height = 2
# width = 3
# r=Rectangle([height,width])
# print(r.perimeter())
# print(r.Area())

## QUES 7
# instance variable
# noOfsides , length
# no local and class variable are used


# ques 9
# try:
#     lst = [0, 0, 0, 0]
#     with open('data.txt', 'r') as f: ##(if file is empty 2nd exception raise)
#         count = 0
#         for line in f.readlines():
#             lst[count] = int(line)
#             count += 1
# # except FileNotFoundError:
# #     print('File not found')
# except ValueError:
#     print('invalid values are given')
# print('Begin')
# x = int(input())
# print(x)
# print('End')

# print('Begin')
# try:  # when input 22 it print 22 , ZZ whole except block execute
#     x = int(input())
#     print(x)
# except ValueError:
#     print('Wrong!')
#     print('End')

# print('Begin')
# try:
#     x = int(input())
#     print(x)   ## ZZ invalid input (value error) occur
# except IndexError:
#     print('Wrong!')
#     print('End')

# print('Begin')
# try:
#     x = int(input())
#     print(x)
# except Exception: ## ZZ exception caught by except block
#     print('Wrong!')
#     print('End')
# 
# print('Begin')
# try:  # when input is 22 else block also executed.
#     x = int(input())
#     print(x)
# except ValueError:
#     print('Wrong!')   # when input iz ZZ only except block is executed
# else:
#     print('Wow')
#     print('End')
# #
# print('Begin')
# try:
#     x = int(input())
#     print(x)
# except ValueError:
#     print('Wrong!')
# finally:
#     print('Done')
#     print('End')
# 
# print('Begin')
# try:  # when input is 22 means valid try , else and finally block executed
#     x = int(input())
#     print(x)
# except ValueError:  # when input is ZZ except and finally block executed
#     print('Wrong!')
# else:
#     print('Wow')
# finally:
#     print('Done')
#     print('End')






