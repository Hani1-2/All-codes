# ##Question # 1
# #
# class PhoneBook(list):
#
#    #Adding contacts
#    #Explicit definition not needed,
#    #append method of list can be directly accessed
#
#    #Printing the phonebook
#    #Explicit definition not needed,
#    #object will be printed as a two dimensional list
#
#    #For pretty printing
#    # def __str__(self):
#    #     strg='Name,Phone No., Email\n'
#    #     for item in self:
#    #         strg+=item[0]+', '+item[1]+', '+item[2]+'\n'
#    #     return strg
#
#
#
#    #For even prettier printing
#    def __str__(self):
#        temp='{name:20}{phone:15}{email:20}\n'
#        strg='Name                Phone          Email\n'
#        for item in self:
#            strg+=temp.format(name=item[0],phone=item[1],email=item[2])
# #        return strg
# #
# #
# #    #Sorting the phonebook name-wise
# #    #Explicit definition not needed,
# #    #sort method of list can be directly accessed
# #
# #    #Searching a contact by first or last name
# #    def search(self,name):
# #        contactsFound=PhoneBook()
# #        for item in self:
# #            if name in item[0]:
# #                contactsFound.append(item)
# #        return contactsFound
# #
# # class ProtectedPhoneBook(PhoneBook):
# #     def __init__(self):
# #         pass
# #     def pop(self,ind):
# #         print('popping is not allowed')
# #     def remove(self,obj):
# #         print('its protected you cant remove it')
# # #
# # Book1=ProtectedPhoneBook()
# # Book1.append(['Maria Waqas','111','mariaw@neduet.edu.pk'])
# # Book1.append(['Ibshar Ishrat','222','ibshar@neduet.edu.pk'])
# # print(Book1)
# # Book1.sort()
# # print(Book1)
# # Book1.pop(0)
# # Book1.remove('Maria Waqas')
# #
# class Sales:
#     def __init__(self):
#         pass
#     def get_data_2(self):
#         l=[]
#         print('Enter three price of Books')
#         for i in range(3):
#             num = float(input('>>> '))
#             l.append(str(num)+'$')
#         self.lst = l
#         return self.lst
#
#     def put_data_2(self):
#         print ('your sales are',self.lst)
#
# class Publication():
#     def __init__(self,title,price):
#         self.title = title
#         self.price = float(price)
#     def show_data(self):
#         print('The title of book is',self.title, 'and its price is',self.price)
#
# class Book(Publication):
#     def __init__(self,title,price,pagecount=0):
#         Publication.__init__(self,title,price)
#         self.pagecount = pagecount
#         self.new=Sales()
#     def get_data(self):
#         pg = int(input('enter total pages of book \n>>> '))
#         self.pagecount += pg
#     def put_data(self):
#         print('the total pages of book are',self.pagecount)
#
# class Tape(Publication):
#     def __init__(self,title,price,t =0):
#         Publication.__init__(self, title, price)
#         self.time = t
#         self.new = Sales()
#     def get_data(self):
#         t = int(input('enter the time of recording \n>>> '))
#         self.time += int(t)
#         return self.time
#     def put_data(self):
#         print ('the time of recording is',self.time,'minutes')
# #
# # ##using composition
# # p1 = Book('alchemist',300)
# # p1.show_data()
# # p1.get_data()
# # p1.put_data()
# # p1.new.get_data_2()
# # p1.new.put_data_2()
# # p2 = Tape('alchemist',400)
# # p2.get_data()
# # p2.put_data()
#
# #Question # 3
# class disk(Publication):
#     def __init__(self,title,price):
#         Publication.__init__(self, title, price)
#         self.diskType = None
#
#     def get_diskType(self):
#         print('input c for CD and d for DVD')
#         user = input('Enter the type of disk CD or DVD\n>>>')
#         ui = user.lower()
#         d = {'c':'CD' , 'd':'DVD'}
#         self.diskType =  d[ui]
#
#     def put_disktype(self):
#         print ('the book of',self.diskType,'type is available')
#
# ob = disk('alchemist',400)
# ob.show_data()
# ob.get_diskType()
# ob.put_disktype()

##ques 6
# class Date:
#     def __init__(self,m=7,d=20,y=2020):
#         self.day = int(d)
#         self.month = int(m)
#         self.year = int(y)
#
#     def set_date(self,m,d,y):
#         self.month = int(m) # issue of entering single value
#         self.day = int(d)
#         self.year = int(y)
#
#     def get_date(self):
#         print(self.day,'-',self.month,'-',self.year)
#     def __add__(self, d2):
#         pass



    # def __str__(self):
#     #     return(self.day+'-'+self.month+'-'+self.year)
# p1 = Date()
# print(p1)
# p1.set_date(23,12,2000)
# p1.get_date()
# s1=Date(2,9,20)
# print(s1)

##ques 7
# class Date:
#     def __init__(self,d=20,m=7,y=2020):
#         self.day = '0'+str(d)
#         self.month = '0'+str(m)
#         self.year = '0'+str(y)
#
#     def set_date(self,d,m,y):
#         f = int(input('enter format value you want\n>>>'))
#         self.format = f
#         self.day = '0'+str(d)
#         self.month = '0'+str(m) # issue of entering single value
#         self.year = str(y)
#
#     def get_date(self):
#         if self.format == 1:
#             return(self.day[-2:]+'-'+self.month[-2:]+'-'+self.year)
#         elif self.format == 2:
#             return(self.month[-2:]+'-'+self.day[-2:]+'-'+self.year)
#         else:
#             print('for this enter month name')
#             name = input('>>>')
#             return (self.month[-2:]+'_'+name+'-'+self.day[-2:]+'-'+self.year)
#     def __str__(self):
#         return ('what interface you want!'
#                 '\n1. dd/mm/yy'
#                 '\n2. mm/dd/yy'
#               '\n3. mm_name/dd/yy')

# s1=Date(12,9,20)
# print(s1)
# s1.set_date(3,2,20)
# s1.get_date()

#ques # 8 & 9
#uncomment Date class to run this test code
# class Publication(Date):
#     countBook = 0
#     countTape = 0
#     def __init__(self,title,price):
#         super().__init__(self)
#         self.title = title
#         self.price = float(price)
#
#     def show_data(self):
#         print('The title of book is',self.title, 'and its price is',self.price)
#     def get_date(self):
#         print('the publishing date of',self.title,super().get_date())


#
# class Book(Publication):
#     def __init__(self,title,price,pagecount=0):
#         Publication.__init__(self,title,price)
#         self.pagecount = pagecount
#         Publication.countBook += 1
#     def get_data(self):
#         pg = int(input('enter total pages of book\n>>> '))
#         self.pagecount += pg
#     def put_data(self):
#         print('the total pages are',self.pagecount)
#
# class Tape(Publication):
#     def __init__(self,title,price,t =0):
#         Publication.__init__(self, title, price)
#         self.time = t
#         Publication.countTape += 1
#     def get_data(self):
#         t = int(input('enter the time of book audio\n>>> '))
#         self.time += int(t)
#         return self.time
#     def put_data(self):
#         print ('the time of recording is',self.time,'minutes')
#
#
# s1 = Book('namal',500)
# r1 = Book('the girl on the train',250)
# p1 = Book('alchemist',300)
# print(p1)
# p1.set_date(2,3,20)
# p1.get_date()
# p1.show_data()
# p1.get_data()
# p1.put_data()
# s2 = Tape('namal',500)
# r2 = Tape('the girl on the train',250)
# p2 = Tape('alchemist',400)
# p2.get_data()
# p2.put_data()
# print(Publication.countTape)
# print((Publication.countBook))

#
# # Ques # 9
# class Vehicle():
#     def __init__(self,n=4,c='black',m='CE175'):
#         self.__noOfWheels = int(n)
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
# # p1 = Vehicle()
# # p1.set_noOfWheel(4)
# # print(p1.get_noOfWheel())
# # p1.set_color('turquiose')
# # print(p1.get_color())
# # p1.set_model('cor104')
# # print(p1.get_model())
#
# #(aggregation)
# class Engine:
#     def __init__(self,engNo = '1234',date='02-02-2020',n=None):
#         self.__EngineNo = engNo
#         self.__dateOfManufacture = date
#         self.new = n
#
#     def set_EngineNO(self,e):
#         self.__EngineNo = e
#     def get_EngineNo(self):
#         return self.__EngineNo
#     def set_DateOfManufacture(self,d):
#         self.__dateOfManufacture = d
#     def get_DateOfManufacture(self):
#         return self.__dateOfManufacture
# #
# a1 = Engine()
# a2 = Vehicle()
# a1.new = a2
# print(a1)
# print(a1.new.get_noOfWheel())
# print(a1.new.get_color())
# print(a1.new.get_model())
# a1.set_EngineNO('12345')
# print(a1.get_EngineNo())
# a1.set_DateOfManufacture('12-09-2001')
# print(a1.get_DateOfManufacture())
# #
# #
# class engine: ##(composition)
#     def __init__(self,engNo = '1234',date='02-02-2020'):
#         self.__EngineNo = engNo
#         self.__dateOfManufacture = date
#         self.vehicle = Vehicle()
#
#     def set_EngineNO(self,e):
#         self.__EngineNo = e
#     def get_EngineNo(self):
#         return self.__EngineNo
#     def set_DateOfManufacture(self,d):
#         self.__dateOfManufacture = d
#     def get_DateOfManufacture(self):
#         return self.__dateOfManufacture
#
#     def __str__(self):
#         return '<Class Vehicle>\n<modelNo:'+str(self.vehicle.get_model())+'>\n'+'<noOfWheel :'+str(self.vehicle.get_noOfWheel())+'>\n'+'<color:'+self.vehicle.get_color()+'>\n'+'<DateOfManufacture:'+str(self.__dateOfManufacture)+'>'
# #
# a1 = engine()
# print(a1)
# a1.set_EngineNO('12345')
# print(a1.get_EngineNo())
# a1.set_DateOfManufacture('12-09-2001')
# print(a1.get_DateOfManufacture())
# print(a1.vehicle.get_model())
# print(a1.vehicle.get_noOfWheel())

#Write code to create a class called Time that has separate member data for hours, minutes, and seconds. Make
#constructor to initialize these attributes, with 0 being the default value. Override __str__ method to display time in
#11:59:59 format when the object is printed. Add another method addTime which takes one argument of Time type
#and add this time to the current time of the self object through + operator. Instantiate two objects t1 and t2 to any
#arbitrary values, display both the objects, add t2 to t1 and display the result.
# #
# class Time:
#     def __init__(self,h=0,m=0,s=0):
#         self.hour = h
#         self.min = m
#         self.second = s
#
#     def addTime(self,t1):
#         print('after adding time is:')
#         self.hour += t1.hour
#         self.min += t1.min
#         self.second += t1.second
#         if self.hour >= 24:
#             self.hour-=24
#         if self.min>=60:
#             self.min-=60
#             self.hour+=1
#         if self.second>=60:
#             self.second-=60
#             self.min+=1
#
#     def printTime(self):
#         self.newhour = str(self.hour)
#         self.newmin = str(self.min)
#         self.newsecond = str(self.second)
#         if self.hour<10:
#             self.newhour='0'+str(self.hour)
#         if self.min<10:
#             self.newmin='0'+str(self.min)
#         if self.second<10:
#             self.newsecond='0'+str(self.second)
#         print(self.newhour,':',self.newmin,':',self.newsecond,sep='')
# t1=Time(2,14,56)
# t1.printTime()
# t2=Time(6,46,55)
# t2.printTime()
# t1.addTime(t2)
# t1.printTime()

#Define a class called BasicSalary having one instance variable basic to store basic salary of an employee. Add
#appropriate __init__ method and another method annualBasicSalary which calculates and returns the sum
#of basic salaries for twelve months. Now define another class called Employee which instantiates an object of
#BasicSalary type in its __init__ method. It also instantiate an instance variable called annualBonus. Add a
#method annualNetSalary to Employee which returns the annual net salary of an employee including the annual
#basic and annual bonus.
# class BasicSalary:
#     def __init__(self):
#         self.basic = 100
#
#     def annualBasicSalary(self):
#         return 12*self.basic
# class Employee:
#     def __init__(self):
#         self.p1 = BasicSalary()
#         self.annualBonus = 1000
#     def annualNetSalary(self):
#         x = self.p1.annualBasicSalary()
#         return x + self.annualBonus
# o1 = Employee()
# print(o1.annualNetSalary())
#Define a class called Point that stores two coordinates of a 2D point. Add appropriate methods including initiator,
# #__str__ and setters. Add any other method if you want to.
# from math import sqrt
# class Point():
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#         self.l = []
#     def set_coord(self,x1,y1):
#         self.x = x1
#         self.y = y1
#         z= self.x,self.y
#         self.l.append(z)
#     def get_coord(self):
#         return self.x ,self.y
#
#     def __str__(self):
#         return "({0}, {1})".format(self.x, self.y)
# # # # p1 =Point(4,5)
# # # print(p1)

# # #To the Distance class developed in problem 19, add an overloaded - operator that subtracts two distances. It
# # #should allow statements like dist3= dist1-dist2. Assume that the operator will never be used to subtract a larger
# # #number from a smaller one (that is, negative distances are not allowed).
# from math import sqrt
# class Distance:
#     def __init__(self,p1=Point(2,3),p2=Point(3,3)):
#         self.p1 = p1
#         self.p2 = p2
#         self.d = 0
#     def set_p1(self,p1):
#         self.p1 = p1
#     def set_p2(self,p2):
#         self.p2=p2
#     def findDistance(self):
#          x = (self.p1.get_coord())
#          y = (self.p2.get_coord())
#          d= ((y[0]-x[0])**2) + ((y[1]-x[1])**2)
#          self.d=sqrt(d)
#          return self.d
#     def __sub__(self, other):
#         if self.d > other.d:
#             return self.d - other.d
#         else:
#             return('Negative distance is not allowed ')
# s = Distance()
# d1=(s.findDistance())
# print('distance 1: ',d1)
# r=Distance()
# r.set_p1(Point(5,4))
# r.set_p2(Point(2,3))
# d2=(r.findDistance())
# print('distance 2: ',d2)
# print(r-s)

# #
# # #Define a mix-in class DistanceFinder containing only one method findDistance(self,p). p is a Point
# #type value and the method returns the distance between self and p. Now link this class to Point class via
# #inheritance so that the current can find its distance from any other point.
# class DistanceFinder(Point):
#     def __init__(self,x=0,y=0):
#         super().__init__()
#         self.x = x
#         self.y = y
#     def findDistance(self,p):
#         return (((self.x - p.x)**2) + ((self.y - p.y)**2)**0.5)
# # p1=DistanceFinder(2,4)
# # p2=DistanceFinder(2,5)
# # print(p1.findDistance(p2))


#Add to the Time class of problem 16 the ability to subtract two time values using the overloaded - operator, and to
#multiply a time value by a number of type float, using the overloaded * operator. The float should be multiplied by
#the hours component; if the hour component is 0, the float should be multiplied by the minute component; and if the
#minute component is also zero then the float should be multiplied by the second component.
# class Time:
#    def __init__(self, h=0, m=0, s=0):
#        self.hour=h
#        self.minute=m
#        self.second=s
#
#    def addTime(self,t):
#        self.second+=t.second
#        if self.second>=60:
#            self.second-=60
#            self.minute+=1
#        self.minute+=t.minute
#        if self.minute>=60:
#            self.minute-=60
#            self.hour+=1
#        self.hour+=t.hour
#        if self.hour>=24:
#            self.hour-=24
#
#    def __sub__(self, t):
#        if self.second > t.second:
#             self.second -= t.second
#             if self.second >= 60:
#                 self.second -= 60
#                 self.minute += 1
#        else:
#            new = t.second-self.second
#            self.second = 60 - new
#        if self.minute > t.minute:
#             self.minute -= t.minute
#             if self.minute >= 60:
#                 self.minute -= 60
#                 self.hour += 1
#        else:
#            new = t.minute-self.minute
#            self.minute = 60 - new
#        if self.hour >t.hour:
#           self.hour -= t.hour
#           if self.hour >= 24:
#               self.hour -= 24
#        else:
#            new = t.hour-self.hour
#            self.hour = 24 - new
#
#
#    def printTime(self):
#        finalhour = str(self.hour)
#        finalminute = str(self.minute)
#        finalsecond = str(self.second)
#        if self.hour < 10:
#            finalhour = '0' + str(self.hour)
#        if self.minute < 10:
#            finalminute = '0' + str(self.minute)
#        if self.second < 10:
#            finalsecond = '0' + str(self.second)
#        print('current time ', finalhour, ':', finalminute, ':', finalsecond, sep='')
#
#    def __mul__(self, t):
#         if self.hour!=0:
#             self.hour*=t
#         else:
#             if self.minute!=0:
#                 self.minute*=t
#             else :
#                 if self.second!=0:
#                     self.second*=t
# t1=Time(23,44,30)
# t2=Time(2,4,30)
# t1.addTime(t2)
# t1.printTime()
# t3=Time(2,15,12)
# t4=Time(4,30,11)
# t3-t4
# t3.printTime()
# (t3*2)
# t3.printTime()

#Define a class Fraction which stores a fraction in two instance variables: numerator and denominator. Define
#appropriate initiator, setters and print methods. Override the following operators: +, -, *, /, >, <, >=, <=, ==, and
#!=. Add another method simplify to simplify the fraction. You overloaded arithmetic methods should return a
#simplified fraction.
# class Fraction:
#     def __init__(self,n=0,d=0):
#         self.numerator = n
#         self.dinominator = d
#     def setNumerator(self,n):
#         self.numerator = n
#     def setDinominator(self,d):
#         if d!=0:
#             self.dinominator = d
#         else:
#             print('Invalid value , setting to 1 instead')
#             self.dinominator = 1
#
#     def __str__(self):
#         return str(self.numerator)+'/'+str(self.dinominator)
#     def convertDecimal(self):
#         return self.numerator/self.dinominator
#     def __add__(self, f2):
#         if isinstance(f2,Fraction):
#             return (self.numerator*f2.dinominator\
#             +f2.numerator*self.dinominator)\
#             /(self.dinominator*f2.dinominator)
#         else:
#             return 'Wrong Argument , only fraction allowed'
#     def __sub__(self, f2):
#         if isinstance(f2,Fraction):
#             return (self.numerator*f2.dinominator\
#             -f2.numerator*self.dinominator)\
#             /(self.dinominator*f2.dinominator)
#         else:
#             return 'Wrong Argument , only fraction allowed'
#     def __gt__(self, f2):
#         if isinstance(f2,Fraction):
#             return self.numerator*f2.numerator\
#                 >f2.numerator*self.dinominator
#         else:
#             return 'Wrong argument , only fraction allowed'
#     def __mul__(self, f2):
#         if isinstance(f2,Fraction):
#             return self.numerator*f2.numerator\
#                 /f2.dinominator*self.dinominator
#         else:
#             return 'Wrong argument , only fraction allowed'
#     def __truediv__(self, f2):
#         if isinstance(f2,Fraction):
#             return (self.numerator*f2.dinominator)\
#                 /(self.dinominator*f2.numerator)
#         else:
#             return 'Wrong argument , only fraction allowed'
#     def simplify(self):
#         HCF = Fraction.findHCF(self.numerator,self.dinominator)
#         self.numerator = int(self.numerator/HCF)
#         self.dinominator = int(self.dinominator/HCF)
#     def findHCF(a,b):
#         factors_a = Fraction.findFactors(a)
#         factors_b = Fraction.findFactors(b)
#         for i in range(len(factors_a)-1,-1,-1):
#             if factors_a[i] in factors_b:
#                 return factors_a[i]
#     def findFactors(x):
#         factors = []
#         for i in range(1,x+1):
#             if x%i==0:
#                 factors.append(i)
#         return factors
#
# f1 = Fraction(2,4)
# f2 = Fraction(2,4)
# f1.simplify()
# print(f1)
# print(f1-f2)
# print(f1+f2)
# print(f1*f2)
# print(f1/f2)

#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"<{self.x}, {self.y}>"
#
#     def setX(self, x):
#         self.x = x
#
#     def setY(self, y):
#         self.y = y
#
#
# class Polygon(Point):
#     def __init__(self):
#         super().__init__(x=0,y=0)
#         self.points = []
#
#     def addPoint(self, x, y):
#         self.points.append(Point(x, y))
#
#     def perimeter(self):
#         p = 0
#         for i in range(0, len(self.points) - 1):
#             p += Polygon.distance(self.points[i], self.points[i + 1])
#         p += Polygon.distance(self.points[len(self.points) - 1], self.points[0])
#         return p
#
#     def distance(p1, p2):
#         return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
# p1 = Polygon()
# triangle=(1,0), (2,2), (3,0)
# p1.addPoint(1,0)
# p1.addPoint(2,2)
# p1.addPoint(3,0)
# print(p1.perimeter())

##Q26
# class PhysicalObject:
#     def __init__(self):
#         super().__init__()
#         print('I\'m class Physical Object')
# class Vehicle(PhysicalObject):
#     def __init__(self):
#         super().__init__()
#         print('I\'m class Vehicle')
# class GroundVehicle(Vehicle):
#     def __init__(self):
#         super().__init__()
#         print('I\'m class Ground vehicle')
# class FlyingVehicle(Vehicle):
#     def __init__(self):
#         super().__init__()
#         print('I\'m class flyingvehicle')
# class FuelTrack(GroundVehicle):
#     def __init__(self):
#         super().__init__()
#         print('I\'m class Fuel Track')
# class AirCraft(GroundVehicle,FlyingVehicle):
#     def __init__(self):
#         super().__init__()
#         print('I\'m class AircraFT')
# class CommercialAircraft(AirCraft):
#     def __init__(self):
#         super().__init__()
#         print('I\'m class Commercial Aircraft')
# class Boeing707(CommercialAircraft):
#     def __init__(self):
#         super().__init__()
#         print('I\'m class Boeing707')
# p1 = FlyingVehicle()

## Question 26
class fancyPrint:
    message = ''
    def setMessage(self,msg):
        fancyPrint.message = msg
    @staticmethod
    def fancyprint():
        print(fancyPrint.message.upper())

    def makeFancy(fancyprint):
        def wrapper():
            print('********************')
            fancyPrint.fancyprint()
            print('******************')
            print('**************')
            print('**********')
        return wrapper
    fancyPrint = makeFancy(fancyprint)

mssg = fancyPrint()
mssg.setMessage('Congratulations!!!')
fancyPrint.fancyPrint()


