from classes2 import Car

class Battery:
    def __init__(self, batterysize, charge_level, battery_health):
        self.batterysize = batterysize
        self.charge_level = charge_level
        self.battery_health = battery_health
    
    def charge(self, amount):
        self.charge_level += amount
        if self.charge_level > 100:
            self.charge_level = 100

    def battery_degrade_by_km(self, km_driven):
        if km_driven > 0:
            self.battery_health -= km_driven / 1000
            if self.battery_health < 70:
                self.battery_health = 70

    def show_battery_status(self):
        print(f"Battery: {self.batterysize}kWh - Charge: {self.charge_level}%")

    def show_battery_health(self):
        print(f"Battery health: {self.battery_health}%")

class ElectricCar(Car):
    def __init__(self, make, model, mileage, battery):
        super().__init__(make, model, mileage)
        self.battery = Battery(82,100,100)

    def __str__(self) -> str:
        return f"{self.make} {self.model} with {self.mileage}km mileage, Battery: {self.battery}"

    def update_mileage(self, upd_mileage):
        km_driven = upd_mileage - self.mileage
        super().update_mileage(upd_mileage)
        self.battery.battery_degrade_by_km(km_driven)
        self.battery.show_battery_health()

tesla_model3 = ElectricCar("Tesla", "Model 3", 0, 82)
tesla_model3.show_service_history()
tesla_model3.update_mileage(10000)
tesla_model3.update_mileage(15000)
tesla_model3.update_mileage(14000)
tesla_model3.update_mileage(18000)
tesla_model3.update_mileage(38000)