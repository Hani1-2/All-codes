# class X:
#     def method(self):
#         print('in x method')
# class Y:
#     def method(self):
#         print('in y method')
# class A(X):
#     def method(self):
#         print('in A method')
# class B(Y):
#     def method(self):
#         print('I B method')
# class C(A,B):
#     pass
# objectC=C()
# objectC.method()

class X:
    def method(self):
        print('In x method')
class Y:
    def method(self):
        print('In y method')
class A(X):
    pass
class B(Y):
    def method(self):
        print('In B method')
class C(A,B):
    pass
objectC=C()
objectC.method()

### Slide 17
##
##class X:
##    pass
##class Y:
##    def method(self):
##        print('In method Y')
##class A(X):
##    pass
##class B(Y):
##    pass
##class C(A, B):
##    pass
##
##objectC=C()
##objectC.method()



### Slide 19
##
##class X:
##    def method(self):
##        print('In method X')
##class A(X):
##    def method(self):
##        print('In method A')
##class B(X):
##    def method(self):
##        print('In method B')
##class C(A, B):
##    def method(self):
##        print('In method C')
##
##objectC=C()
##objectC.method()



### Slide 20
##
##class X:
##    def method(self):
##        print('In method X')
##class A(X):
##    def method(self):
##        print('In method A')
##class B(X):
##    def method(self):
##        print('In method B')
##class C(A, B):
##    pass
##
##objectC=C()
##objectC.method()



### Slide 21
##
##class X:
##    def method(self):
##        print('In method X')
##class A(X):
##    pass
##class B(X):
##    def method(self):
##        print('In method B')
##class C(A, B):
##    pass
##
##objectC=C()
##objectC.method()



### Slide 22
##
##class X:
##    def method(self):
##        print('In method X')
##class A(X):
##    pass
##class B(X):
##    pass
##class C(A, B):
##    pass
##
##objectC=C()
##objectC.method()