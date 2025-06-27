class Car:

    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.service_history = []

    def __str__(self) -> str:
        return f"{self.make} {self.model} with {self.mileage} km mileage"
    
    def __repr__(self) -> str:
        return f'Car ("{self.make}", "{self.model}", "{self.mileage}")'

    def display(self):
        print(f"The {self.make} model {self.model} has a mileage of: {self.mileage}")

    def update_mileage(self, upd_mileage):
        if upd_mileage > self.mileage:
            self.mileage = upd_mileage

    def add_service_note(self, note):
        self.service_history.append(note)

    def show_service_history(self):
        if len(self.service_history) == 0:
            print("No service history yet")
        else:
            print("This car's service history:")
            for i, item in enumerate(self.service_history, start=1):
                print(f"{i}: {item}")

bmw_116i = Car("BMW", "116i", 75000)
bmw_116i.update_mileage(10000)
bmw_116i.display()
bmw_116i.add_service_note("Oil changed")
bmw_116i.add_service_note("Sparkplugs renewed")
bmw_116i.show_service_history()
print(bmw_116i)