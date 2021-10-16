###Ques 2
##def factorial(n):
##    assert n > -1, "Negative number"
##    if n == 0:
##        return 1
##    return n * factorial(n-1)
##
##print(factorial(7))

###Part c
##def toh(num,first,middle,last):
##    assert num > 0
##    if num == 1:
##        print("Move disk from", first, "to", last)
##        return
##    toh(num-1,first,last,middle)
##    toh(1,first,middle,last)
##    toh(num-1,middle,first,last)
##
##toh(3,'A','B','C')
##
#Part D
##def Ackermann(m,n):
##    if m == 0:
##        return n+1
##    elif m > 0 and n == 0:
##        return Ackermann(m-1, 1)
##    elif m > 0  and n>0:
##        return Ackermann(m-1, Ackermann(m, n-1))
##print()
##print(Ackermann(3,4))
##
###Part E
def quicksort(list):
    lst=[]
    n=len(list)
    if n>1:
        lst.append([0,n-1])
        i=0
    while not len(lst) == 0:
        x=lst.pop()
        beg=x[0]
        end=x[1]
        #print(list,beg,end) #uncomment this line to see the step by step working of the algo
        loc=quick(list,beg,end)
        if beg<(loc-1):
            lst.append([beg,loc-1])
        if (loc+1)<end:
            lst.append([loc+1,end])

def quick(list,beg,end):
    loc=beg
    left=beg
    right=end
    while True:
        while list[loc]<=list[right] and loc!=right:
            right-=1
        if loc==right:
            return loc
        if list[loc]>list[right]:
            list[loc],list[right]=list[right],list[loc]
            loc=right
        while list[loc]>=list[left] and loc!=left:
            left+=1
        if loc==left:
            return loc
        if list[loc]<list[left]:
            list[loc],list[left]=list[left],list[loc]
            loc=left

list1=[44, 33, 11, 55, 77, 90, 40, 60, 99, 22, 88, 66]
list2=['D', 'A', 'T', 'A', 'S', 'T', 'R', 'U', 'C', 'T', 'U', 'R', 'E', 'S']

print()
quicksort(list1)
print(list1)

print()
quicksort(list2)
print(list2)


##
##
##
###Part a
##def C(Group, Members):
##    if Members == 1:
##        return Group
##    elif Members == Group:
##        return 1
##    elif Group > Members > 1:
##        return C(Group-1, Members-1)+ C(Group -1, Members)
##
##print()
###print(C(4,3))
##print(C(6,4))
