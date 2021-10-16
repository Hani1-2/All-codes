class Node:
    def __init__(self,pri,item):
        self.pri = pri
        self.data = item
        self.next = None

####  class queue
class Priority_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

### find the length of function
    def __len__(self):
        if self.front is None:
            return 0
        count = 0
        a = self.front
        while a is not None:
            count+=1
            a=a.next
        return count

### check if queue is empty or not
    def isEmpty(self):
        return self.front is None


### this function insert the elements in the queue by checking their priority
    def enqueue(self,pri,item):
        new = Node(pri,item)
        if self.front is None:
            self.front = new
            self.rear = new
            return

        if self.front.pri > pri:
            new.next = self.front
            self.front = new
            return

        if self.rear.pri <= pri:
            self.rear.next = new
            self.rear = new
            return

        x= self.front
        y = x.next
        while y is not None and y.pri <= pri:
            x = x.next
            y = y.next
        x.next = new
        new.next = y
        if y is None:
            self.rear = new

##### this function dequeue the elemnt in FIFO order
    def dequeue(self):
        assert not self.isEmpty(), "Empty Queue , underflow"
        x= self.front.pri
        y= self.front.data
        self.front = self.front.next
        return [x,y]

#### this function traverse through the priority queue
    def traverse(self):
        if not self.isEmpty():
            a=self.front
            print("Traversing through the list")
            while a is not None:
                print("{",a.pri,",",a.data,"}",end="")
                a=a.next
            print()

    
lst= [[4,5],[1,6],[3,7],[2,8],[1,7]]
pr_q = Priority_Queue()
print(pr_q.isEmpty())
for i in range(len(lst)):
    pr_q.enqueue(lst[i][0] , lst[i][1])
pr_q.traverse()
print("Dequeing or Removing through the list\n",pr_q.dequeue())
pr_q.traverse()
print("Dequeing or Removing through the list\n",pr_q.dequeue())
pr_q.traverse()
print("Dequeing or Removing through the list\n",pr_q.dequeue())
pr_q.traverse()
pr_q.enqueue(1,4)
pr_q.enqueue(2,6)
pr_q.enqueue(1,8)
pr_q.enqueue(1,5)
pr_q.traverse()
print("Dequeing or Removing through the list\n",pr_q.dequeue())
pr_q.traverse()
print("Dequeing or Removing through the list\n",pr_q.dequeue())
pr_q.traverse()
print(len(pr_q))









        
