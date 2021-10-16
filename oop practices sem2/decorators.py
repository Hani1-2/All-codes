###slide 4
##
##def funcObject():
##    print('I am function object')
##
##m=funcObject()
##s=funcObject
##s()
##print(s)



###Slide 5
##
##def funcObject():
##    print('I am function object')
##
##def func_a(x):
##    print(x)
##    x()
##
##func_a(funcObject)
##s=funcObject
##func_a(s)



###Slide 6
##
##def funcObject():
##    print('I am function object')
##
##def func_c():
##    return funcObject
##
##print(func_c())
##
##def func_c():
##    return funcObject()
##
##print(func_c())



###Slide 10
##
###defining a decorator
##def myDecorator(func):
##    def myWrapper():
##        print('Wrapper before func execution')
##        func()
##        print('Wrapper after func execution')
##    return myWrapper
##
##using the decorator
#@myDecorator
#def myFunc():
#    print('Decorated')
##myFunc=myDecorator(myFunc)
#
##calling the function
#myFunc()



###Slide 11
##
# import time
# def calcTime(func):
#    def wrapper():
#        begin=time.time()
#        func()
#        end=time.time()
#        print('Run-time:',end-begin,'seconds')
#    return wrapper
#
# @calcTime
# def long_loop():
#    print('Take your time\nHit any alphanumeric key to exit!')
#    input()
#
# long_loop()

class fancyPrint:
    message = ''
    def setMessage(self,m):
        fancyPrint.message = (m)

    @staticmethod
    def fancyPrint():
        print(fancyPrint.message.upper())

    def makeFancy(fancyprint):
        def wrapper():
            print('**********')
            fancyPrint.fancyPrint()
            print('*******')
        return wrapper
    fancyPrint = makeFancy(fancyPrint)
mssg=fancyPrint()
mssg.setMessage('Congratulations!!')
fancyPrint.fancyPrint()
