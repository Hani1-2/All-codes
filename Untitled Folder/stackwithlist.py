class mystack:
    def __init__(self):
        self.elements = list()

    def isEmpty(self):
        return len(self.elements) == 0

    def pop(self):
        assert not self.isEmpty(),"Empty stack!"
        x = self.elements.pop()
        #self.top -= 1
        return x

    def push(self,value):
        #self.top += 1
        self.elements.append(value)



##class mystack:
##    def __init__(self,size):
##        self.top = None
##        self.size = size 
##        self.elements = list()
##
##    def isEmpty(self):
##        return len(self.elements) == 0
##
##    def pop(self):
##        if not self.isEmpty():
##            print("Empty stack! underflow")
##        x = self.elements.pop()
##        #self.top -= 1
##        return x
##
##    def push(self,value):
##        if len(self.elements) == self.size:
##            print("Full stack , overflow")
##        #self.top += 1
##        self.elements.append(value)
##

