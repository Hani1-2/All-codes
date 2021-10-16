class myqueue:
    def __init__(self):
        self.elements = list()

    def __len__(self):
        return len(self.elements)

    def isEmpty(self):
        return len(self)==0

    def enqueue(self,item):
        self.elements.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Empty queue"
        return self.elements.pop(0)

    def traverse(self):
        for i in range(len(self)):
            print(self.elements[i],end=" ")
            
