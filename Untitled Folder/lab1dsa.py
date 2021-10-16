#print in triangle
x=int(input("enter the number"))
for n in range(0,x):
    n +=1
    print ("*" *(0+n))
    print(id(n))
for n in range(-x,0):
    n +=1
    print ("*" *(0-n+1))
    print(id(n))
