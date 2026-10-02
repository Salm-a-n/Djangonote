class Car:
    def __init__(self, brand, color, pee):
        self.brand = brand
        self.color = color
        self.pee=pee

    def drive(self):
        print(f"{self.color} {self.brand} is driving!")
    def horn(self):
        print(f"this car {self.brand} has {self.pee} as horn!")
class vandi(Car):
    def __init__(self, brand, color, pee ):
        super().__init__(brand, color, pee)
    def drive(self):
        print(f"this car{self.color} {self.brand} is driving! and it is vandi")


c1 = Car("Tesla", "Red","noooo")
c1.drive()
v1 = vandi("BMW", "Black","ppippiripippi")
v1.drive()
v1.horn()
