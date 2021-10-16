## Question  :03

# class two_init:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#     def __init__(self,x,y):
#         self.x =x
#         self.y =y
# p1 = two_init()
# print(p1.x)
# print(p1.y)
# the second initializer run in python , if we didnt give any value so we havw two choice
# either to change the position of two initializer or to give user defined perimeter

## question 4
# class variable:
#     def __init__(self,x=2):
#         self.x = 0
#         self.x =x
# p1 = variable()
# print(p1.x)

# class Bank:
#     loan_take_previously = True
#     def application_for_loan(self):
#         if Bank.loan_take_previously == False:
#             print('loan granted')
#         else:
#             print('loan is not granted')
# p1 =Bank()
# p1.application_for_loan()
# p1.loan_take_previously = False
# p1.application_for_loan()
# import datetime
# x = datetime.datetime.now()
# y=x.strftime("%d")
# print(y)
# z = datetime.date(2020,8,12)
# v = z.strftime("%d")
# print(v)
# print(int(y)-int(v))
# class MyStudent:
#     name = None
#     roll_no = None
#     email = None
#     count = 0
#     def std_info(self):
#         MyStudent.name = input('Enter your name...')
#         MyStudent.roll_no = int(input('Enter your roll no...'))
#         MyStudent.email = input('Enter your email...')
#     def GPa(self,l=[]):
#         self.cdp = []
#         self.GPA = []
#         d = {'A':4,'B':3,'C':2}
#         for i in range (len(l)):
#             self.user = input(f'Enter your {l[i]}  grade ')
#             self.cd = int(input(f'Enter your {l[i]}  cdp point '))
#             self.cdp.append(self.cd)
#             y = d.get(self.user)
#             self.GPA.append(y)
#             print(f'The GPa of {l[0]} is {y}')
#     def CGPA(self):
#         total = 0
#         for j in range (len(self.GPA)):
#             total += self.cdp[j]*self.GPA[j]
#         self.cgpa = total/(sum(self.cdp))
#         print(f'The CGPA of this semester is {self.cgpa}')
#     @classmethod
#     def classMethod(cls):
#         print(f'name : {cls.name}\nroll_no: {cls.roll_no}\nemail: {cls.email}')
#     @staticmethod
#     def course_info():
#         l=[]
#         no = int(input('Enter no of courses...'))
#         MyStudent.count = no
#         for i in range (no):
#             x = input('Enter the name of course')
#             l.append(x)
#         return l
#
# a1 = MyStudent()
# a1.std_info()
# MyStudent.classMethod()
# l =MyStudent.course_info()
# print(l)
# a1.GPa(l)
# a1.CGPA()

# import datetime as dt
# class date:
#     def __init__(self):
#         self.due_day = 0
#     def issue_date(self):
#         self.creation_date = dt.datetime.now()
#         print('the book issued on', self.creation_date)
#     def due_date(self):
#         self.today =self.creation_date.strftime('%d')
#         month =self.creation_date.strftime('%m')
#         if int(self.today) > 20 :
#             if int(month)%2 == 0:
#                 due = 30 - int(self.today)
#                 self.due_day = 10 - due
#             elif int(month)%2 != 0:
#                 due = 31 - int(self.today)
#                 self.due_day = 10 - due
#         else:
#             self.due_day = int(self.today) + 10
#         print('you have 10 days to return the book')
#         return self.due_day
#     def check_fine(self):
#         print('Welcome !!! Now you can return the book')
#         day = int(input('Enter today day no of local format'))
#         if int(self.today)<=day or day<=self.due_day:
#             print('no fine')
#         else:
#             print('you run out of day , You have to pay of 50 Rs for fine')
#
#
# p1=date()
# p1.issue_date()
# print(p1.due_date())
# p1.check_fine()



#
# dd=dt.datetime(2020,9,4)
# print(dd)
# dued = dd.strftime('%d')
# print(dued)
# class Hospital:
#     def __init__(self,n,a):
#         self.name = n
#         self.address = a
#
# class Doctor(Hospital):
#     def __init__(self,n=None,a=None,s=None):
#         super().__init__(n,a)
#         self.specialization = s
#
# class Patient(Hospital):
#     def __init__(self,n=None,a=None,d=None):
#         super().__init__(n,a)
#         self.disease = d
# class medical_test:
#     def __init__(self,p,d):
#         self.p = p
#         self.d = d
#     def medical_info(self):
#         return (f'The medical test of {self.p.disease} is done')
#     def all_info(self):
#         print(f'Doctor: {self.d.name} \nPatient: {self.p.name} \nmedical info: {self.medical_info()}')
#
# h = Hospital('Ziauddin Hosputal','F.B Area')
# d = Doctor('Rafique','Shadman','Technition')
# p = Patient('ABC','Gulshan','Dilated cardiomyopathy')
# m = medical_test(p,d)
# m.all_info()

# ##
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

#### Question # 3
# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     def __init__(self,n,s):
#         self.noOfWheel = n
#         self.speed = s
#     @abstractmethod
#     def same_info(self):
#         print('I have wheels and  variable speed ')
#     @abstractmethod
#     def print_func(self):
#         pass
# class Truck(vehicle):
#     def __init__(self,n,s,f,a):
#         super().__init__(n,s)
#         self.fuel = f
#         self.space =a
#     def same_info(self):
#         super().same_info()
#         print(f'I have {self.noOfWheel} wheels')
#         print(f'I have {self.speed} speed')
#     def fuel(self):
#         print(f'I have {self.fuel} fuel')
#     def accomodation(self):
#         print(f'I have {self.space} to accomodate')
#     def print_func(x):
#         return x()
# class Cycle(vehicle):
#     def __init__(self,n,s,b,h):
#         super().__init__(n,s)
#         self.brake = b
#         self.horn =h
#     def same_info(self):
#         super().same_info()
#         print(f'I have {self.noOfWheel} wheels')
#         print(f'I have {self.speed} speed')
#
#     def brake(self):
#         return(self.brake)
#
#     def horn(self):
#         return(f'I have {self.horn} to give a signal to padestarian ')
# def print_func(x):
#     return x.same_info()
#
# t = Truck(4,'20m/s','CNG','seven')
# c = Cycle(2,'2m/s','handbreak','horn bell')
# print_func(t)
# print_func(c)
#
#
# def user_dic():
#     with open('user_log', 'r') as f:
#         value = f.read()
#         v1 = value.split(',')
#         print(v1)
#         n = v1[-2]
#         n = n.split(' ')
#         print(n)
# user_dic()
# def idd():
#     with open('user_login', 'r') as f:
#         x = f.readlines()
#         print(x)
#         if x == []:
#             print('id is 0')
#         else:
#             print(x[-1][0])
# idd()
# # l=[1]
# (print(l[-1]))
# def USER_LOG():
#     d={}
#     with open('user_login', 'r') as f:
#         x = f.readlines()
#         for i in x:
#             y = i.strip('\n')
#             d[i[0]]=i[1:-2]
#         print(d)
# USER_LOG()
with open('user_history', 'r') as f:
    d={}
    x = len(f.readlines())
    f.seek(0)
    for i in range (x) :
        v=f.readline()
        v1 = v.split(',')
        d[v1[0]]=v1[1:-2]
print(d)


