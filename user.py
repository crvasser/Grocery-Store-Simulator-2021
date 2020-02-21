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
    while (1):
        string = input("type product (amount) to add item to stock")
        strings = string.split()
        if strings[0] in supplier.getProduce():
            if isinstance(strings[1], 'int'):
                if isinstance(strings[2], 'int'):
                    produce = strings[0]
                    amount = strings[1]
                    userSellPrice = strings[2]
                    store.add(produce, amount, supplier, userSellPrice, money)

