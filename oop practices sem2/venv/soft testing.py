###Slide 13
##
##def findPower(base,exp):
##    if exp==0:
##        return 1
##    else:
##        return base**exp
##
##print(findPower(0,0))
##print(findPower(2,0))
##print(findPower(4,4))
##print(findPower(25,-5))
##print(findPower(1009,-1))
##print(findPower(-3,45))
##print(findPower(2.5,3))
##print(findPower(2.5,6.7))
##print(findPower(-2.4,-1.1))



###Slide 15
##
##def printList(lst):
##    print('S. No.     Element')
##    sNo=1
##    for i in lst:
##        print(sNo,'     ',i)
##
##printList(['Apples','Oranges','Bananas'])
##printList([])
##printList()



###Slide 19
##
##def ifPositive(x):
##    if x>=-1:
##        return True
##    else:
##        return False
##
##print(ifPositive(-2))
##print(ifPositive(+2))
##print(ifPositive(0))
##print(ifPositive(-1))



###Slide 21
##
##def printList(lst):
##    print('S. No.     Element')
##    sNo=1
##    for i in lst:
##        print(f'{sNo:3}        {i:10}')
##        sNo+=1
##
##printList(['Apples','Oranges','Bananas'])
##printList(['Apples'])
##printList([])
##printList()



###Slide 25
##
##def avg(grades):
##    assert len(grades) != 0, 'No grades data'
##    return sum(grades)/len(grades)
##
##print(avg([190,92,96]))
##print(avg([])) #or print(avg())



###Slide 26
##
##def avg(grades):
##    try:
##        assert len(grades) != 0
##        return sum(grades)/len(grades)
##    except AssertionError:
##        print('No grades data')
##
##print(avg([190,92,96]))
##print(avg([])) #or print(avg())