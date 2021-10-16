# class Hospital:
#     def __init__(self,n,a):
#         self.name = n
#         self.address = a
#
# class Doctor(Hospital):
#     def __init__(self,n=None,a=None,s=None):
#         super().__init__(n,a)
#         self.specialization = s
#
# class Patient(Hospital):
#     def __init__(self,n=None,a=None,d=None):
#         super().__init__(n,a)
#         self.disease = d
# class medical_test:
#     def __init__(self,p,d):
#         self.p = p
#         self.d = d
#     def medical_info(self):
#         return (f'The medical test of {self.p.disease} is done')
#     def all_info(self):
#         print(f'Doctor: {self.d.name} \nPatient: {self.p.name} \nmedical info: {self.medical_info()}')
#
# h = Hospital('Ziauddin Hosputal','F.B Area')
# d = Doctor('Rafique','Shadman','Technition')
# p = Patient('ABC','Gulshan','Dilated cardiomyopathy')
# m = medical_test(p,d)
# m.all_info()

class A(object):
    def innn(self):

        print('in a ')

class B(object):
    def innn(self):
        print( 'in b')

class X(A, B):
    def innn(self):
        print( 'in x' )

class Y(A,B):
    def innn(self):
        print( ' in y ')

class Z(X, Y):
    def innn(self):
        print( 'in z ')
print(Z.__mro__)
obj = Z()
obj.innn()