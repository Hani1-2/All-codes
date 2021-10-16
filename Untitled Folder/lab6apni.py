class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traverse(self):
        a=self
        print("\nTraversing the list...")
        while a is not None:
            print(a.data,end=" ")
            a=a.next
            
    def search(self,target):
        a=self
        if a.data==target:
            return [True, None, a]
        b=a.next
        while b is not None and b.data!=target:
            a=a.next
            b=b.next
        return [b is not None, a, b]
    
    def __len__(self):
        a = self
        i=0
        while a is not None:
            i+=1
            a = a.next
        return i

    def insert(self, value):
        n = ListNode(value)
        n.next=self.next
        self.next=n

    def ins_after(self,x,val):
        res = self.search(x)
        if res[0] == True:
            res[2].insert(val)

    def ins_before(self,x,val):
        res = self.search(x)
        if res[0] == True:
            if res[2] is self:
                new = ListNode(val)
                new.next = self
                self=new
            else:
                res[1].insert(val)
        return self

    def delete_begin(self):
        item=None
        if self.next is not None:
            tmp=self.next
            item=tmp.data
            self.next=tmp.next
        return item
a = ListNode(5)
a.traverse()
for i in range(4):
    a.insert(i)
a.traverse()
a.ins_after(2,7)
a.traverse()
a.ins_before(2,9)
a.traverse()
a.delete_begin()
a.traverse()
