from singlylinkedlist import ListNode
class myqueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def __len__(self):
        if self.front is None:
            return 0
        return len(self.front)

    def isEmpty(self):
        return self.front is None

    def enqueue(self,item):
        if self.front is None:
            self.front = ListNode(item)
            self.rear = self.front
        else:
            self.rear.insert(item)
            self.rear = self.rear.next

    def dequeue(self):
        assert not self.isEmpty(),"Empty queue"
        x = self.front.data
        self.front = self.front.next
        return x

    def traverse(self):
        if self.front is not None:
            self.front.traverse()


