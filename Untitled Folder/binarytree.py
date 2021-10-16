class BTree:
    # creates tree root and returns a pointer to it.
    def __init__(self, item):
        self.data = item
        self.lc = None
        self.rc = None

    # adds item as left child to the node
    def addlc(self, item):
        assert self.lc is None, "Left child already present"
        self.lc = BTree(item)

    # adds item as right child to the node
    def addrc(self, item):
        assert self.rc is None, "Right child already present"
        self.rc = BTree(item)

    # deletes left child of node
    def dellc(self):
        assert self.lc is not None, "Left child absent"
        assert self.lc.lc is None and self.lc.rc is None, "This node has children"
        x = self.lc.data
        self.lc = None
        return x

    # deletes left child of node
    def delrc(self):
        assert self.rc is not None, "Right child absent"
        assert self.rc.lc is None and self.rc.rc is None, "This node has children"
        x = self.rc.data
        self.rc = None
        return x

    def posttraverse(self):
        if self.lc is not None:
            self.lc.posttraverse()
        if self.rc is not None:
            self.rc.posttraverse()
        print(self.data, end=" ")
        
    def pretraverse(self):
        print(self.data, end=" ")
        if self.lc is not None:
            self.lc.pretraverse()
        if self.rc is not None:
            self.rc.pretraverse()
            
    def traversein(self):
        if self.lc is not None:
            self.lc.traversein()
        print(self.data, end=" ")
        if self.rc is not None:
            self.rc.traversein()
            
    def traversebf(self):
        nodes = [self]
        print(self.data, end=" ")
        i=0  # index of elemnt in nodes list
        n=1 # no of elements in nodes list 
        while i<n:
            p = nodes[i]
            if p.lc is not None:
                print(p.lc.data, end=" ")
                nodes.append(p.lc)
                n+=1
            if p.rc is not None:
                print(p.rc.data, end=" ")
                nodes.append(p.rc)
                n+=1
            i+=1
        print()

    def height(self):
        if self.rc is None and self.lc is None:
            return 1
        rh = 0
        lh = 0
        if self.rc is not None:
            rh = self.rc.height()
        if self.lc is not None:
            lh = self.lc.height()
        if rh > lh:
            return rh + 1
        return lh + 1

    def nodecount(self):
        if self.lc is None and self.rc is None:
            return 1
        lnc = 0
        rnc = 0
        if self.lc is not None:
            lnc = self.lc.nodecount()
        if self.rc is not None:
            rnc = self.rc.nodecount()
        return lnc + rnc + 1

    def leafcount(self):
        if self.lc is None and self.rc is None:
            return 1
        llc = 0
        rlc = 0
        if self.lc is not None:
            llc = self.lc.leafcount()
        if self.rc is not None:
            rlc = self.rc.leafcount()
        return llc + rlc

    def internalNodeCount(self):
        if self.lc is None and self.rc is None:
            return 0
        return 1 + self.lc.internalNodeCount() + self.rc.internalNodeCount()

    def isStrictlyBinary(self):
        if self.lc is None:
            if self.rc is None:
                return True
            return False
        if self.rc is None:
            return False
        return self.lc.isStrictlyBinary() and self.rc.isStrictlyBinary()

    def isAlmostComplete(self):
        if self.isPerfect():
            return True
        if self.lc is None:
            return False
        hl = self.lc.height()
        if self.rc is None:
            if hl == 1:
                return True
            return False
        hr = self.rc.height()
        if hl == hr and self.lc.isPerfect():
            return self.rc.isAlmostComplete()
        if hl == hr + 1 and self.rc.isPerfect():
            return self.lc.isAlmostComplete()
        return False

    def isPerfect(self):
        h = self.height()
        n = self.nodecount()
        m = pow(2, h) - 1
        if n == m:
            return True
        return False
##
    def calculateDepth(self):
        d = 0
        while (self is not None):
            d += 1
            self= self.lc
        return d


# Check if the tree is perfect binary tree
    def is_perfect(self, d, level=0):

        # Check if the tree is empty
        if (self is None):
            return True

        # Check the presence of trees
        if (self.lc is None and self.rc is None):
            return (d == level + 1)

        if (self.lc is None or self.rc is None):
            return False

        return (self.lc.is_perfect(d, level + 1) and
                self.rc.is_perfect(d, level + 1))

    def is_Perfect(self):
        if self is None:
            return True
        lh = self.lc.nodecount()
        rh=self.rc.nodecount()
        if lh == rh:
            return True
        else:
            return False

##    def buildtree(val):
##        if len(val)==0 or val[0] is None:
##            return None
##        root =BTree(val[0])
##        nodes = [root]
##        n=0
##        i=0
##        while i <len(val):
##            p=node[n]
##            if val[i] != None:
##                p.addlc(val[i])
##                nodes.append(p.lc)
##            i+=1
##            if val[i] != None:
##                p.addrc(vak[i])
##                nodes.append(p.rc)
##            i+=1
##            n+=1
##        return root
##
##t = BTree(6)
##t.addlc(4)
##t.addrc(8)
##t.lc.addlc(3)
##t.lc.addrc(2)
##t.rc.addlc(7)
##t.rc.addrc(6)
##val=[5,8,None,3,6,None,None,2,7]
##
##t = buildtree(val)
print("Breadth first traversal")
t.traversebf()
print("In order traversal")
t.traversein()
print()
print('internal node:',t.internalNodeCount())
print('leaf count',t.leafcount())
print('node count',t.nodecount())
##print()
##t.pretraverse()
##print()
##t.posttraverse()
##print('miss PBT code',t.isPerfect())
##d= t.calculateDepth()
##print('resursive PBT code',t.is_perfect(d))
##print('Mine iterative PBT code',t.is_Perfect())
##print("Almost complete",t.isAlmostComplete())
####
