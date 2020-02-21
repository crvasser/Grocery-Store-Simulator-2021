from money import money
# might not need this if we decided to check the money in the supplier purchaseStock method


class store:
    inventory = [[], [], []]
# stored like [PRODUCT, STOCK, PRICE]

    def __init__(self):
        self.inventory = store.inventory

# should first check that there is enough money, then if supplier has enough product
# then call to checkInventory to handle adding to store's stock
    def add(self, product, amount, supplier, buyPrice):
        if money.getMoney() < buyPrice * amount:
            print("Cannot afford " + amount + " " + product + "\n")
            return
        if supplier.stockAvailable(product, amount):
            sellPrice = supplier.getPrice(product)
            self.checkInventory(product, amount, sellPrice)

            # not sure if we are updating the money here or in supplier
            money.setMoney(money.getMoney()-(buyPrice*amount))
        else:
            print(amount + " " + product + " not in stock\n")

# checks if there is an entry in the store's stock for the given product then either creates a new entry
# or updates the existing entry's amount value
    def checkInventory(self, product, amount, sellPrice):
        for i in self.inventory:
            if product in i[0]:
                i[1] = i[1] + amount
                return
        self.inventory.append([product, amount, sellPrice])

# need init function, init store init inventory array

