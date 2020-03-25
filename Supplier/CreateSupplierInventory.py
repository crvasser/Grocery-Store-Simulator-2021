import random


class CreateSupplierInventory:

    OutF = open("SupplierInventory12.txt", "w")
    food = ["Apples", "Bananas", "Oranges", "Bread", "Eggs", "Milk", "Cereal", "Cheese", "Chicken", "Lettuce",
            "Tomatoes", "Potatoes", "Onions", "Grapes", "Watermelon", "Peppers", "Steak", "Ham", "Rice", "Ice Cream",
            "Lemon", "Salt", "Pepper", "Butter", "Fish", "Carrots", "Chips", "Nuts", "Pickles", "Bottled Water", "Ice",
            "Turkey", "Mayonnaise", "Ketchup", "Mustard", "Strawberries", "Blueberries", "Bitconnect", "Beer",
            "Male Order Bride"]
    cost = 0.0
    for line in food:
        cost = random.randint(0, 10) + random.random()
        OutF.write(line)
        OutF.write(" %s %s" % (random.randint(0, 1000), round(cost, 2)))
        OutF.write("\n")

    OutF.close()


