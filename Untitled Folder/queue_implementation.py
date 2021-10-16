from queuewithlist import *
#from queuewithlinkedlist import *
my_q = myqueue()
print(my_q.isEmpty())
mynum = [5,8,4,3,7]
for i in range(len(mynum)):
    my_q.enqueue(mynum[i])
my_q.traverse()
print()
print(my_q.isEmpty())
print("Dequeue the queue",end=' ')
while not my_q.isEmpty():
    print()
    print(my_q.dequeue())
    my_q.traverse()
print(my_q.isEmpty())
