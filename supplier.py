# global inventory array
#
# remove stock if stock is empty
# file input for inventory
#
import random

class supplier:
    inventory = [["Apples", 130, 0.75], ["Bananas", 23, 0.67], ["Carrots", 95, 0.56]]
    inventory2 = [[]]
    fileNames = ["SupplierInventory1", "SupplierInventory2", "SupplierInventory3", "SupplierInventory4",
                 "SupplierInventory5", "SupplierInventory6", "SupplierInventory7", "SupplierInventory8",
                 "SupplierInventory9", "SupplierInventory10", "SupplierInventory11", "SupplierInventory12"]

    # set the self stock to be the array, eventually it will take in a file
    def __init__(self):
        self.stock = supplier.fileRead(self)

    def fileRead(self):
        # random.randint(0, len(supplier.fileNames) - 1) replaces 0 but need to rewrite tests before it work
        with open("./Supplier/" + supplier.fileNames[0]) as file:
            inventory2 = [line.split() for line in file]
        for i in inventory2:
            i[1] = int(i[1])
            i[2] = float(i[2])
        return inventory2

    # takes in item name and amount requested
    #
    def purchaseStock(self, item, amount):
        if self.stockAvailable(item, amount):
            if self.removeFromInventory(item, amount):
                return True
            else:
                return False
        else:
            return False

    # checks if the item can be purchased in that amount
    def stockAvailable(self, item, amount):
        for i in self.stock:
            if item in i[0]:
                if i[1] >= amount:
                    return True
                else:
                    return False

    def stockAmountAvailable(self, item):
        for i in self.stock:
            if item in i[0]:
                return item[1]

    # removes from inventory and returns true.
    def removeFromInventory(self, item, amount):
        for i in self.stock:
            if item in i[0]:

                i[1] = i[1] - amount
                if i[1] == 0:
                    self.stock.remove(i)
                return True
        return False

    # returns the price of the item from seller
    def sellerItemPrice(self, item):
        for i in self.stock:
            if item in i[0]:
                return i[2]
        return False

    def availStockAsText(self):
        names = ""
        for i in self.stock:
            names = names + str(i[1]) + " " + i[0] + " at " + str(i[2]) + " each " + "\n"
        return names

    def availStockAsList(self):
        names = list()
        for i in self.stock:
            names.append(i[0])
        return names
