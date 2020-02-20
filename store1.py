class store:
    inventory = [[], [], []]

    def __init__(self):
        self.inventory = store.inventory

    def add(product, amount, supplier, buyPrice):
        if supplier.purchaseStock(product, amount, buyPrice):
            checkInventory(product, amount)
        else:
            sellPrice = supplier.getPrice(product)
            inventory.append([product, amount, sellPrice])

    def checkInventory(product, amount):
        for i in inventory:
            if product in i[0]:
                i[0][1] = i[0][1] + amount
                return

# need init function, init store init inventory array

# need add stock function, checks if supplier has stock, and if you can afford init
