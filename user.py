from money import money
from supplier import supplier
from store import store

string = input("type start to begin game, type quit to quit")
if 'quit' in string:
    quit()
if 'start' in string:
    print("game has begun")
    money = money(2000)
    supplier = supplier()
    store = store()
    while 1:
        string = input("type addItem or checkInventory ")
        if 'addItem' in string:
            string = input("(item) (amount) (cost), or quit ")
            strings = string.split()
            if strings[1].isdigit():
                if supplier.stockAvailable(strings[0], int(strings[1])):
                    if strings[2].isdigit():
                        produce = strings[0]
                        amount = int(strings[1])
                        userSellPrice = int(strings[2])
                        store.add(produce, amount, supplier, userSellPrice, money)
        if 'checkInventory' in string:
            print("money = ", money.amount)
            print("inventory = ", store.inventory)


