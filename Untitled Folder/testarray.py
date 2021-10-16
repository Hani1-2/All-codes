from pyarray import Array

myarray = Array(12)
print('We create an array of 12 elements :')
myarray.traverse()
for i in range (8):
    myarray[i] = i + 2
print('this is how it looks')
myarray.traverse()
print('x= ',myarray[3])
myarray.delete(2)
print('after deleting at 2 ....')
myarray.traverse()
myarray.insert(5,1)
print('after inserting 1 at 5...')
myarray.traverse()
print('here is the length of array...')
print(len(myarray))
