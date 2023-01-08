class Item ():
  # constructor
  def __init__(self, id, code, name, price):
    self.id = id
    self.code = code
    self.name = name
    self.price = price


# Define an Array of Item object
items = [
  Item(1, "A001", "Oreo", 2),
  Item(2, "A002", "Nutella Biscuits", 2.5),
  Item(3, "A003", "Coca Cola 300 ml", 4),
  Item(4, "A004", "Oman chips", 3),
  Item(5, "A005", "Coffee 350 ml", 5),
  Item(6, "A006", "Pastry", 5.5),
  Item(7, "A007", "Kitkat", 3.5),
  Item(8, "A008", "Water 250 ml", 1),
  Item(9, "A009", "Extra", 2.5),
  Item(10, "A010", "Lays", 4)
]

# Display vending screen messages
print("################  Python Vending Machine   ################### ")
print(f"----------------      Total Items : {len(items)}    ---------------------- \n")

print("Id  | Code  |   Name                      | Price ")
print("---------------------------------------------------")
for x in items:
  print(f"{x.id}  | {x.code}   |   {x.name.ljust(25)} | {x.price}")

balance = 0
loaded = 0
print(f"\nYour balance is {balance}!")

# Ask user to load balance in order to start transaction

response = 'yes'
while response != 'no':
  loaded = float(input("Please enter the amount to load..."))
  balance += loaded
  print(f"{loaded} is added, your current balance is {balance}!")
  response = str(input("do you want to add more money? (yes/no)?"))
  if response == 'no':
    break

  continue

# Now Ask user to make a selection of Items
run = True

while run == True:
  selected_item = ""
  selected_item = str(input("Please enter item code..."))

  item_found = [itm for itm in items if itm.code == selected_item]

  if (len(item_found) <= 0):
    print("Selected Item code is invalid, try again!")
    run = False
  else:
    print(f"You have selected : {item_found[0].name}, price is {item_found[0].price}")

    if (balance >= item_found[0].price):
      print("Dispensing your item ({item_found[0].name} - Price ({item_found[0].price}))...")
      balance -= item_found[0].price
      print(f"Your current balance is {balance}")
    else:
      print("You have insufficient balance!")
run = False