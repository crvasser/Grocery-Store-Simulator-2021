from money import money

string = raw_input("type start to begin game, type quit to quit")
if 'quit' in string:
    quit()
if 'start' in string:
    print("game has begun")
    a = money(2000)
    print(a.get_money())
    # supplier = supplier.init()
    # store = store.init()
    #vwhile():
       #  string = input("type product (amount) to add item to stock")
        # if string[0] in supplier.getProduce():
           # if isinstance(string[1],'int'):
              #  store.add(string[0], string[1])
