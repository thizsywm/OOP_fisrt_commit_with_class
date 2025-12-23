class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print (f'{self.brand} , {self.model} is drive')
    
my_car = Car('Toyota', 'Vios')
my_car.drive()