import unittest
from models import Product, Cart, SpecialPrice, ProductsManager


class TestCart(unittest.TestCase):

    def setUp(self):
        # Set up some sample products and a cart for testing
        self.product1 = Product(1, "Product 1", 10)
        self.product2 = Product(2, "Product 2", 20)
        self.product3 = Product(3, "Product 3", 30)
        self.special_price = SpecialPrice(2, 15)
        
        self.products = [self.product1, self.product2, self.product3]
        self.manager = ProductsManager(self.products)
        self.cart = Cart()

    def test_scan_without_special_price(self):
        # Test scanning products without special price
        self.cart.scan(self.product1)
        self.cart.scan(self.product2)
        self.assertEqual(self.cart.calculate_total(), 30)

    def test_scan_with_special_price(self):
        # Test scanning products with special price
        self.product1.add_special_price(self.special_price)
        self.cart.scan(self.product1)
        self.cart.scan(self.product1)
        self.cart.scan(self.product1)
        self.assertEqual(self.cart.calculate_total(), 25)
    
    def test_scan_with_special_price_with_different_products(self):
        # Test scanning products with special price
        self.product1.add_special_price(self.special_price)
        self.product2.add_special_price(SpecialPrice(3, 35))
        self.cart.scan(self.product1)
        self.cart.scan(self.product2)
        self.cart.scan(self.product1)
        self.cart.scan(self.product2)
        self.cart.scan(self.product1)
        self.cart.scan(self.product2)
        self.assertEqual(self.cart.calculate_total(), 60)
        
    def test_get_product_with_name(self):
        # Test getting product by name from product manager
        product = self.manager.get_product_with_name("Product 1")
        self.assertEqual(product, self.product1)

if __name__ == '__main__':
    unittest.main()
