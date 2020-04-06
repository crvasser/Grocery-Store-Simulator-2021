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
            print("Cannot afford " + str(amount) + " " + str(product) + "\n")
            return False
        if supplier.stockAvailable(product, amount):
            self.checkInventory(product, amount, userPrice, supplier.sellerItemPrice(product))
            money.setMoney(money.getMoney()-(supplier.sellerItemPrice(product)*amount))
            supplier.purchaseStock(product, amount)
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
    def checkInventory(self, product, amount, userPrice, sellerPrice):
        for i in self.inventory:
            if product in i[0]:
                if userPrice == i[2]:
                    i[1] = i[1] + amount
                    i[3] = sellerPrice
                    return
                else:
                    i[1] = i[1] + amount
                    i[2] = userPrice
                    i[3] = sellerPrice
                    return
        self.inventory.append([product, amount, userPrice, sellerPrice])

# checks that the given store has the requested amount of product
# reduces store inventory for product by amount and increases money by amount x prod. price
    def sellProduct(self, productIndex, amount, money):
        if amount == 0:
            return
        if amount > self.inventory[productIndex][1]:
            amount = self.inventory[productIndex][1]
        self.inventory[productIndex][1] -= amount
        money.setMoney(money.getMoney() + amount*self.inventory[productIndex][2])
        if self.inventory[productIndex][1] == 0:
            self.inventory.remove(self.inventory[productIndex])

# Removes a specified product from the store inventory without adding money
# Used by the shoplifter event
    def removeProduct(self, productIndex, amount):
        if amount == 0:
            return
        if amount > self.inventory[productIndex][1]:
            amount = self.inventory[productIndex][1]
        self.inventory[productIndex][1] -= amount
        if self.inventory[productIndex][1] == 0:
            self.inventory.remove(self.inventory[productIndex])


