class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

blue_car = Car(color="blue", mileage=20_000)
red_car = Car(color="red", mileage=30_000)

for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage:,} miles")


class Category:
  def __init__(self, name):
    self.name = name
    # self.sauce = sauce
    self.ledger = []

food = Category(name="Rice")
auto = Category(name="Auto")
clothing = Category(name="T-Shirt & Trouser")

for cat in (food, auto, clothing):
    print(f"The {cat.name} car has miles")

def withdraw(self, amount, description = ""):
    self.ledger.append({"amount": -amount, "description": description})


def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

    food.deposit(1000, "initial deposit")