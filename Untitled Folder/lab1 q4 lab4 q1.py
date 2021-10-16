##Lab 1 q:4
lst=[1,2,3,(2,3),5,9,(6,3,5)]
count=0
for x in lst:
    if type(x)!=tuple:
        count+=1
    else:
        ta=id(x)
        print(x,"----",ta)
print("List ----",id(lst))
print('Elements in list except tuple:',count)


##Lab 4 q:1
def mat_input():
    n=int(input("\nDimensions of square matrix:"))
    print("\nEnter values separated by commas")
    mat=[]
    for i in range(1,n+1):
        a=input(f'Enter values for row{i}: ')
        lst=a.split(',')
        b=[int(j) for j in lst]
        mat.append(b)
    print("Matrix:")
    for i in range(n):
        for j in range(n):
            print(mat[i][j],' ' ,end='')
        print()
    return mat
        
def mat_mult(a,b):
    res=[]
    n=len(a)
    for x in range(n):
        r= [ ]
        for y in range(n):
            r.append(y)
        res.append(r)

    for i in range(n):
        for j in range(n):
            res[i][j]=0
            for k in range(n):
                res[i][j]=res[i][j]+a[i][k]*b[k][j]
    print("\n\nResult of Multiplication:")
    for i in range(n):
        for j in range(n):
            print(res[i][j],' ' ,end='')
        print()
    return res

m1=mat_input()
m2=mat_input()
t=mat_mult(m1,m2)
