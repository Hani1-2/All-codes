###Slide 10
##
##amount=int(input('Enter amount to be shared: '))
##sharers=int(input('Enter number of sharers: '))
##print('Each one will get Rs. ',amount/sharers)
##print('Have a blessed day')



###Slide 11
##
##try:
##    amount=int(input('Enter amount to be shared: '))
##    sharers=int(input('Enter number of sharers: '))
##    print('Each one will get Rs. ',amount/sharers)
##except:
##    print('Enter inputs in digits!')
##print('Have a blessed day')



###Slide 12
##
##try:
##    amount=int(input('Enter amount to be shared: '))
##    sharers=int(input('Enter number of sharers: '))
##    print('Each one will get Rs. ',amount/sharers)
##except ValueError:
##    print('Enter inputs in digits!')
##except ZeroDivisionError:
##    print('Number of sharers must be >=1')
##print('Have a blessed day')



###Slide 13
##
##try:
##    amount=int(input('Enter amount to be shared: '))
##    sharers=int(input('Enter number of sharers: '))
##    print('Each one will get Rs. ',amount/sharers)
##except ValueError:
##    print('Enter inputs in digits!')
##except ZeroDivisionError:
##    print('Number of sharers must be >=1')
##except:
##    print('Something went wrong!')
##print('Have a blessed day')



###Slide 14
##
try:
   amount=int(input('Enter amount to be shared: '))
   sharers=int(input('Enter number of sharers: '))
   print('Each one will get Rs. ',amount/sharers)
except ValueError as e:
   print('Problem with value:',type(e),e)
except ZeroDivisionError as e:
   print('Problem with value:',type(e),e)
except:
   print('Cannot identify the problem')
print('Have a blessed day')