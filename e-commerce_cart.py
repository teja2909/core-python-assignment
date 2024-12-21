def calculate_total(car_items):
    if not cart_items:
        return "cart is empty!Price:0"
    total = sum(cart_items.values())
    if len(car_items)>5:
        total*=0.9
    return f"Total price:{total}"
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500,'Mobile':25000,'TV':45000}
print(calculate_total(cart_items))
