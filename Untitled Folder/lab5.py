#Algo 5.1
##
##def Mat_to_List(M):
##    uni_list=[]
##    s = len(M)
##    size = int((s)*(s+1)*(0.5))
##    for i in range(size):
##        uni_list.append(0)
##    #matrix to list
##    i = 0
##    for j in range(s):
##        for k in range(j+1):
##            uni_list[i]=(M[j][k])
##            i+=1
##
##    print("The converted list: ",uni_list)


##M =[[4,0,0,0],
##        [3,-5,0,0],
##        [1,6,2,0],
##        [8,0,5,9]]
##for i in M:
###print(i)
###Mat_to_List(M)


#list to matrix
##def List_to_Mat(l):
##    n=4
##    A=[]
##    #initializing all elements to zero
##    for j in range(n):
##        r=[]
##        for k in range(n):
##            if k>j:
##                r.append(0)
##            else:
##                r.append(l[int(0.5*j*(j+1)+k)])
##        A.append(r)
##
##    print("Converting from list to Matrix: ")
##    for i in A:
##        print(i)
##lst=[4, 3, -5, 1, 6, 2, 8, 0, 5, 9]
##print(lst)
##List_to_Mat(lst)

##
#part(d) removing non zeros

##def Store_Mat(M):
##    U=[]
##    for i in range(len(M)):
##        for j in range(len(M)):
##            if M[i][j]!=0:
##                U.append(M[i][j])
##    print('Unidirectional list',U)
##
##M=[[5,-7,0,0],[1,0,3,0],[9,0,6,0],[2,4,0,0]]
##for i in M:
##    print(i)
##Store_Mat(M)
##
####OUTPUT : 
####list:  [5, -7, 1, 4, 3, 9, -3, 6, 2, 4]
####Q3
##
#(part d)
##def List_to_Mat(U):
##    M=[]
##    n=4 #matrix order
##    k=0
##    for i in range(n):
##        l=[]
##        for j in range(n):
##            if i-1<=j<=i+1:
##                l.append(U[k])
##                k+=1
##            else:
##                l.append(0)
##        M.append(l)
##
##    for i in M:
##        print(i)
##
##lst= [3, 4, 5, 6, 7, 8, 9, 3, 1, 5]
##List_to_Mat(lst)
##
##b
##def size(M):
##    s = 0
##    for i in range(len(M)):
##        for j in range(len(M)):
##            if M[i][j]!=0:
##                s+=1
##    print('size of list :' ,s)
##M=[[5,-7,0,0],[1,0,3,0],[9,0,6,0],[2,4,0,0]]
##for i in M:
##    print(i)
##size(M)
####OUTPUT
####[[5, -7, 0, 0], [1, 4, 3, 0], [0, 9, -3, 6], [0, 0, 2, 4]]
##
##
####Q4
from scipy.sparse import csr_matrix
import numpy as np

# sparse matrix
mat = [[31,0,0,0,0,0],
           [45,23,0,0,98,0],
           [12,34,56,0,0,57]]

# make dense array of input sparse matrix
dense_array = np.array(mat)
print("Dense Array :\n ",dense_array)

#convert into csr
csr_mat= csr_matrix(dense_array) # making a sparse matrix
print("Compressed sparsed row : ",csr_mat)

#convert to dense again
dense_arr2 = csr_matrix.todense(csr_mat)
print("Dense Array: \n",dense_arr2)
