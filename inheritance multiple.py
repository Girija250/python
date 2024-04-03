class Engine:
    def start():
        return "Engine started"
class FuelTank:
    def refuel():
        return "Fuel tank refueled"
class vehicle(Engine,FuelTank):
    pass
class car(vehicle):
    def drive():
        return "Car is being driven"
class bike(vehicle):
    def ride():
        return "Bike is being ridden"
print(car.start())
print(car.refuel())
print(car.drive())
print(bike.start())
print(bike.refuel())
print(bike.ride())
