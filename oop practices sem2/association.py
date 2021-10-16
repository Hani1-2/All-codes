# Slide 5

##class B:  #this class can be defined above or below definition of class A
##        def __init__(self,var):
##            self.varB=var
##class A:
##    def __init__(self,x,y):
##        self.varA=x
##        self.instB=B(y)
##
##aa=A('r',5)
##print('varA:',aa.varA)
##print('instB:',aa.instB.varB)
##del(aa)
###print('varA:',aa.varA) #will give error
###print('instB:',aa.instB.varB) #will give error


###Slide 6
##
##class B:  #this class can be defined above or below definition of class A
##        def __init__(self,var):
##            self.varB=var
##class A:
##    def __init__(self,x,y):
##        self.varA=x
##        self.instB=y
##
##bb=B(5)
##aa=A('r',bb)
##print('varA:',aa.varA)
##print('varB from class A:',aa.instB.varB) #this varB and the varB are pointing to same object 5, use id() to check
##print('varB from class B:',bb.varB)
##del(aa)
###print('varA:',aa.varA) #will give error
###print('varB from class A:',aa.instB.varB) #will give error
##print('varB from class B:',bb.varB)


###Slide 7
##
##class B:  #this class can be defined above or below definition of class A
##        def __init__(self,var):
##            self.varB=var
##class A:
##    def __init__(self,x,y):
##        self.varA1=x
##        self.varA2=y
##
##bb=B(5)
##aa=A('r',bb.varB)
##print('varA1:',aa.varA1,', varA2:',aa.varA2)
##print('varB from class B:',bb.varB)
##del(aa)
###print('varA1:',aa.varA1,', varA2:',aa.varA1) #will give error
##print('varB from class B:',bb.varB)


####Slide 8
####
# class A:
#    class B:
#        def __init__(self,var):
#            self.varB=var
#
#    def __init__(self,x,y):
#        self.varA=x
#        self.instB=self.B(y)
#
# aa=A('r',5)
# print('varA:',aa.varA)
# print('instB:',aa.instB.varB)
# #bb=B() #will give error
# bb=A.B(8)
# print('varB:',bb.varB)
# ab =aa.B(4)
# print(ab.varB)


###Slide 9
##
##x='Global'
##def func1():
##    x='Enclosing'
##    def func2():
##        x='Local'
##        print(x)
##    func2()
##
##func1()


###Slide 10
##
##x='Global'
##class A:
##    x='Class'
##    def method(self):
##        self.x='Inst'
##        print(self.x)
##
##a=A()
##a.method()


###Slide 11
# ##
# x='Global'
# class A:
#    x='Class'
#    def method(self):
#        #x='Method'
#        print(x)
#
# a=A()
# a.method()


###Slide 12
# ##
# x='Global'
# def func():
#    #x='Function'
#    class A:
#        x='Class'
#        def method(self):
#            #x='Method'
#            print(x)
#
#    a=A()
#    a.method()
#
# func()


#Slide 13

# x='Global'
# class A:
#    x='ClassA'
#    def methodA(self):
#        x='MethodA'
#        v=self.B()
#        v.methodB()
#    class B:
#        x='ClassB'
#        def methodB(self):
#            x='MethodB'
#            print(x)
# a=A()
# a.methodA()