from store import store
from money import money
from supplier import supplier

testStore = store()
supplier = supplier()
money = money(100)
testStore.add("Apples", 1, supplier, 1, money)

print("PRODUCT: " + testStore.inventory[0][0])
print("AMOUNT: " + testStore.inventory[0][1])
print("PRICE: " + testStore.inventory[0][2])



