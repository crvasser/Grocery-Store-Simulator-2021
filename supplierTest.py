from supplier import supplier
import unittest

supplier = supplier()
print(supplier.sellerItemPrice("Carrots"))
print(supplier.stockAvailable("Carrots", 10))
print(supplier.removeFromInventory("Carrots", 10))
print(supplier.purchaseStock("Carrots", 10))



class supplierTest:
    def test(self):
        self.assertEqual(supplier.sellerItemPrice("carrot"), 0.57)
