from pyarray2d import Array2D
def multi_mat(mat1,num):
    x = mat1.numrows()
    y = mat1.numcols()
    mat4 = Array2D(x,y)
    mat4.clear(0)
    for i in range(x):
        for j in range(y):
            mat4[i,j] = mat4[i,j] + (mat1[i,j]*num)
    return mat4.traverse()

print('****This is my matrix****')
mat1 = Array2D(2,2)
for i in range(2):
    for j in range(2):
        mat1[i,j] = 2 * i + 3 * j +4
mat1.traverse()
print()
print('****After multiply by number
      ****')
multi_mat(mat1,2)
