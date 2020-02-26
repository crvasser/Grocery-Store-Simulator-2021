from supplier import supplier
import unittest

supplier = supplier()
print(supplier.sellerItemPrice("Carrots"))
print(supplier.stockAvailable("Carrots", 10))
print(supplier.removeFromInventory("Carrots", 10))
print(supplier.purchaseStock("Carrots", 75))
print(supplier.purchaseStock("Carrots", 85))
print(supplier.purchaseStock("Apples", 130))
print(supplier.availStockAsText())
print(supplier.availStockAsList())
print("success test")




class supplierTest:
    def test(self):
        self.assertEqual(supplier.sellerItemPrice("carrot"), 0.57)
