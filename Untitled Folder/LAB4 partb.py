##
####Lab 4 q:1
##def mat_input():
##    n=int(input("\nDimensions of square matrix:"))
##    print("\nEnter values separated by commas")
##    mat=[]
##    for i in range(1,n+1):
##        a=input(f'Enter values for row{i}: ')
##        lst=a.split(',')
##        b=[int(j) for j in lst]
##        mat.append(b)
##    print("Matrix:")
##    for i in range(n):
##        for j in range(n):
##            print(mat[i][j],' ' ,end='')
##        print()
##    return mat
##        
##def mat_mult(a,b):
##    res=[]
##    n=len(a)
##    for x in range(n):
##        r= [ ]
##        for y in range(n):
##            r.append(y)
##        res.append(r)
##
##    for i in range(n):
##        for j in range(n):
##            res[i][j]=0
##            for k in range(n):
##                res[i][j]=res[i][j]+a[i][k]*b[k][j]
##    print("\n\nMultiplication Of Matrices:")
##    for i in range(n):
##        for j in range(n):
##            print(res[i][j],' ' ,end='')
##        print()
##    return res
##
##m1=mat_input()
##m2=mat_input()
##t=mat_mult(m1,m2)



#LAB4 PARTb

###Creates matrix of r*c dimension
def matInput():
    r = int(input("no of rows:"))
    c = int(input("no of coloumns:"))
    mat = []
    for x in range(r):
        row = []
        for y in range(c):
            temp = int(input(f'Enter element for row {x+1}:'))
            row.append(temp)
        mat.append(row)
    for i in mat:
        print(i)
    return mat

def matMult(a,b):
    assert len(a[0]) == len(b), "Matrix multiplication not possible" #col of mat(a) equal to row of mat(b)
    res=[]
    for x in range(len(a)):
        r=[]
        for y in range(len(b[0])):
            r.append(y)
        res.append(r)

    for i in range(len(a)):
        for j in range(len(b[0])):
            res[i][j]=0
            for k in range(len(b)):
                res[i][j]+=(a[i][k]*b[k][j])
    for i in res:
        print(i)
    return res

m1 = matInput()
print()
m2 = matInput()
print()
matMult(m1,m2)
