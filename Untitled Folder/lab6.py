
class LinkedList:

    def __init__(self,data):
        self.data  = data
        self.next = None
        self.head = None

    def search(self,x):
        a = None
        b = self.pointer
        if b.data == x:
            return [True, a,b]
        a=b
        b = b.next
        while b.data!=x and b is not  None:
            a = b
            b = b.next

        if b.data == x:
            return [True,a,b ]
        else:
            return [False,a,b]

    def traverse(self):
        a = self.head
        while a is not None:
            print(a.data)
            a=a.next

    def insert(self,x, val):
        self.val = SingleNode(val)
        res = self.search(x)

        if res[0] is True:
            if res[1] is None:
                self.pointer = self.val
                self.pointer.next = res[2]
            #means the given node is not head
            else:
                self.x = res[1]
                self.val.next = self.x.next
                self.x.next = self.val
        else:
            print("invalid")

    def traverse(self):
        a = self
        if a is None:
            print("no traversal in empty")
        else:
            while a is not None:
                print(a.data,end = " ")
                a = a.next
            print("")

    def dele(self,x):
        res = self.search(x)
        assert res[0] == True,"invalid"
        p = res[1]
        q = res[2]
        if p is None:
            self.pointer = q.next
            return q
        else:
            p.next = q.next
            return q
a=LinkedList()


###Double Linked List
class DoubleNode:

    def __init__(self,data):
        self.before = None
        self.data = data
        self.after = None


    def search(self,x):
        a = self
        while a is not None and a.data != x :
            a = a.after
        if a is not None:
            return [True,a]

    def ins_after(self,x,val):

        res = self.search(x)
        assert res[0] is True, "invalid insertion"
        p = res[1]
        q = DoubleNode(val)
        r = p.after

        q.before = p
        q.after = r
        p.after  = q
        if r is not None:
            r.before = q

    def ins_before(self,x,val):
        res = self.search(x)
        assert res[0] is True,"invalid insertion"
        r = res[1] #head
        # print( r is self)
        p = r.before #none
        q = DoubleNode(val) # newhed

        q.before = p
        q.after  = r

        if p is not None:
            p.after = q
        r.before = q
        # self = q


    def traverse(self):
        a = self

        while a is not None:
            print(a.data, end=" ")
            a = a.after

        print(" ")

    def delete(self,x):
        res = self.search(x)
        q = res[1]
        p = q.before
        r = q.after
        if p is not None:
            p.after = r
        if r is not None:
            r.before = p
        if p is  None:
            return r
        return  p
if __name__ == "__main__":
    a = DoubleNode(2)
    a.ins_after(2,3)
    a.ins_after(3,4)
    a.traverse()
    a.ins_before(4,5)
    a.traverse()
    a.ins_before(5,6)
    a.traverse()
    a.delete(6)
    a.traverse()
    a.delete(4)
    a.traverse()
