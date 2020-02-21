from supplier import supplier
import unittest

supplier = supplier()
print(supplier.sellerItemPrice("carrot"))
class supplierTest:
    def test(self):
        self.assertEqual(supplier.sellerItemPrice("carrot"), 0.57)
