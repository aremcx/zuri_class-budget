class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def withdraw(self, amount, description = ""):
    self.ledger.append({"amount": -amount, "description": description})

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  def get_balance(self):
    total = 0
    for item in self.ledger:
      total += item['amount']
    return total

  def transfer(self, amount, budget_category):
    self.withdraw(amount, f"Transfer to {budget_category.name}")
    budget_category.deposit(amount, f"Transfer from {self.name}")

  def __str__(self):
    output = self.name.center(30, "*") + "\n"
    for item in self.ledger:
      output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
    output += f"Total: {format(self.get_balance(), '.2f')}"
    return output


food = budget.Category("Rice")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
