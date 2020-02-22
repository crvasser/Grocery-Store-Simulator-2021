import unittest
from supplier import supplier

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier = supplier()

class TestPurchase(TestSupplier):

    def test_purchaseStock(self):
        self.assertEqual(self.supplier.sellerItemPrice("Carrots"), 0.56)

    def test_stockAvailable1(self):
        self.assertTrue(self.supplier.stockAvailable("Carrots", 10))

    def test_stockAvailable2(self):
        self.assertFalse(self.supplier.stockAvailable("Carrots", 100))

    def test_removeFromInventory(self):
        self.assertTrue(self.supplier.removeFromInventory("Carrots", 10))

    def test_sellerItemPrice(self):
        self.assertTrue(self.supplier.sellerItemPrice("Carrots"))
