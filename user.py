
string = input("type start to begin game, type quit to quit")
if "quit" in string:
    quit()
if "start" in string:
    print("game has begun")
    supplier = supplier.init()
    store = store.init()
    while():
        string = input("type product (amount) to add item to stock")
        if string[0] in supplier.getProduce():
            store.add(string[0], string[1])