class SpecialPrice:

    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

class Product:

    def __init__(self, product_id, name, unit_price):
        self.id = product_id
        self.name = name
        self.price = unit_price
        self.special_price = None

    def add_special_price(self, special_price):
        self.special_price = special_price

class ProductsManager:
    def __init__(self, all_products):
        self.all_products = all_products
    
    def get_product_with_name(self, product_name):
        for product in self.all_products:
            if product.name == product_name:
                return product
        return None
        
class Cart:

    def __init__(self):
        self.cart_items = {}
        self._total_cart_value = 0

    def scan(self, product):
        if product.id in self.cart_items:
            self.cart_items[product.id]["quantity"] += 1
        else:
            self.cart_items[product.id] = {
                "quantity": 1,
                "special_price": product.special_price,
                "normal_price": product.price,
            }

    def calculate_total(self):
        for product_id in self.cart_items:
            cart_item = self.cart_items[product_id]
            item_total_price = 0
            quantity = cart_item["quantity"]
            special_price = cart_item["special_price"]
            normal_price = cart_item["normal_price"]
            if special_price:
                no_of_special_price_groups = quantity // special_price.quantity
                no_of_items_outside_special_price_group = quantity % special_price.quantity
                item_total_price = (no_of_special_price_groups * special_price.price) + (
                    no_of_items_outside_special_price_group * normal_price)
            else:
                item_total_price = quantity * normal_price
            self._total_cart_value += item_total_price
        return self._total_cart_value
