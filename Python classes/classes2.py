class Car:

    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    def display(self):
        print(f"The {self.make} model {self.model} has a mileage of: {self.mileage}")

    def update_mileage(self, upd_mileage):
        if upd_mileage > self.mileage:
            self.mileage = upd_mileage

bmw_116i = Car("BMW", "116i", 75000)
bmw_116i.update_mileage(10000)
bmw_116i.display()