from money import money


class store:
    inventory = list()
# stored like [PRODUCT, STOCK, PRICE]

    def __init__(self):
        self.inventory = store.inventory

# should first check that there is enough money, then if supplier has enough product
# then call to checkInventory to handle adding to store's stock
    def add(self, product, amount, supplier, userPrice, money):
        if money.getMoney() < supplier.sellerItemPrice(product) * amount:
            print("Cannot afford " + amount + " " + product + "\n")
            return False
        if supplier.stockAvailable(product, amount):
            self.checkInventory(product, amount, userPrice)
            money.setMoney(money.getMoney()-(supplier.sellerItemPrice(product)*amount))
            return True
        else:
            print(str(amount) + " " + str(product) + " not in stock\n")
            return False

    def availStockAsText(self):
        names = ""
        for i in self.inventory:
            names = names + str(i[1]) + " " + i[0] + " at " + str(i[2]) + " each " + "\n"
        return names

# checks if there is an entry in the store's stock for the given product then either creates a new entry
# or updates the existing entry's amount value
    def checkInventory(self, product, amount, userPrice):
        for i in self.inventory:
            if product in i[0]:
                i[1] = i[1] + amount
                return
        self.inventory.append([product, amount, userPrice])



# need init function, init store init inventory array

