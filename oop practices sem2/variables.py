###Slide 5, 6, 7
##
##class Point:
##    def __init__(self,xcoord=0,ycoord=0):
##        self.x=xcoord
##        self.y=ycoord
##    def setx(self,xcoord):
##        self.x=xcoord
##    def sety(self,ycoord):
##        self.y=ycoord
##    def get(self):
##        return self.x, self.y
##    def move(self, dx, dy):
##        self.x+=dx
##        self.y+=dy
##
##p1=Point(1,5)
##print(p1.get( ))
##print(p1.__dict__)
##p1.setx(4)
##p1.sety(7)
##print(p1.get( ))
##p1.move(1,1)
##print(p1.get( ))
##print(p1.__dict__)



#Slide 8, 9
#
# class Point:
#    def __init__(self,xcoord=0,ycoord=0):
#        self.__x=xcoord
#        self.__y=ycoord
#    def setx(self,xcoord):
#        self.__x=xcoord
#    def sety(self,ycoord):
#        self.__y=ycoord
#    def get(self):
#        return self.__x, self.__y
#    def move(self, dx, dy):
#        self.__x+=dx
#        self.__y+=dy
#
# p1=Point()
# print(p1.get( ))
# print(p1.__dict__)
# p1.__x=4
# print(p1.__dict__)

###Slide 10-13
##
# from datetime import datetime
# class Time:
#    def __init__(self, h=0, m=0, s=0):
#        self.hour=(h)
#        self.minute=(m)
#        self.second=(s)
#    def printTime(self):
#        hour = '0'+str(self.hour)
#        minute = '0'+str(self.minute)
#        second = '0'+str(self.second)
#        print(hour[-2:],':',minute[-2:],':',second[-2:],sep='')
#    def addTime(self,t):
#        self.second+=t.second
#        if self.second>=60:
#            self.second-=60
#            self.minute+=1
#
#        self.minute+=t.minute
#        if self.minute>=60:
#            self.minute-=60
#            self.hour+=1
#        self.hour+=t.hour
#        if self.hour>=24:
#            self.hour-=24
#
# t1=Time(23,44,30)
# t1.printTime()
# t2=Time(2,4,30)
# t2.printTime()
# t1.addTime(t2)
# t1.printTime()

# datetime.timedelta(x)
###Slide 10, 11
##
# class Animal:
#    def __init__(self, s='animal', l='talk'):
#        self.specie=s
#        self.language=l
#    def info(self):
#        print('Specie:',self.specie,'\nLanguage:',self.language)
#    def speak(self):
#        print('I am a', self.specie,'and I can',self.language)
#
# class Duck(Animal):
#    pass
#
# tom=Animal('cat','meow')
# tom.info()
# tom.speak()
# daffy=Duck('duck','quack')
# daffy.info()
# daffy.speak()


###Slide 12, 13, 14
##
##class Animal:
##    def __init__(self, s='animal', l='talk'):
##        self.specie=s
##        self.language=l
##    def info(self):
##        print('Specie:',self.specie,'\nLanguage:',self.language)
##    def speak(self):
##        print('I am a', self.specie,'and I can',self.language)
##
##class Duck(Animal):
##    def setBeakType(self, b='short'):
##        self.beakType=b
##tom=Animal('cat','meow')
##tom.info()
##tom.speak()
##daffy=Duck('duck','quack')
##daffy.setBeakType('long and curved')
##daffy.info()
##daffy.speak()
##print('\n',dir(tom))
##print('\n',dir(daffy))
##tom.setBeakType()



###Slide 15, 16
##
##class Animal:
##    def __init__(self, s='animal', l='talk'):
##        self.specie=s
##        self.language=l
##    def info(self):
##        print('Specie:',self.specie,'\nLanguage:',self.language)
##    def speak(self):
##        print('I am a', self.specie,'and I can',self.language)
##
##class Duck(Animal):
##    def setBeakType(self, b='short'):
##        self.beakType=b
##    def speak(self):
##        print('quack! quack!! quack!!!')
##
##
##tom=Animal('cat','meow')
##tom.info()
##tom.speak()
##daffy=Duck('duck','quack')
##daffy.setBeakType('long and curved')
##daffy.info()
##daffy.speak()



###Slide 17, 18
##
##class Animal:
##    def __init__(self, s='animal', l='talk'):
##        self.specie=s
##        self.language=l
##    def info(self):
##        print('Specie:',self.specie,'\nLanguage:',self.language)
##    def speak(self):
##        print('I am a', self.specie,'and I can',self.language)
##
##class Duck(Animal):
##    def setBeakType(self, b='short'):
##        self.beakType=b
##    def info(self):
##        print('Specie:',self.specie,'\nLanguage:',self.language, '\nBeak type:',self.beakType)
##    def speak(self):
##        print('quack! quack!! quack!!!')
##
##
##tom=Animal('cat','meow')
##tom.info()
##tom.speak()
##daffy=Duck('duck','quack')
##daffy.setBeakType('long and curved')
##print(daffy.__dict__)
##daffy.info()
##daffy.speak()

###Slide 14-15
##
# class Tracker:
#    count=0
#
#    def __init__(self):
#        self.serialNo=Tracker.count+1
#        Tracker.count+=1
#    def reportSerial(self):
#        print('I am object number',self.serialNo)
#
#
# n1=Tracker()
# n2=Tracker()
# n3=Tracker()
# n1.reportSerial()
# n2.reportSerial()
# n3.reportSerial()
# print(n1.__dict__)
# print(n2.__dict__)

############## inheritance lecture 11 #############
# class Animal:
#     def __init__(self,s='Animal',l='talk'):
#         self.specie = s
#         self.language = l
#     def info(self):
#         print('specie:',self.specie ,'\nlanguage:',self.language)
#     def speak(self):
#         print('I am a',self.specie,'and I can',self.language)
#
# class Duck(Animal):
#     def __init__(self,s,l,b='long'):
#         super().__init__(s,l)
#         self.beaktype = b
#     def info(self):
#         super().info()
#         print('beaktype:',self.beaktype)
#     def speak(self):
#         print('quack!quack!!quack!!!')
# p1=Duck('duck','quack','sharp')
# p1.info()
# p1.speak()

########### str method #########
# class representation:
#     def __str__(self):
#         print('good string representation')
# p1=representation()
# print(p1)


class Animal:
    def __init__(self,s='Animal',l='talk'):
        self.__specie = s
        self.__language = l
    def __str__(self):
        return '<'+self.__specie+', '+self.__language+'>'
    def info(self):
        print('specie:',self.__specie ,'\nlanguage:',self.__language)
    def speak(self):
        print('I am a',self.__specie,'and I can',self.__language)

class Duck(Animal):
    def __init__(self,s='Animal',l='talk',b='long'):
        Animal.__init__(self,s,l)
        self.beaktype = b
    def __str__(self):
        return '<'+self.__specie+', '+self.__language+', '+self.beaktype+'>'
    def info(self):
        super().info()
        print('beaktype:',self.beaktype)
    def speak(self):
        print('quack!quack!!quack!!!')

a1 = Animal()
a1.info()
a1.speak()
print(a1)
a2=Duck()
print(a2)


#Slide 17

# class Animal:
#    def __init__(self, s='animal', l='talk'):
#        self.specie=s
#        self.language=l
#    def __str__(self):
#        return '<'+self.specie+', '+self.language+'>'
#    def info(self):
#        print('Specie:',self.specie,'\nLanguage:',self.language)
#    def speak(self):
#        print('I am a', self.specie,'and I can',self.language)
#
# tom = Animal()
# print(tom)
# print(type(tom))
#
# print(Animal)
# print(type(Animal))
#
# print(isinstance(tom, Animal))