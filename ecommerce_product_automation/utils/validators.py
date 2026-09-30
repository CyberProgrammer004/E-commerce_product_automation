def validate_price(price):
    if price <= 0:
        return False

    return True

def validate_stock(stock):
    if stock <= 0:
        return False

    return True

def validate_name(name):
    if name == None or name == '':
        return False
    return True

def validate_unique_id(product_id, products):
    for product in products:
        if product.id == product_id:
            return False

    return True  
