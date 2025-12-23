class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f'{self.brand} is driving')
car = Car('toyo', 'vios')
car.drive()

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def charge(self):
            print(f'{self.brand} is charging')
ev = ElectricCar('tesla', 'v3', 75)
ev.drive()
ev.charge()