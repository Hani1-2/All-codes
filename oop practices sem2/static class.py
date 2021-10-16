###Slide 8,9,10
##
##class myClass:
##    classAttribute='ClassAttribute'
##    def __init__(self):
##        self.instanceAttribute='InstanceAttribute'
##    def instanceMethod(self):
##        print(myClass.classAttribute)
##        print(self.instanceAttribute)
##        print('This is an instance method')
##    @classmethod
##    def classMethod(cls):
##        print(cls.classAttribute)
##        #print(self.instanceAttribute) #error
##        #print(cls.instanceAttribute) #error
##        print('This is a class method')
##    @staticmethod
##    def staticMethod():
##        print(myClass.classAttribute)
##        #print(self.instanceAttribute) #error
##        #print(cls.instanceAttribute) #error
##        print('This is a static method')
##    def anotherMethod(self):
##        self.instanceMethod() 
##        myClass.classMethod() #can be accessed using self too but doesn't make sense that way
##        myClass.staticMethod() #can be accessed using self too but doesn't make sense that way
##
##a=myClass()
##a.instanceMethod()
##myClass.classMethod()
##myClass.staticMethod()
##a.instanceMethod()
##a.classMethod()
##a.staticMethod()
##a.anotherMethod()



###Slide 11,12,13
##
##class Fraction:
##    def __init__(self, x=0, y=1):
##        self.numerator=x
##        self.denominator=y
##    def setNumerator(self,x):
##        self.numerator=x
##    def setDenominator(self,y):
##        if y!=0:
##            self.denominator=y
##        else:
##            print('Invalid value, setting to 1 instead')
##    def __str__(self):
##        return str(self.numerator)+'/'+str(self.denominator)
##    def convertDecimal(self):
##        return self.numerator/self.denominator
##    def __add__(self,f2):
##        if isinstance(f2,Fraction):
##            return self.numerator*f2.denominator+f2.numerator*self.denominator, \
##                   self.denominator*f2.denominator
##        else:
##            return 'Wrong argument, only fractions allowed'
##    def __gt__(self,f2):
##        if isinstance(f2,Fraction):
##            return self.numerator*f2.denominator>f2.numerator*self.denominator
##        else:
##            return 'Wrong argument, only fractions allowed'
##
##f1=Fraction(1,2)
##f2=Fraction(1,8)
##print(f1+f2)
##print(f1>f2)



###Slide 14,15
##
class Fraction:
   def __init__(self, x=0, y=1):
       self.numerator=x
       self.denominator=y
   def setNumerator(self,x):
       self.numerator=x
   def setDenominator(self,y):
       if y!=0:
           self.denominator=y
       else:
           print('Invalid value, setting to 1 instead')
   def __str__(self):
       return str(self.numerator)+'/'+str(self.denominator)
   def convertDecimal(self):
       return self.numerator/self.denominator
   def __add__(self,f2):
       if isinstance(f2,Fraction):
           return self.numerator*f2.denominator+f2.numerator*self.denominator, \
                  self.denominator*f2.denominator
       else:
           return 'Wrong argument, only fractions allowed'
   def __gt__(self,f2):
       if isinstance(f2,Fraction):
           return self.numerator*f2.denominator>f2.numerator*self.denominator
       else:
           return 'Wrong argument, only fractions allowed'
   def simplify(self):
       HCF=Fraction.findHCF(self.numerator,self.denominator)
       self.numerator=int(self.numerator/HCF)
       self.denominator=int(self.denominator/HCF)
   def findHCF(a,b):
       factor_a=Fraction.findFactors(a)
       factor_b=Fraction.findFactors(b)
       for i in range (len(factor_a)-1,-1,-1):
           if factor_a[i] in factor_b:
               return factor_a[i]
   def findFactors(x):
       factors=[]
       for i in range(1,x+1):
           if x%i==0:
               factors.append(i)
       return factors

f1=Fraction(15,19)
f1.simplify()
print(f1)
