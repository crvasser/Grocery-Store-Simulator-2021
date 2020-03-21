from random import seed
from random import randint

class customer:

    # call to method within store class that first checks for available product
    # if product is available in specified amount, remove product from inventory
    # increase money by amount x product price
    def buyProduct(self, store, money):
        seed(1)
        product = randint(1, len(store.inventory))
        amount = randint(0, min(store.inventory[product][1], 5))
        store.sellProduct(product, amount, money)
