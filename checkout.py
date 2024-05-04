from models import Product, Cart, SpecialPrice, ProductsManager

# Product pricing for this week
product_pricing = {
    'A': {'unit_price': 50, 'special_price': SpecialPrice(3, 130)},
    'B': {'unit_price': 30, 'special_price': SpecialPrice(2, 45)},
    'C': {'unit_price': 20},
    'D': {'unit_price': 15},
}

# Load all products 
all_products = []
for product_name in product_pricing:
    product_info = product_pricing[product_name]
    product_obj = Product(product_name, product_name, product_info['unit_price'])
    if 'special_price' in product_info:
        product_obj.add_special_price(product_info['special_price'])
    all_products.append(product_obj)
product_manager = ProductsManager(all_products)

# Test code 
cart_items_and_total = {
"": 0,
"A": 50,
"AB": 80,
"CDBA": 115,
"AA": 100,
"AAA": 130,
"AAAA": 180,
"AAAAA": 230,
"AAAAAA": 260,
"AAAB": 160,
"AAABB": 175,
"AAABBD": 190,
"DABABA": 190,
}


for products_to_scan, total in cart_items_and_total.items():
    cart = Cart()
    for product_name in products_to_scan:
        product = product_manager.get_product_with_name(product_name)
        cart.scan(product)

    cart_total = cart.calculate_total()
    if total == cart_total:
        status = "Success"
    else:
        status = "Failed"
    print("{}, Expected Total - {}, Actual Total - {}, Test Status - {}".format(products_to_scan, total, cart_total, status))