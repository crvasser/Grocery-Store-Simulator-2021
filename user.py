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
        if string[0] in supplier.stock():
            if isinstance(string[1], 'int'):
                if isinstance(string[2], 'int'):
                    produce = string[0]
                    amount = string[1]
                    userSellPrice = string[2]
                    store.add(produce, amount, supplier, userSellPrice, money)

