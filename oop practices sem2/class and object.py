###Slide 5
#
# class Animal:
#    specie = 'cat'
#    language = 'meow'
#
#    def speak (self):
#        print('I am a ' + self.specie + ' and I can ' + self.language)
#
# a1=Animal()
# print ('Attribute 1 of Animal: ' + a1.specie)
# print('Attribute 2 of Animal: ' + a1.language)
# a1.speak()


# class Animal:
#    specie = 'cat'
#    language = 'meow'
#
#    def speak (self):
#        print('I am a ' + self.specie + ' and I can ' + self.language)
#
# a1 = Animal()
# a1.specie = 'lion'
# a1.language = 'roar'
# print ('Attribute 1 of Animal: ' + a1.specie)
# print('Attribute 2 of Animal: ' + a1.language)
# a1.speak()
#
# class Animal:
#
#    def set_specie(self,s):
#        self.specie = s
#    def set_language(self,l):
#        self.language = l
#
#    def get_specie(self):
#        return self.specie
#    def get_language(self):
#        return self.language
#
#    def speak (self):
#        print('I am a ' + self.specie + ' and I can ' + self.language)
#
# a1=Animal()
# a1.set_specie('goat')
# a1.set_language('bleet')
# print ('the attribute 1 of a1 is',a1.get_specie())
# print ('the attribute 2 of a1 is',a1.get_language())
# a1.speak()

# class Point:
#     x = 0
#     y = 0
#     def set_x(self,xcoord):
#         self.x = xcoord
#     def set_y(self,ycoord):
#         self.y = ycoord
#     def get(self):
#         return self.x , self.y
#     def move(self,x1,y1):
#         self.x += x1
#         self.y += y1
#         return (self.x,self.y)
# p1 = Point()
# p1.set_x(3)
# p1.set_y(2)
# print('the initial point is' , p1.get())
# print('the point move to', p1.move(3,4) )

##with user comments
##
class Animal:
   '''Class Animal defines an animal object having a specific specie and language.
      It has two attributes and three methods.'''
   specie = 'cat'
   language = 'meow'

   def setSpecie (self,s):
       '''This is setter method for the attribute specie'''
       self.specie = s
   def setLanguage (self, l):
       '''This is setter method for the attribute language'''
       self.language = l
   def speak (self):
       '''This method shows how an animal talks!!'''
       print('I am a' , self.specie, 'and I can', self.language)
p1 =Animal()
help(p1)
#
# class Circle:
#     color = None
#     radius = None
#
#     def set_radius(self,radius):
#         self.radius = radius
#
#     def set_color(self,color):
#         self.color  = color
#
#     def get_color(self):
#         return self.color
#
#     def get_radius(self):
#         return self.radius
#
#     def circum(self):
#         circumf = 2*3.14*self.radius
#         print ('the circumference of cirlce is' , circumf)
#
#     def area(self):
#         area = 3.142 * (self.radius**2)
#         print ('the area of the circle is', area)
#
# a1 = Circle()
# a1.set_color('green')
# a1.set_radius(3)
# a1.area()
# a1.circum()

# class Student:
#     name = None
#     roll_no = None
#     marks = [0,0,0]
#
#     def setName(self,n):
#         self.name = n
#     def setRoll(self,r):
#         self.roll_no = r
#     def setMarks(self,m):
#         self.marks[0] = m[0]
#         self.marks[1] = m[1]
#         self.marks[2] = m[2]
#
#     def getName(self):
#         return self.name
#     def getRollno(self):
#         return self.roll_no
#     def getMarks(self):
#         return (self.marks[0] , self.marks[1] , self.marks[2])
#
#     def get_student(self):
#         print ('<student name>' , self.name)
#         print ('<roll no>', self.roll_no)
#         print ('Marks')
#         print ('Quiz no 1' , self.marks[0])
#         print('Quiz no 2', self.marks[1])
#         print('Quiz no 3', self.marks[2])
#
#     def avg(self):
#         avg = (self.marks[0] +self.marks[1] +self.marks[2])/3
#         return avg
#
# s1=Student()
# s1.setName('Haniya Maqsood')
# s1.setRoll(18)
# m= [13,7,9]
# s1.setMarks(m)
# s1.get_student()
# print('the average of quiz is ' , s1.avg())

# class Animal:
#    specie = 'cat'
#    language = 'meow'
#    count=0
#
#    def setSpecie (self, s):
#        self.specie = s
#    def setLanguage (self, l):
#        self.language = l
#    def getSpecie (self):
#        return self.specie
#    def getLanguage (self):
#        return self.language
#    def speak (self):
#        print('I am a',self.specie,'and I can',self.language)
#    def speakAlot (self):
#        for i in range(10):
#            print(self.language)
#    def countAnimal (self):
#        Animal.count+=1
#        self.assignID(Animal.count)
#        return Animal.count
#    def assignID (self, id):
#        self.ID=id
#    def getID (self):
#        return self.ID
#
# a1=Animal()
# x=a1.countAnimal()
# a2=Animal()
# a2.countAnimal()
# a3=Animal()
# a3.countAnimal()
# print('Count:', x)
# print('ID of a1:', a1.getID())
# print('Count:', Animal.count)
# print('ID of a2:', a2.getID())
# print('Count:', Animal.count)
# print('ID of a3:', a3.getID())
# print('Total count:', Animal.count)


