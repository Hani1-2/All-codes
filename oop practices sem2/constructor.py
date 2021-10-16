###Slide 4, 5
##
##class Fraction:
##    def setNumerator(self,x):
##        self.numerator=x
##    def setDenominator(self,y):
##        if y!=0:
##            self.denominator=y
##        else:
##            print('Invalid value, setting to 1 instead')
##            self.denominator=1
##    def getFraction(self):
##        return self.numerator, self.denominator
##    def convertDecimal(self):
##        return self.numerator/self.denominator
##
##f1=Fraction()
##f1.setNumerator(4)
##f1.setDenominator(10)
##print(f1.getFraction())
##print(f1.convertDecimal())
##
##f2=Fraction()
##f2.setNumerator(9)
##f2.setDenominator(0)
##print(f2.getFraction())



###Slide 12
##
##class Fraction:
##    def __init__(self, x, y):
##        self.numerator=x
##        self.denominator=y
##    def setNumerator(self,x):
##        self.numerator=x
##    def setDenominator(self,y):
##        if y!=0:
##            self.denominator=y
##        else:
##            print('Invalid value, setting to 1 instead')
##            self.denominator=1
##    def getFraction(self):
##        return self.numerator, self.denominator
##    def convertDecimal(self):
##        return self.numerator/self.denominator
##
##f1=Fraction(33,100)
##print('Autoinitializations:', f1.getFraction())
##f1.setNumerator(4)
##f1.setDenominator(10)
##print('Using setters:', f1.getFraction())
###f1=Fraction()



###Slide 13
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
##    def getFraction(self):
##        return self.numerator, self.denominator
##    def convertDecimal(self):
##        return self.numerator/self.denominator
##
##f1=Fraction(33,100)
##print('f1:', f1.getFraction())
##f2=Fraction()
##print('f2:', f2.getFraction())



###Slide 16

class Fraction:
   def __init__(self, x=0, y=1):
       self.numerator=x
       self.denominator=y
   def __del__(self):
       print('Goodbye everyone:((')
   def setNumerator(self,x):
       self.numerator=x
   def setDenominator(self,y):
       if y!=0:
           self.denominator=y
       else:
           print('Invalid value, setting to 1 instead')
   def getFraction(self):
       return self.numerator, self.denominator
   def convertDecimal(self):
       return self.numerator/self.denominator

f1=Fraction(33,100)
print('f1:', f1.getFraction())
del f1
#print('f1:', f1.getFraction())
