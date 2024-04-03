class vehicle:
    def wheel():
        return 0
class car(vehicle):
    def wheel():
        return 4
class bike(vehicle):
    def wheel():
        return 2
class auto(vehicle):
    def wheel():
        return 3
print("the wheels of car are", car.wheel())
print("The wheels of bike are",bike.wheel())
print("The wheels of auto are ",auto.wheel())
