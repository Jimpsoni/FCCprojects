class Category:
  def __init__(self, name):
    self.ledger = []
    self.category = name
    self.balance = 0

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.balance -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, obj):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {obj.category}")
      obj.deposit(amount, f"Transfer from {self.category}")
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.balance - amount >= 0:
      return True
    else:
      return False

  def __repr__(self):
    string = ""

    # Make the title
    stars = int((30 - len(self.category)) / 2)
    string += "*" * stars + self.category + "*" * stars + "\n"

    # Get all the ledger items
    for item in self.ledger:
      info = list(item.items())
      amount, text = info[0][1], info[1][1]
      amount = "{:.2f}".format(amount)

      if len(text) > 23:
        text = text[:23]

      spaces = 30 - len(text + amount)
      text = text + spaces * " " + amount

      string += text + "\n"
    
    string += f"Total: {self.balance}"
    return string

def create_spend_chart(categories):
  # Get the category spendings
  category_spendings = []
  total = 0

  names = []
  
  # Go through all the withdrawals
  for category in categories:
    name = category.category
    names.append(name)
    amount = 0
    for action in category.ledger:
      if action['amount'] < 0:
        amount -= action['amount']
        total -= action['amount']
    category_spendings.append((name, amount))

  category_spendings = list(map(lambda x: int(x[1] / total * 100 / 10) * 10, category_spendings))

  #  Initialize the full chart, here we build the whole thing
  full_chart = "Percentage spent by category\n"

  # Percentage board
  for i in range(10, -1, -1):
    if i == 0:
      layer = "  0|"
    elif i == 10:
      layer = "100|"
    else:
      layer = f" {i}0|"

    for j in category_spendings:
      if j >= i * 10:
        layer += " o "
      else:
        layer += "   "
    full_chart += layer + " \n"

  # Dashed line
  full_chart += "    " + "---" * len(category_spendings) + "-\n"

  # Name part
  longest_name = max(names, key=len)
  for i in range(len(longest_name)):
    layer = "    "
    for name in names:
      try:
        layer += " " + name[i] + " "
      except IndexError:
        layer += "   "

    full_chart += layer + " \n"

  # Return the chart
  return full_chart[:-1]
