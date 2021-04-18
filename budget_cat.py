# class Car:
# def __init__(self, color, mileage):
# self.color = color
# self.mileage = mileage

# blue_car = Car(color="blue", mileage=20_000)
# red_car = Car(color="red", mileage=30_000)

# for car in (blue_car, red_car):
#  print(f"The {car.color} car has {car.mileage:,} miles")


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        self.ledger.append({"amount": -amount, "description": description})

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, budget_category):
        self.withdraw(amount, f"Transfer to {budget_category.name}")
        budget_category.deposit(amount, f"Transfer from {self.name}")

    def __str__(self):
        for item in self.ledger:
            item += f"{item['description']}{format(item['amount'], '.2f')}\n"
            item += f"Total: {format(self.get_balance(), '.2f')}"
            return item


food = Category(name="Rice")
auto = Category(name="Auto")
clothing = Category(name="T-Shirt & Trouser")

# food = budget.Category("Food")
# clothing = budget.Category("Clothing")
# auto = budget.Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "Bills")
food.withdraw(15.89, "restaurant and more food for dessert")

food.transfer(500, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto.deposit(1000, "initial deposit")
auto.withdraw(15)

food.deposit(400, "test")
food.transfer(50, clothing)
auto.transfer(250, food)
food.deposit(700, "Another deposit")
print(auto.name, " ", auto.get_balance())
print(clothing.name, " ", clothing.get_balance())
print(food.name, " ", food.get_balance())