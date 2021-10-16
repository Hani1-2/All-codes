class Parent:
    def __init__(self, name):
        print ('Parent __init__',name)

class Child(Parent):
    def __init__(self):
        print('Child __init__')
        super().__init__('max')

child=Child()
print (Child.__mro__)