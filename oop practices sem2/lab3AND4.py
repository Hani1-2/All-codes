# HANIYA MAQSOOD (CS-018)
# RUMAISA MARYAM (CS-024)
# HALEEMA AFSHAN (CS-023)
# LAB SESSION # 3 AND 4
# LAB 3 QUES # 1
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
# l = MyStudent.course_info()
# print(l)
# a1.GPa(l)
# a1.CGPA()

## LAB 3 QUESTION 2
# *******CLASS METHOD*******
# class method is basically used to access class attributes like name , roll no , email
# class method can be accessed outside the class by using class name
# class method can't access the instance attributes
#     @classmethod
#     def classMethod(cls):
#         print(f'name : {cls.name}\nroll_no: {cls.roll_no}\nemail: {cls.email}')

# ******STATIC METHOD*****
# Static methods are instance less methods , as we don't use any self in it
# Static method take no parameter like self or cls you can see below
# Static method provides utility to a class so we use this function to fin courses of Semester.
#     @staticmethod
#     def course_info():
#         l=[]
#         no = int(input('Enter no of courses...'))
#         MyStudent.count = no
#         for i in range (no):
#             x = input('Enter the name of course')
#             l.append(x)
#         return l

# ******INSTANCE METHOD*****
# Instance method must take an argument self ,
# so that it can easily access by the instance of a class.
# Instance methods can easily manipulate the class attribute
# Instance methods can be used within the class using self operator
# CGPA method is an instance method used in our class which can access the instance variable
# of cgpa and cdp points and GPA.
#     def CGPA(self):
#         total = 0
#         for j in range (len(self.GPA)):
#             total += self.cdp[j]*self.GPA[j]
#         self.cgpa = total/(sum(self.cdp))
#         print(f'The CGPA of this semester is {self.cgpa}')

# LAB 4 QUES 1
# class person:
#     def __init__(self,name='none'):
#         self.name=name
#     def getInfo(self):
#         return self.name
# class student(person):
#     def __init__(self,name='none',department='none',year=0):
#         self.name=name
#         self.department=department
#         self.year=year
#     def getInfo(self):
#         print (self.name , self.department,self.year)
# class teacher(person):
#     def __init__(self,name='none',course='none'):
#         self.name=name
#         self.course=course
#     def getInfo(self):
#         print( self.name,self.course)
#
# p1=person('Rumaisa')
# print(p1.getInfo())
# p2=student('Haniya','CIS',1)
# p2.getInfo()
# p3=teacher('Haleema','oop')
# p3.getInfo()

# lab 4 Ques 2
# class Bank_Account:
#     def __init__(self,account_number='none'):
#         self.AccountNumber=account_number
#     def getInfo(self):
#         return self.AccountNumber
# class Saving_Account(Bank_Account):
#     def __init__(self,minimum_balance=0,interest_rate=0):
#         self.MinimumBalance=minimum_balance
#         self.intersetRate=interest_rate
#     def getInfo(self):
#         print('Minimum Balance =',self.MinimumBalance,'Interest Rate=',self.intersetRate)
# class Current_Account(Bank_Account):
#     def __init__(self,withdrawl_limit=0):
#         self.Withdrawllimit=withdrawl_limit
#     def getInfo(self):
#         return self.Withdrawllimit
#
# p1=Bank_Account('123rm19')
# print(p1.getInfo())
# p2=Saving_Account(500,10)
# p2.getInfo()
# p3=Current_Account(1000000)
# print(p3.getInfo())

# QUESTION # 3
# class Employee:
#      def __init__(self,Employee_id,Employee_name,designation):
#           self.employeeid=Employee_id
#           self.employeename=Employee_name
#           self.designation=designation
#      def getInfo(self):
#           return("Employee_id:"+" "+ str(self.employeeid)+"\nEmployee_name:"+" "+self.employeename+"\nDesignation:"+" "+self.designation)
# class Manager(Employee):
#      def __init__(self,name):
#           self.name=name
#      def getInfo(self):
#           return self.name
# class Team_lead(Employee):
#      def __init__(self,leadername):
#           self.lname=leadername
#      def getInfo(self):
#           return self.lname
# class Clerk(Employee):
#      def __init__(self,clerk="clerk"):
#           self.clerk=clerk
#      def getInfo(self):
#           return self.clerk
# e=Employee(12345,"Haroon","Executive")
# print(e.getInfo())
# m=Manager("Hassan")
# print(m.getInfo())
# t=Team_lead("Muskan")
# print(t.getInfo())
# c=Clerk()
# print(c.getInfo())









