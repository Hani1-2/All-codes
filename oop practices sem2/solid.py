

###Slide 7
#class Circle:
#    def __init__(self,r=0):
#        self.radius=r
#    def findArea(self):
#        return 3.14*self,radius**2
#    def displayArea(self):
#        print('Area:',self.findArea())
#    def saveToFile(self):
#        f=open('area.txt','w')
#        f.write(str(self.findArea()))
#        f.close()



###Slide 8
##
#class Circle:
#    def __init__(self,r=0):
#        self.radius=r
#    def findArea(self):
#        return 3.14*self,radius**2
#class DisplayCircle(Circle):
#    def __init__(self,a):
#        self.area=a
#    def displayArea(self):
#        print('Area:',self.area())
#    def saveToFile(self):
#        f=open('area.txt','w')
#        f.write(str(self.area()))
#        f.close()



##Slide 10
#
#class Shape:
#    def __init__(self,r=0):
#        self.radius=r
#    def findArea(self):
#        return 3.14*self,radius**2
#    def findAreaRectangle(self, l, w):
#        return



##Slide 11
#
#class Rectangle(Shape):
#    def __init__(self,l=0,w=0):
#        self.length=l
#        self.width=w
#    def findArea(self):
#        return self.length*self.width



##Slide 12
#
#from abc import ABC,abstractmethod
#class Shape(ABC):
#    @abstractmethod
#    def setDimensions(self):
#        pass
#    @abstractmethod
#    def findArea(self):
#        pass
#class Circle(Shape):
#    def setDimensions(self,r):
#        self.radius=r
#    def findArea(self):
#        return 3.14*self.radius**2
#class Rectangle(Shape):
#    def setDimensions(self,l,w):
#        self.length=l
#        self.width=w
#    def findArea(self):
#        return self.length*self.width



##Slide 15
#
#from abc import ABC,abstractmethod
#class Shape(ABC):
#    @abstractmethod
#    def setDimensions(self):
#        pass
#    @abstractmethod
#    def findArea(self):
#        pass
#class Rectangle(Shape):
#    def setDimensions(self,l,w):
#        self.length=l
#        self.width=w
#    def findArea(self):
#        return self.length*self.width
#class Square(Rectangle):
#    def setDimensions(self,l):
#        self.length=l
#    def findArea(self):
#        return self.length*2



##Slide 16
#
#from abc import ABC,abstractmethod
#class Shape(ABC):
#    @abstractmethod
#    def setDimensions(self):
#        pass
#    @abstractmethod
#    def findArea(self):
#        pass
#class Rectangle(Shape):
#    def setDimensions(self,l,w):
#        self.length=l
#        self.width=w
#    def findArea(self):
#        return self.length*self.width
#class Square(Shape):
#    def setDimensions(self,l):
#        self.length=l
#    def findArea(self):
#        return self.length*2



#Slide 18
#
#from abc import ABC,abstractmethod
#class Shape(ABC):
#    @abstractmethod
#    def setDimensions(self):
#        pass
#    @abstractmethod
#    def findArea(self):
#        pass
#    @abstractmethod
#    def findPerimeter(self):
#        pass
#class Rectangle(Shape):
#    def setDimensions(self,l,w):
#        self.length=l
#        self.width=w
#    def findArea(self):
#        return self.length*self.width
#    def findPerimeter(self):
#        return 2*(self.length+self.width)
#class Circle(Shape):
#    def setDimensions(self,r):
#        self.radius=r
#    def findArea(self):
#        return 3.14*self.radius**2
#    def findPerimeter(self):
#        return 2*3.14*self.radius



#Slide 19
#
#from abc import ABC,abstractmethod
#class Shape(ABC):
#    @abstractmethod
#    def setDimensions(self):
#        pass
#    @abstractmethod
#    def findArea(self):
#        pass
#    @abstractmethod
#    def findPerimeter(self):
#        pass
#class Perimeterized(ABC):
#    @abstractmethod
#    def findPerimeter(self):
#        pass
#class Circumferenced(ABC):
#    @abstractmethod
#    def findCircumference(self):
#        pass
#class Rectangle(Shape,Perimeterized):
#    def setDimensions(self,l,w):
#        self.length=l
#        self.width=w
#    def findArea(self):
#        return self.length*self.width
#    def findPerimeter(self):
#        return 2*(self.length+self.width)
#class Circle(Shape,Cicumferenced):
#    def setDimensions(self,r):
#        self.radius=r
#    def findArea(self):
#        return 3.14*self.radius**2
#    def findCircumference(self):
#        return 2*3.14*self.radius



##Slide 22
#
#class NewsPaper:  #low level module
#    def printInPaper(self,news='',time=''):
#        print('Printing in',time,'newspaper...')
#        print(news)
#class Facebook:  #low level module
#    def postOnFacebook(self,news=''):
#        print('Posting on Facebook...')
#        print(news)
#class FrontEnd: #high level module
#    def __init__(self):
#        ##n=NewsPaper()
#        ##n.printInPaper('Raining heavily today','evening')
#        f=Facebook()
#        f.postOnFacebook('Raining heavily today')
#
#FrontEnd()



##Slide 23,24
#
#class Publisher:
#    def publish(self,news='',time='',medium=None):
#        medium.publishIt(news,time)
#class NewsPaper:  #low level module
#    def publishIt(self,n,t):
#        self.printInPaper(n,t)
#    def printInPaper(self,news,time):
#        print('Printing in',time,'newspaper...')
#        print(news)
#class Facebook:  #low level module
#    def publishIt(self,n,t):
#        self.postOnFacebook(n)
#    def postOnFacebook(self,news):
#        print('Posting on Facebook...')
#        print(news)
#class FrontEnd: #high level module
#    def __init__(self):
#        p=Publisher()
#        #p.publish('Raining heavily today','evening',medium=NewsPaper())
#        p.publish('Raining heavily today',medium=Facebook())
#
#FrontEnd()



##Slide 24; making publish method static
#
#class Publisher:
#    @staticmethod
#    def publish(news='',time='',medium=None):
#        medium.publishIt(news,time)
#class NewsPaper:  #low level module
#    def publishIt(self,n,t):
#        self.printInPaper(n,t)
#    def printInPaper(self,news,time):
#        print('Printing in',time,'newspaper...')
#        print(news)
#class Facebook:  #low level module
#    def publishIt(self,n,t):
#        self.postOnFacebook(n)
#    def postOnFacebook(self,news):
#        print('Posting on Facebook...')
#        print(news)
#class Television:
#    def publishIt(self,n,t):
#        self.announceOnTV(n)
#    def announceOnTV(self,news):
#        print('Announcing on TV...')
#        print(news)
#class FrontEnd: #high level module
#    def __init__(self):
#        Publisher.publish('Raining heavily today','evening',medium=NewsPaper())
#        #Publisher.publish('Raining heavily today',medium=Facebook())
#        Publisher.publish('Raining heavily today',medium=Television())
#
#FrontEnd()



##Slide 24; making Publisher class abstract
#
#class Publisher:
#    @staticmethod
#    def publish(news='',time='',medium=None):
#        try:
#            medium.publishIt(news,time)
#        except AttributeError:
#            print('Medium is not suitable')
#class NewsPaper:  #low level module
#    def publishIt(self,n,t):
#        self.printInPaper(n,t)
#    def printInPaper(self,news,time):
#        print('Printing in',time,'newspaper...')
#        print(news)
#class Facebook:  #low level module
#    def publishIt(self,n,t):
#        self.postOnFacebook(n)
#    def postOnFacebook(self,news):
#        print('Posting on Facebook...')
#        print(news)
#class Television:
#    def publishIt(self,n,t):
#        self.announceOnTV(n)
#    def announceOnTV(self,news):
#        print('Announcing on TV...')
#        print(news)
#class FrontEnd: #high level module
#    def __init__(self):
#        Publisher.publish('Raining heavily today','evening',medium=NewsPaper())
#        Publisher.publish('Raining heavily today',medium=Facebook())
#        Publisher.publish('Raining heavily today',medium=Television())
#        Publisher.publish('Raining heavily today',medium=list())
#
#FrontEnd()



##Slide
#
#from abc import ABC,abstractmethod
#class Publisher(ABC):
#    @staticmethod
#    @abstractmethod
#    def publish(news='',time='',medium=None):
#        try:
#            if isinstance(medium,Publisher):
#                medium.publishIt(news,time)
#            else:
#                raise AttributeError
#        except AttributeError:
#            print('Medium is not suitable')
#class NewsPaper(Publisher):  #low level module
#    def publishIt(self,n,t):
#        self.printInPaper(n,t)
#    def printInPaper(self,news,time):
#        print('Printing in',time,'newspaper...')
#        print(news)
#class Facebook(Publisher):  #low level module
#    def publishIt(self,n,t):
#        self.postOnFacebook(n)
#    def postOnFacebook(self,news):
#        print('Posting on Facebook...')
#        print(news)
#class Television:
#    def publishIt(self,n,t):
#        self.announceOnTV(n)
#    def announceOnTV(self,news):
#        print('Announcing on TV...')
#        print(news)
#class FrontEnd: #high level module
#    def __init__(self):
#        Publisher.publish('Raining heavily today','evening',medium=NewsPaper())
#        Publisher.publish('Raining heavily today',medium=Facebook())
#        Publisher.publish('Raining heavily today',medium=Television())
#        Publisher.publish('Raining heavily today',medium=list())
#
#FrontEnd()