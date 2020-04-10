from random import randint
import math


class events:
    worldEvents = ["There was an earthquake in Utah, I wonder how this will change prices!",
                   "Volcanic eruption in the Pacific Rim, prices are sure to shift!",
                   "Global pandemic ensues, the pandemonium is sure to change supplier prices.",
                   "Suppliers are experiencing difficulties in obtaining some items, prices will change.",
                   "Dow Jones index down 2000 points today, suppliers are sure to change their prices.",
                   "Local peewee baseball team hits 5 home runs, wins free pizza for the whole town.",
                   "Gigantic tentacle monster found deep in the ocean, experts are unclear as to how this will affect the world economy.",
                   "Marble racing to take over the world of sports, this will surely shock the market!",
                   "Gorilla escapes zoo enclosure and eats all the bananas in New York, climbs Empire State Building.",
                   "Amateur robotics team accidentally creates AI capable of self thought.",
                   "Novel Superbug is 'just a really nice guy' says doctors.",
                   "World's largest Chia Pet sold for $540,000 at auction.",
                   "Scientists discover new way to create synthetic muscles, babies to bench 150 lbs by the end of this summer.",
                   "History's greatest jewel heist gang arrested, police officers worldwide rejoice.",
                   "Transcontinental scooter track opened, carbon emissions to reduce 40% by the end of next year.",
                   "High tech burger flipping technology developed by Squarepants Inc.",
                   "Mayor Antone Deponte announces free sodie pop to child who brings in the most Box Tops.",
                   "Never before seen movie found in storage, is expected to beat out all superhero movies at box office.",
                   "Gas leak in old house turns out to be century old cow in basement emitting methane.",
                   "MalWart CEO Tim Timothy turns towards teflon as riots break out over best cookware material.",
                   "George Clooney's ego wins Best Supporting Role at this year's movie awards."]

    # call to method within store class that first checks for available product
    # if product is available in specified amount, remove product from inventory
    # increase money by amount x product price
    def customerBuyProduct(self, store, money):
        product = randint(0, len(store.inventory)-1)
        amount = randint(0, 5)
        # prevent customer from paying for products placed at an unreasonably high price
        if store.inventory[product][2] > 5 * store.inventory[product][3]:
            print("PRODUCT COSTS TOO MUCH, CUSTOMER REFUSED TO BUY")
            return 0

        prodName = store.inventory[product][0]
        store.sellProduct(product, amount, money)

        # return product that was purchased
        return prodName

    # Reduces the total amount of money by a random amount between (1, 300) dollars to simulate a robbery
    def robberStealMoney(self, money):
        amount = randint(0, 300)
        money.setMoney(money.getMoney() - amount)

    # Removes a random amount of a random product from the store inventory to simulate a shoplifting event
    def shoplifterStealProduct(self, store):
        if store.inventory > 1:
            product = randint(0, len(store.inventory)-1)
            amount = randint(0, min(store.inventory[product][1], 50))
            store.removeProduct(product, amount)
            return store.inventory[product][0]

    # Randomizes a price change for a product. Will be called by world events call
    def supplierRandomPriceChange(self, supplier):
        event = randint(0, len(self.worldEvents)-1)
        #Change all prices in supplier
        for product in range(len(supplier.stock)):
            amount = math.floor(supplier.stock[product][2])
            dollar = randint(amount*(-1), amount)
            final = round(supplier.stock[product][2] + dollar)
            cents = randint(1, 99)
            final = final + (cents/100)
            if final == 0:
                final = 1.00
            supplier.stock[product][2] = final
        return self.worldEvents[event]
