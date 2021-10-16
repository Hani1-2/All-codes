##from stackwithlist import mystack
import random

class mystack:
    def __init__(self):
        self.elements = list()

    def isEmpty(self):
        return len(self.elements) == 0

    def pop(self):
        assert not self.isEmpty(),"Empty stack!"
        x = self.elements.pop()
        #self.top -= 1
        return x

    def push(self,value):
        #self.top += 1
        self.elements.append(value)

def quicksort(list):
    s=mystack()
    n=len(list)
    if n>1:
        s.push([0,n-1])
    while not s.isEmpty():
        x=s.pop()
        beg=x[0]
        end=x[1]
##        print(list,beg,end) #uncomment this line to see the step by step working of the algo
        loc=quick(list,beg,end)
        if beg<(loc-1):
            s.push([beg,loc-1])
        if (loc+1)<end:
            s.push([loc+1,end])

def quick(list,beg,end):
    left=beg
    right=end
    z = random.choice(list)
    loc=list.index(z)
##    print(loc)
##    print(z)
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

##mylist=[12,19,16]
mylist=[66,77,60,88,55]
#mylist=[44,33,11,55,77,90,40,60,99,22,88,66]
quicksort(mylist)
print(mylist)
