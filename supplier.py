# global inventory array

# need init function, initialize class and inventory array

# need purchase stock function, checks if stock is available and removes it from inventory array
# TODO
# Figure out how the inventory will work, Array or file? - currently use a static array, later import file
# Purchase Stock
# Stock Availability
# Remove from Inventory



class supplier:
    inventory = [["Apples", 130, 0.75], ["banana", 23, 0.67], ["carrot", 95, 0.56]]

    # set the self stock to be the array, eventually it will take in a file
    def __init__(self):
        self.stock = supplier.inventory

    # takes in item name and amount requested
    #
    def purchaseStock(self, item, amount):
        if self.stockAvailable(self, item, amount):
            return self.removeFromInventory(self, item, amount)

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

    # returns the price of the item from seller
    def sellerItemPrice(self, item):
        for i in self.stock:
            if item in i[0]:
                return i[2]
