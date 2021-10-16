#print in triangle
##x=int(input("enter the number"))
##for n in range(0,x):
##    n +=1
##    print ("*" *(0+n))
##    print(id(n))
##for n in range(-x,0):
##    n +=1
##    print ("*" *(0-n+1))
##    print(id(n))

##
####
##dic1={1:10, 2:20}
##print('Address of dic1: ',id(dic1))
##dic2={3:30, 4:40}
##print('Address of dic2: ',id(dic2))
##dic3={5:50,6:60}
##print('Address of dic3: ',id(dic3))
##dic1.update(dic2)
##dic1.update(dic3)
##print(dic1)
##print('Address of concatenated dic: ',id(dic1))
##print('~~~Yes we can find the address of keys in dictionary~~~')
##print('Address of keys in dic1 are given below:')
##for i in dic1:
##    print(id(dic1))


##lst = [1,2,2,3,3,4,4,5,2]
##print(lst)
##print('Address of list with duplicates ', id(lst))
##for i in (lst):
##    count = 0
##    x = len(lst)
##    for j in range(x):
##        if i == lst[j]:
##            count+=1
##        if count >1 :
##            lst.remove(i)
##            break
##print()
##lst.sort()
##print(lst)
##print('Address of list without duplicates ', id(lst))
            

##lst = [1,2,23,3,4,(2,3,5),'haniya']
##print('Address of list: ',id(lst))
##for i in lst:
##    if type(i) == type(()):
##        print('Address of tuple is: ',id(i))

#lab 2
import timeit
def insertdata_atposition(list,data,pos):
     list1 = list[0:pos]
     list2 = list[pos:]
     return list1 +data +list2

##start = timeit.default_timer()
##lst = [1,2,3,4,5,6]
##print(lst)
##data = (input('Enter the data you want to insert'))
##data = data.split(' ')
##pos = int(input('Enter position of insertion'))
##print(insertdata_atposition(lst,data,pos))
##stop = timeit.default_timer()
##print('timme taken by implemented func',stop - start)
##
##
##start = timeit.default_timer()
##lst = [1,2,3,4,5,6]
##print(lst)
##data = (input('Enter the data you want to insert'))
##pos = int(input('Enter position of insertion'))
##(lst.insert(pos,data))
##print(lst)
##stop = timeit.default_timer()
##print('timme taken by built-in func',stop - start)

def deletedata_fromlist(list,data):
    for i in range(len(list)):
        if list[i] == data :
            list1 = list[0:i]
            list2 = list[i+1:]
    return (list1 + list2)
##start = timeit.default_timer()
##lst = [11,22,3,34,5,4]
##data = 34
##print(deletedata_fromlist(lst,data))
##stop = timeit.default_timer()
##print('time traken by implemented func',start-stop)
##
##start = timeit.default_timer()
##lst = [11,22,3,34,5,4]
##data = 34
##(lst.remove(data))
##print(lst)
##stop = timeit.default_timer()
##print('time traken by implemented func',start-stop)
    
def searchitem(list,data):
    for i in range(len(list)):
        if list[i] == data:
            print(i)

##start = timeit.default_timer()
##lst = [11,22,3,34,5,4]
##data = 34
##(searchitem(lst,data))
##stop = timeit.default_timer()
##print('time traken by implemented func',start-stop)
##
##start = timeit.default_timer()
##lst = [11,22,3,34,5,4]
##data = 34
##print(lst.index(data))
##stop = timeit.default_timer()
##print('time traken by implemented func',start-stop)


##### Question # 2 ######
# tuple
def insertfunc(tuple,item,pos):
     tup1 = tuple[0:pos]
     tup2 = tuple[pos:]
     
     return tup1 +item +tup2
##start = timeit.default_timer()
##tup = (2,3,8,9,10)
##data = input('Enter value you want to insert')
##x=tuple(data)
##pos =int(input('Enter position for insertion'))
##print(insertfunc(tup,x,pos))
##stop = timeit.default_timer()
##print('time traken by implemented func',start-stop)

def deletefunc(tuple,item):
     for i in range(len(tuple)):
          if tuple[i] == item:
               pos = i
               tup1 = tuple[0:pos]
               tup2 = tuple[pos+2:]
               return (tup1 + tup2)   
tup = (2,3,8,9,10)
print(tup)
start = timeit.default_timer()
data = int(input('Enter value you want to delete'))
print(deletefunc(tup,data))
stop = timeit.default_timer()
print('time traken by implemented func',start-stop)


def searchfunc(tuple,item):
    for i in range(len(tuple)):
        if tuple[i] == int(item):
            return i
##start = timeit.default_timer()
##tup = (3,4,5,6,7)
##print(tup)
##data = input('Enter value you want to search')
##print(searchfunc(tup,data))
##stop = timeit.default_timer()
##print('time traken by implemented func',start-stop)
##
##start = timeit.default_timer()
##tup = (3,4,5,6,7)
##print(tup)
##data = int(input('Enter value you want to search'))
##print(tup.index(data))
##stop = timeit.default_timer()
##print('time traken by built in func',start-stop)

#~~~~Dictionary~~~~~

def insertdata_indic(d,k,v):
     d[k]=v
     return d

##start = timeit.default_timer()
##d={'name':'Haniya','father':'Maqsood'}
##k = (input('Enter the key you want to insert'))
##v = (input('Enter the value you want to insert'))
##print(insertdata_indic(d,k,v))
##stop = timeit.default_timer()
##print('timme taken by implemented func',stop - start)
##
##start = timeit.default_timer()
##d={'name':'Haniya','father':'Maqsood'}
##print(d)
##k = (input('Enter the key you want to insert'))
##v = (input('Enter the value you want to insert'))
##(d.update({k:v}))
##print(d)
##stop = timeit.default_timer()
##print('timme taken by implemented func',stop - start)


def deletedata_fromdic(dic,k):
        if  k in dic:
            del dic[k]
        else:
            print('key not found')
        return dic
##start = timeit.default_timer()
##d={'name':'Haniya','father':'Maqsood'}
##print(d)
##k = (input('Enter the key you want to delete'))
##print(deletedata_fromdic(d,k))
##stop = timeit.default_timer()
##print('timme taken by implemented func',stop - start)
##
##start = timeit.default_timer()
##d={'name':'Haniya','father':'Maqsood'}
##print(d)
##k = (input('Enter the key you want to delete'))
##d.pop(k)
##print(d)
##stop = timeit.default_timer()
##print('timme taken by bultin func',stop - start)


def searchdata_fromdic(dic,k):
        if  k in dic:
            print ((k,d[k]))
        else:
            print('key not found')
        return dic
##
##start = timeit.default_timer()
##d={'name':'Haniya','father':'Maqsood'}
##print(d)
##k = (input('Enter the key you want to search'))
##print(searchdata_fromdic(d,k))
##stop = timeit.default_timer()
##print('timme taken by implemented func',stop - start)
##
##start = timeit.default_timer()
##d={'name':'Haniya','father':'Maqsood'}
##print(d)
##k = (input('Enter the key you want to search'))
##x=d.get(k)
##print((k,x))
##stop = timeit.default_timer()
##print('timme taken by bultin func',stop - start)









