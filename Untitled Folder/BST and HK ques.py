##def conv(f):
##    c= (9/5)*f + 32
##    return print( ' the temp in celcius is ' , c)

##class node:
##    def __init__(self,data):
##        self.data = data
##        self.next = None;
##    
##class linkedlist:
##    def __init__(self):
##        self.start = None;
##        
##    def viewlist(self):
##        if self.start == None:
##            print("list is empty")
##        else:
##            temp = self.start
##            while temp != None: # 
##                print(temp.data , end = ' ') 
##                temp = temp.next
##                
##    def deleteFirst(self):
##        if self.start == None:
##            print("Linked list is empty")
##        else:
##            self.start = self.start.next
##            
##    def insertlast(self,value):
##        l= [int(input()) for i in range (value)]
##        for i in l:
##            newNode = node(i)
##            if (self.start == None):
##                self.start = newNode;
##            else:
##                temp = self.start
##                while temp.next!=None:
##                    temp=temp.next  
##                temp.next = newNode
##
##mylist = linkedlist()
##mylist.insertlast(4)
##
##
##mylist.viewlist()
##print()
##mylist.deleteFirst()
##mylist.viewlist()



##class Node:
##    def __init__(self,data):
##        self.data = data
##        self.next = None 
##class Solution: 
##    def display(self,head):
##        current = head
##        while current:
##            print(current.data,end=' ')
##            current = current.next
##
##    def insert(self,head,data):     # this insert part is tricky
##        if (head == None):
##            head = Node(data)
##        elif (head.next == None):
##            head.next = Node(data)
##        else: 
##            self.insert(head.next, data)
##        return head
##
##        
##mylist= Solution()
##T=int(input())
##head=None
##for i in range(T):








    
##    data=int(input())
##    head=mylist.insert(head,data)    
##mylist.display(head); 


### day 17 power calculator
##class e(Exception):
##    pass
##
##class Calculator:
##    def __init__(self):
##        pass
##
##    def power(self,n,p):
##        self.n = n
##        self.p = p
##        if (n <0 or p < 0):
##            raise ValueError ('n and p should be non-negative')
##        
##        return (n ** p)
##
##myCalculator=Calculator()
##T=int(input())
##for i in range(T):
##    n,p = map(int, input().split())
##    try:
##        ans=myCalculator.power(n,p)
##        print(ans)
##    except Exception as e:
##        print(e)  

##import sys
##from collections import deque
##
##class Solution:
##    def __init__(self):
##        self.stack = list()
##        self.queue = deque()
##
##    def pushCharacter(self , character):
##        self.stack.append(character)
##
##    def enqueueCharacter(self , character):
##        self.queue.append(character)
##
##    def popCharacter(self):
##        return self.stack.pop()
##
##    def dequeueCharacter(self):
##        return self.queue.popleft()
##
##    
##s=input()
###Create the Solution class object
##obj=Solution()   
##
##l=len(s)
##
#### push/enqueue(add an object to back of the line) all the characters of string s to stack
##
##for i in range(l):
##    obj.pushCharacter(s[i])
##    obj.enqueueCharacter(s[i])
##    
##isPalindrome=True
##'''
##pop the top character from stack
##dequeue (remove the object at the head of the line  )the first character from queue
##compare both the characters
##''' 
##for i in range(l // 2):
##    if obj.popCharacter()!=obj.dequeueCharacter():
##        isPalindrome=False
##        break
###finally print whether string s is palindrome or not.
##if isPalindrome:
##    print("The word, "+s+", is a palindrome.")
##else:
##    print("The word, "+s+", is not a palindrome.") 

# this is called binary search tree

##class Node:
##    def __init__(self,data):
##        self.right=self.left=None
##        self.data = data
##class Solution:
##    def insert(self,root,data):
##        if root==None:
##            return Node(data)
##        else:
##            if data<=root.data:
##                cur=self.insert(root.left,data)
##                root.left=cur
##            else:
##                cur=self.insert(root.right,data)
##                root.right=cur
##        return root
##
##    def getHeight(self,root):
##        #Write your code here
##        if not root:
##            return -1
##        if not root.left and not root.right:
##            return 0
##        left_height = self.getHeight(root.left)
##        right_height = self.getHeight(root.right)
##        return max(left_height , right_height) + 1
##
##T=int(input())
##myTree=Solution()
##root=None
##for i in range(T):
##    data=int(input())
##    root=myTree.insert(root,data)
##height=myTree.getHeight(root)
##print(height)
##

# BSt transversal , it prints the numbers in the form of BST
##class Node:
##    def __init__(self,data):
##        self.right=self.left=None
##        self.data = data
##class Solution:
##    def insert(self,root,data):
##        if root==None:
##            return Node(data)
##        else:
##            if data<=root.data:
##                cur=self.insert(root.left,data)
##                root.left=cur
##            else:
##                cur=self.insert(root.right,data)
##                root.right=cur
##        return root
##
##    def levelOrder(self,root):
##        queue = [root] if root else []
##    
##        while queue:
##            node = queue.pop()
##            print(node.data, end=" ")
##        
##            if node.left: queue.insert(0,node.left)
##            if node.right: queue.insert(0,node.right)
##
##T=int(input())
##myTree=Solution()
##root=None
##for i in range(T):
##    data=int(input())
##    root=myTree.insert(root,data)
##myTree.levelOrder(root)
##
##
##class Node:
##    def __init__(self,data):
##        self.data = data
##        self.next = None
##
##    def __repr__(self):
##        return self.data
##
##class LinkedList:
##    def __init__(self):
##        self.head = None
##
##    def __repr__(self):
##        node = self.head
##        nodes = []
##        while node is not None:
##            nodes.append(node.data)
##            node = node.next
##        nodes.append('None')
##        return ('-->'.join(nodes))
##
##llist = LinkedList([])
##print (llist)
##T=int(input())
##
##root=None
##for i in range(T):
##    data=int(input())
##myTree = LinkedList()
##print (myTree)



###t there is a linked list which remove all duplicates occur in the linkedlist

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        h = head
        while head.next is not None:
            if head.next.data==head.data:
                head.next=head.next.next
            else:
                head=head.next
        return h

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 












































