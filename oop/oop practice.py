class Car:
    def __init__(self, speed, color):
        print (speed)
        print(color)
        self.speed=speed
        self.color=color
        print('the __init__ is called')

ford=Car(200,'red')
honda=Car(340,'blue')
audi=Car(780,'black')
#
# ford.speed = 200
# honda.speed = 300
# audi.speed = 223
#
# ford.color='red'
# audi.color='blue'
# honda.color='green'
#
print(ford.speed)
print(ford.color)

