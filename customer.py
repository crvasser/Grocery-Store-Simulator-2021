class customer:

    # call to method within store class that first checks for available product
    # if product is available in specified amount, remove product from inventory
    # increase money by amount x product price
    def buyProduct(self, product, amount, store, money):
        store.sellProduct(product, amount, money)
