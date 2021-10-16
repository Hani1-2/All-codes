# Ques 1 class cirlce
# import math
# class circle:
#     def __init__(self,radius=0,color=None):
#         self.radius = radius
#         self.color = color
#
#     def set_radius(self,r):
#         self.radius = r
#     def get_radius(self):
#         return self.radius
#     def set_color(self,c):
#         self.color = c
#     def get_color(self):
#         return self.color
#     def get_circumference(self):
#         return (2*math.pi*self.radius)
#     def get_area(self):
#         return (math.pi*(self.radius**2))
# p1=circle()
# p1.set_radius(3)
# p1.set_color('pink')
# print(p1.get_radius())
# print(p1.get_color())
# print(p1.get_area())
# print(p1.get_circumference())

# QUES # 2
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#     def with_draw(self):
#         amount = int(input('enter amount you want to with draw'))
#         if self.balance <=0:
#             print ('Sorry! you have not sufficient balance to withdraw this amount ')
#         else:
#             self.balance -= amount
#             print (f'this {amount} is withdrawn from your balance')
#             return self.balance
#
#     def deposit(self):
#         amount = int(input('enter amount you want to deposit '))
#         if amount <=0 :
#             print ('please deposit sufficient amount')
#         else:
#             self.balance += amount
#             print (f'this {amount} amount is deposit to your balance')
#
#     def balance(self):
#         return self.balance
#
# p1 = BankAccount()
# p1.deposit()
# p1.with_draw()
# print('your remaining balance is',p1.balance)

#QUES # 3
# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
#     def with_draw(self):
#         amount = int(input('enter amount you want to with draw'))
#         if self.__balance <=0:
#             print ('Sorry! you have not sufficient balance to withdraw this amount ')
#         else:
#             self.__balance -= amount
#             print (f'this {amount} is withdrawn from your balance')
#             return self.__balance
#
#     def deposit(self):
#         amount = int(input('enter amount you want to deposit '))
#         if amount <=0 :
#             print ('please deposit sufficient amount')
#         else:
#             self.__balance += amount
#             print (f'this {amount} amount is deposit to your balance')
#
#     def set_balance(self):
#          x = self.__balance
#     def get_balance(self):
#         return x
# p1 = BankAccount()
# p1.deposit()
# p1.with_draw()
# print('your remaining balance is',p1._BankAccount__balance)

# ques 4
# class workers:
#     def set_hours_worked(self,h):
#         self.__HoursWorked = h
#     def changerate(self,r):
#         self.__WageRate = r
#     def pay(self):
#         return (self.__HoursWorked * self.__WageRate)
#
# p1 = workers()
# p1.set_hours_worked(6)
# p1.changerate(200)
# print(p1.pay())

##ques 5
# class workers:
#     def __init__(self):
#         self.__WageRate = 100
#         self.__HoursWorked = 0
#
#     def set_hours_worked(self,h):
#         self.__HoursWorked = h
#     def changerate(self,r):
#         self.__WageRate = r
#     def pay(self):
#         return (self.__HoursWorked * self.__WageRate)
#
# p1 = workers()
# p1.set_hours_worked(6)
# p1.changerate(200)
# print(p1.pay())

# #QUES # 6
# class vehicles():
#     def __init__(self,n=4,c='black',m='CE175'):
#         self.__noOfWheels = n
#         self.__color = c
#         self.__modelNo = m
#     def set_noOfWheel(self,n):
#         self.__noOfWheels = n
#     def get_noOfWheel(self):
#         return self.__noOfWheels
#     def set_color(self,c):
#         self.__color = c
#     def get_color(self):
#         return self.__color
#     def set_model(self,m):
#         self.__modelNo = m
#     def get_model(self):
#         return self.__modelNo
#
# p1 = vehicles()
# p1.set_noOfWheel(4)
# print(p1.get_noOfWheel())
# p1.set_color('turquiose')
# print(p1.get_color())
# p1.set_model('cor104')
# print(p1.get_model())
#
# # ques # 7
# class engine:
#     def __init__(self,engNo = '1234',date='02-02-2020'):
#         self.__EngineNo = engNo
#         self.__dateOfManufacture = date
#     def set_EngineNO(self,e):
#         self.__EngineNo = e
#     def get_EngineNo(self):
#         return self.__EngineNo
#     def set_DateOfManufacture(self,d):
#         self.__dateOfManufacture = d
#     def get_DateOfManufacture(self):
#         return self.__dateOfManufacture
#
# a1 = engine()
# a1.set_EngineNO('12345')
# print(a1.get_EngineNo())
# a1.set_DateOfManufacture('12-09-2001')
# print(a1.get_DateOfManufacture())

# #ques 8
# class Int:
#     def __init__(self,i1=0,i2=0):
#         self.int_1 =i1
#         self.int_2 =i2
#     def set_int_1(self,i1):
#         self.int_1 = i1
#     def set_int_2(self,i2):
#         self.int_2 = i2
#     def add_int(self):
#         int_3 = self.int_1 +self.int_2
#         return int_3
#
# a1 =Int()
# a1.set_int_1(20)
# a1.set_int_2(30)
# print(a1.add_int())

##qUES 12
# class Tracker:
#     count = 0
#     def __init__(self):
#         Tracker.count+=1
#         self.countMethod()
#     def countMethod(self):
#         Tracker.count += 1
#         print('I am a Tacker no',Tracker.count)
#
# t1 = Tracker()
# print(t1.countMethod())
# t2 = Tracker()
# print(t2.countMethod())
# t3 = Tracker()
# print(t3.countMethod())

##Ques 9
# class TollBooth:
#     def __init__(self,c=0,p=0):
#         self.total_no_of_car = c
#         self.total_pay = p
#         self.paying_car = 0
#         self.non_paying_car =0
#
#     def PayingCar(self):
#         self.total_no_of_car += 1
#         self.total_pay += 50
#         self.paying_car +=1
#
#     def NoPayingCar(self):
#         self.total_no_of_car +=1
#         self.non_paying_car +=1
#     def checkaccount(self):
#         # for i in range (self.total_no_of_car):
#         while True:
#             print('press y to count the paying car \npress z to count the non paying car\npress another key to see total car , cash and exit')
#             find = (input('>>> '))
#             if find == 'y':
#                 print('No of paying car',self.paying_car)
#             elif find == 'z':
#                 print('No of non paying car',self.non_paying_car)
#             else:
#                 print('total no of cars:',self.total_no_of_car)
#                 print('total cash',self.total_pay)
#                 break
#     def Display(self):
#         return ('The No.of Total car is',self.total_no_of_car ,'The Total amount collected is',self.total_pay)
#
# p1=TollBooth()
# p1.PayingCar()
# p1.NoPayingCar()
# p1.PayingCar()
# p1.checkaccount()




##Ques 11
# class Angle:
#     def __init__(self,d=0,m=0,c='W'):
#         self.degree = int(d)
#         self.minute = float(m)
#         self.direction = c
#
#     def Convertor(self):
#         self.minute/=60

# class Int:
#     def __init__(self,i1=2,i2=4):
#         self.int_1 = i1
#         self.int_2 = i2
#     def set_int(self,i1,i2):
#         self.int_1 = i1
#         self.int_2 = i2
#     def get_int(self):
#         new = self.int_1 + self.int_2
#         return new
# p1=Int()
# p1.set_int(7,8)
# print(p1.get_int())


class Angle:
    def __init__(self,d=0,m=0,di=0):
        self.degree = int(d)
        self.minute = float(m)
        self.direction = str(di)
        self.l = []

    def find_location(self):
        while True:
            loc = input("press 'l' to enter location")
            if loc == 'l':
                x = input('Enter degree for longitude (0-180): ')
                y = input('Enter minute for longitude: ')
                self.degree = int(x)
                z = input('enter direction press E for East and W for West')
                self.minute = float(y)
                self.direction = str(z)
                self.display_location()
                self.l.append([self.degree,self.minute,self.direction])
                x1 = input('Enter degree for latitude (0-90): ')
                y1 = input('Enter minute for latitude: ')
                z1 = input('enter direction press N for North and S for South')
                self.degree = int(x1)
                self.minute = float(y1)
                self.direction = str(z1)
                self.display_location()
                self.l.append([self.degree,self.minute,self.direction])
                print('Hit enter to exit or c to continue')
                f = input()
                if f=='':
                    break
                else:
                    continue




    def display_location(self):
        print('required direction:',self.degree,'\u00b0',self.minute,"'",self.direction,sep='')
#
# p1=Angle()
# p1.find_location()

class ship(Angle):
    serial_no = 0
    def __init__(self):
        super().__init__(d=0,m=0,di=0)
        self.d={'serialno':'location'}
        ship.serial_no += 1

    def ship_loc(self):
        ship.find_location(self)
        lst = self.l
        self.d[self.serial_no]= lst


s = ship()
s.ship_loc()
s1=ship()
s1.ship_loc()
print(s.d)
print(s1.d)

