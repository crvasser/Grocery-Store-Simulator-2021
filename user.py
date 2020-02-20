from money import money
from supplier import Supplier
from store1 import store
string = raw_input("type start to begin game, type quit to quit")
if 'quit' in string:
    quit()
if 'start' in string:
    print("game has begun")
    money = money(2000)
    supplier = Supplier()
    store = store.init()
    while():
        string = input("type product (amount) to add item to stock")
        if string[0] in supplier.getProduce():
           if isinstance(string[1],'int'):
              store.add(string[0], string[1], supplier, money)