# global inventory array

# need init function, initialize class and inventory array

# need purchase stock function, checks if stock is available and removes it from inventory array
# TODO
# Figure out how the inventory will work, Array or file? - currently use a static array, later import file
# Purchase Stock
# Stock Availability
# Remove from Inventory
class Supplier:
    inventory = [["Apples", "banana", "carrot"], [130, 23, 95], [0.75, 0.67, 0.56]]

    # set the self stock to be the array, eventually it will take in a file
    def __init__(self):
        self.stock = Supplier.inventory

    # takes in item name and amount requested
    #
    def purchaseStock(self, item, amount):
        if stockAvailable(self, item, amount):
            removeFromInventory(self, item, amount)

            return

    # checks if the item can be purchased in that amount
    def stockAvailable(self, item, amount):
        if item in self.stock:
            if self.stock[self.stock.index(item)][1] >= amount:
                return True
            else:
                return False
        else:
            return False

    # removes from inventory and returns true.
    def removeFromInventory(self, item, amount):
        return
