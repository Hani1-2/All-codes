###Slide 5,6
##
# def inputInRange(minValue,maxValue):
#    print(f'Enter a value in between {minValue} and {maxValue}:',end=' ')
#    while True:
#        value=int(input())
#        if value >= minValue and value <= maxValue:
#            return value
#        print('Value out of range, please try again:',end=' ')
#
# def createList(n, minValue, maxValue):
#    result = []
#    for i in range(n):
#        result.append(inputInRange(minValue, maxValue))
#    return result
#
# lst = createList(2, 10, 20)
# print(lst)



###Slide 9
##
##def inputInRange(minValue,maxValue):
##    print(f'Enter a value in between {minValue} and {maxValue}:',end=' ')
##    while True:
##        value=int(input())
##        if value >= minValue and value <= maxValue:
##            return value
##        print('Value out of range, please try again:',end=' ')
##
##def createList(n, minValue, maxValue):
##    result = []
##    for i in range(n):
##        result.append(inputInRange(minValue, maxValue))
##    return result
##
##try:
##    lst = createList(2, 10, 20)
##    print(lst)
##except ValueError:
##    print('Cannot create a list!')



##Slide 11
##
##def inputInRange(minValue,maxValue):
##    print(f'Enter a value in between {minValue} and {maxValue}:',end=' ')
##    while True:
##        value=int(input())
##        if value >= minValue and value <= maxValue:
##            return value
##        print('Value out of range, please try again:',end=' ')
##
##def createList(n, minValue, maxValue):
##    result = []
##    try:
##        for i in range(n):
##            result.append(inputInRange(minValue, maxValue))
##    except ValueError:
##        print('Error creating list!!')
##    return result
##
##lst = createList(2, 10, 20)
##print(lst)



###Slide 13
##
# def inputInRange(minValue,maxValue):
#    print(f'Enter a value in between {minValue} and {maxValue}:',end=' ')
#    try:
#        while True:
#            value=int(input())
#            if value >= minValue and value <= maxValue:
#                return value
#            print('Value out of range, please try again:',end=' ')
#    except:
#        print('Invalid entry interrupted list creation!!!')
#
# def createList(n, minValue, maxValue):
#    result = []
#    for i in range(n):
#        result.append(inputInRange(minValue, maxValue))
#    return result
#
# lst = createList(2, 10, 20)
# print(lst)



###Slide 15
##
# def inputInRange(minValue,maxValue):
#    print(f'Enter a value in between {minValue} and {maxValue}:',end=' ')
#    while True:
#        try:
#            value=int(input())
#            if value >= minValue and value <= maxValue:
#                return value
#            print('Value out of range, please try again:',end=' ')
#        except:
#            print('Invalid entry interrupted list creation!!!')
#            print('Enter a valid integer:',end=' ')
#
# def createList(n, minValue, maxValue):
#    result = []
#    for i in range(n):
#        result.append(inputInRange(minValue, maxValue))
#    return result
#
# lst = createList(2, 10, 20)
# print(lst)



###Slide 17
##
# def inputInRange(minValue,maxValue):
#    print(f'Enter a value in between {minValue} and {maxValue}:',end=' ')
#    while True:
#        try:
#            value=int(input())
#            if value >= minValue and value <= maxValue:
#                return value
#            raise ValueError()#round brackets are optional
#        except:
#            print('Invalid entry interrupted list creation!!!')
#            print('Enter a valid integer:',end=' ')
#
# def createList(n, minValue, maxValue):
#    result = []
#    for i in range(n):
#        result.append(inputInRange(minValue, maxValue))
#    return result
#
# lst = createList(2, 10, 20)
# print(lst)
#


###Slide 18
##
# def inputInRange(minValue,maxValue):
#    print(f'Enter a value in between {minValue} and {maxValue}:',end=' ')
#    while True:
#        try:
#            value=int(input())
#            if value >= minValue and value <= maxValue:
#                return value
#            raise ValueError()
#        except:
#            print('Invalid entry interrupted list creation!!!')
#            print('Enter a valid integer:',end=' ')
#
# def createList(n, minValue, maxValue):
#     result = []
#     for i in range(n):
#        result.append(inputInRange(minValue, maxValue))
#     return result
#
# try:
#    print('Opening MyList.txt!!')
#    f=open('MyList.txt','w')
#    lst = createList(2, 10, 20)
# except:
#    print('Cannot create a list')
# else:
#    f.write(str(lst))
#    print('List successfully saved!!')
# finally: #optional to place in finally
#    f.close()
#    print('Closing MyList.txt!!')



###Slide 22
##
##class InvalidWithdrawal(Exception):
##    pass
##
##try:
##    raise InvalidWithdrawal
##except InvalidWithdrawal:
##    print('I am sorry, but do not have enough balance')



###Slide 23
##
# class InvalidWithdrawal(Exception):
#    def __init__(self, balance, amount):
#        super().__init__(f'Account doesn\'t have ${amount}')
#        self.amount = amount
#        self.balance = balance
#    def overage(self):
#        return self.amount - self.balance
#
# try:
#    raise InvalidWithdrawal(20, 50)
# except InvalidWithdrawal as e:
#    print('I am sorry, but your withdrawal is more than your balance by',e.overage())