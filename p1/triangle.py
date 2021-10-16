class Car:
    def __init__(self,speed,color):
        self.__speed=speed
        self.__color=color

    def set__speed(self,value):
        self.__speed=value

    def get__speed(self):
        return self.__speed

    def set__color(self,value):
        self.__color=value

    def get__color(self):
        return self.__color

ford=Car(200,'red')
honda=Car(300,'blue')
audi=Car(400,'black')

ford.set__speed(300)
ford.set__color('yellow')

