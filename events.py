from random import seed
from random import randint

class events:

    # call to method within store class that first checks for available product
    # if product is available in specified amount, remove product from inventory
    # increase money by amount x product price
    def customerBuyProduct(self, store, money):
        seed(1)
        product = randint(1, len(store.inventory))
        amount = randint(0, min(store.inventory[product][1], 5))
        store.sellProduct(product, amount, money)

    # Reduces the total amount of money by a random amount between (1, 300) dollars to simulate a robbery
    def robberStealMoney(self, money):
        seed(1)
        amount = randint(0, 300)
        money.setMoney(money.getMoney() - amount)

    # Removes a random amount of a random product from the store inventory to simulate a shoplifting event
    def shoplifterStealProduct(self, store):
        seed(1)
        product = randint(0, len(store.inventory))
        amount = randint(0, min(store.inventory[product][1], 5))
        store.removeProduct(product, amount)

