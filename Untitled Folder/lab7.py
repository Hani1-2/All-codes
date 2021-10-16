class stack:
    def __init__(self,size):
        self.data=[]
        self.maxStk=size
        self.element=[]
    def isEmpty(self):
        return len(self.element)==0
    def push(self,item):
        assert len(self.data)<self.maxStk,"overflow"
        self.data.append(item)
    def pop(self):
        assert len(self.data)!=0,"underflow"
        return (self.data.pop())



x=4
z=0
y=x+1
f=stack(5)
f.push(y)
f.push(y+1)
f.push(x)
f.push(z)
f.pop()
x=y+1
f.push(x)
f.push(z)
f.isEmpty()
while ((f.isEmpty())==False):
    print(f.pop())
print(z)
print("x:",x)
print("y:",y)
print("z:",z)
