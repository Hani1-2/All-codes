###Slide 5, 6, 7
##
# class Point:
#    def __init__(self,xcoord=0,ycoord=0):
#        self.x=xcoord
#        self.y=ycoord
#    def setx(self,xcoord):
#        self.x=xcoord
#    def sety(self,ycoord):
#        self.y=ycoord
#    def get(self):
#        return self.x, self.y
#    def move(self, dx, dy):
#        self.x+=dx
#        self.y+=dy
#
# p1=Point(1,5)
# print(p1.get( ))
# print(p1.__dict__)
# p1.setx(4)
# p1.sety(7)
# print(p1.get( ))
# p1.move(1,1)
# print(p1.get( ))
# print(p1.__dict__)



###Slide 8, 9
##
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

# class Time:
#    def __init__(self, h=0, m=0, s=0):
#        self.hour=h
#        self.minute=m
#        self.second=s
#    def printTime(self):
#        print(self.hour,':', self.minute,':',self.second, sep='')
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
# t1=Time(23,44,30)
# t1.printTime()
# t2=Time(2,4,30)
# t2.printTime()
# t1.addTime(t2)
# t1.printTime()



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
# n1=Tracker()
# n2=Tracker()
# n3=Tracker()
# n1.reportSerial()
# n2.reportSerial()
# n3.reportSerial()
# print(n1.__dict__)
# print(n2.__dict__)
