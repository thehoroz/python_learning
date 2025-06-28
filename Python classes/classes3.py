from classes2 import Car

class ElectricCar(Car):
    def __init__(self, make, model, mileage, batterysize):
        super().__init__(make, model, mileage)
        self.batterysize = batterysize
        self.charge_level = 0
        self.battery_health = 100

    def __str__(self) -> str:
        return f"{self.make} {self.model} with {self.mileage}km mileage, Battery: {self.batterysize}kWh"
    
    def charge(self, amount):
        self.charge_level += amount
        if self.charge_level > 100:
            self.charge_level = 100

    def show_battery_status(self):
        print(f"Battery: {self.batterysize}kWh - Charge: {self.charge_level}%")

    def update_mileage(self, upd_mileage):
        super().update_mileage(upd_mileage)
        if self.mileage >= 30000:
            self.battery_health = 70
        else:
            self.battery_health = 100 - self.mileage / 1000

    def show_battery_health(self):
        print(f"Battery health: {self.battery_health}%")

tesla_model3 = ElectricCar("Tesla", "Model 3", 0, 82)
tesla_model3.show_service_history()
tesla_model3.charge(150)
tesla_model3.show_battery_status()
tesla_model3.update_mileage(10000)
tesla_model3.update_mileage(15000)
tesla_model3.update_mileage(14000)
tesla_model3.update_mileage(18000)
tesla_model3.show_battery_health()