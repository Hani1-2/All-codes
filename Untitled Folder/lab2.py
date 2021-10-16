####lab 2
##### Question # 2 ######
# tuple
import timeit
def insertfunc(tup,item,pos):
     tup = tup[:pos] +(item,)+ tup[pos:]
     return tup

##start = timeit.default_timer()
##tup = (2,3,8,9,10)
##print(tup)
##data =int(input('Enter value you want to insert'))
##pos =int(input('Enter position for insertion'))
##print(insertfunc(tup,data,pos))
##stop = timeit.default_timer()
##print('time traken by implemented func',start-stop)
##print('Tuple is immutable datatype no builtin func to insert an element')
        

##def deletefunc(tuple,item):
##    for i in range(len(tuple)):
##        if tuple[i] == item:
##            tup1 = tuple[0:i]
##            tup2 = tuple[i+1:]
##            return (tup1 + tup2)
def deletefunc(tuple,item):
     tup=()
     for i in range(len(tuple)):
         if tuple[i] == item:
             tup1 = tuple[0:i]
             print(tup1)
             tup1 = tup1[:-1]
             tup2 = tuple[i+1:]
             tup = (tup1 + tup2)
             print(type(tup))
     return ((tup))
start = timeit.default_timer()
tup = input('Enter any value in tuple:')

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
##d={'name':'abc','father':'xyz'}
##k = (input('Enter the key you want to insert'))
##v = (input('Enter the value you want to insert'))
##print(insertdata_indic(d,k,v))
##stop = timeit.default_timer()
##print('timme taken by implemented func',stop - start)
##
##start = timeit.default_timer()
##d={'name':'abc','father':'xyz'}
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
##d={'name':'abc','father':'xyz'}
##print(d)
##k = (input('Enter the key you want to delete'))
##print(deletedata_fromdic(d,k))
##stop = timeit.default_timer()
##print('timme taken by implemented func',stop - start)
##
##start = timeit.default_timer()
##d={'name':'abc','father':'xyz'}
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

##start = timeit.default_timer()
##d={'name':'abc','father':'xyz'}
##print(d)
##k = (input('Enter the key you want to search'))
##searchdata_fromdic(d,k)
##stop = timeit.default_timer()
##print('timme taken by implemented func',stop - start)
##
##start = timeit.default_timer()
##d={'name':'abc','father':'xyz'}
##print(d)
##k = (input('Enter the key you want to search'))
##x=d.get(k)
##print((k,x))
##stop = timeit.default_timer()
##print('timme taken by bultin func',stop - start)

