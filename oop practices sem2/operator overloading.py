#Slide 8

# class MyStr():
#    def __init__(self, s=''):
#        self.strg=s
#    def __add__(self,anyObject):
#        return self.strg + str(anyObject)
#
# x=MyStr('Python')
# print(x+' Programming')
# print(x+3)
# print(x+3.7)
# print(x+[2,3])
#
#
#
# #Slide 10, 11
#
# class Point:
#    def __init__(self,xcoord=0,ycoord=0):
#        self.x=xcoord
#        self.y=ycoord
#    def setx(self,xcoord):
#             self.x=xcoord
#    def sety(self,ycoord):
#        self.y=ycoord
#    def __str__(self):
#        return '<'+str(self.x)+', '+str(self.y)+'>'
#    def move(self, dx, dy):
#        self.x+=dx
#        self.y+=dy
#    def __add__(self,p2):
#        return self.x+p2.x,self.y+p2.y
#        #return '<'+str(self.x+p2.x)+', '+str(self.y+p2.y)+'>'
#        #return Point(self.x+p2.x,self.y+p2.y)
#
# p1=Point(1,5)
# p2=Point(2,2)
# print(p1)
# print(p2)
# print(p1+p2)



###Slide 17
##
# class Point:
#     def __init__(self,xcoord=0,ycoord=0):
#         self.x=xcoord
#         self.y=ycoord
#     def setx(self,xcoord):
#         self.x=xcoord
#     def sety(self,ycoord):
#         self.y=ycoord
#     def __str__(self):
#         return '<'+str(self.x)+', '+str(self.y)+'>'
#     def move(self, dx, dy):
#         self.x+=dx
#         self.y+=dy
#     def __add__(self,p2):
#         return self.x+p2.x,self.y+p2.y
#     def __iadd__(self,p2):
#         self.x=self.x+p2.x
#         self.y=self.y+p2.y
#         return self
#         #return Point(self.x+p2.x,self.y+p2.y)
#
# p1=Point(1,5)
# p2=Point(2,2)
# p1+=p2
# print(p1)