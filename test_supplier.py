import unittest
from supplier import supplier

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier = supplier()

class TestPurchase(TestSupplier):

    def test_purchaseStock1(self):
        self.assertEqual(self.supplier.sellerItemPrice("Carrots"), 0.56)

    def test_purchaseStock2(self):
        self.assertEqual(self.supplier.sellerItemPrice("Bananas"), 0.67)

    def test_purchaseStock3(self):
        self.assertFalse(self.supplier.sellerItemPrice("coconut"))

    def test_stockAvailable1(self):
        self.assertTrue(self.supplier.stockAvailable("Carrots", 10))

    def test_stockAvailable2(self):
        self.assertFalse(self.supplier.stockAvailable("Carrots", 100))

    def test_removeFromInventory1(self):
        self.assertTrue(self.supplier.removeFromInventory("Apples", 10))

    def test_removeFromInventory2(self):
        self.assertTrue(self.supplier.removeFromInventory("Carrots", 10))

    def test_sellerItemPrice1(self):
        self.assertTrue(self.supplier.sellerItemPrice("Carrots"))

    def test_sellerItemPrice2(self):
        self.assertTrue(self.supplier.sellerItemPrice("Bananas"))
