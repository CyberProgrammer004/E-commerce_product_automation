class ReportedService:
    def total_products(self, products):
        total = 0
        for product in products:
            total += 1
        return total

    def total_inventory_value(self, products):
        total = 0
        for product in products:
            total += product.price * product.stock
        return total

    def low_stock_product(self, products, limit):
        result = []
        for product in products:
            if product.stock < limit:
                result.append(product)
        return result

    def most_expencive_product(self, products):
        highest_price = 0
        expencive_product = None

        for product in products:
            if product.price > highest_price:
                highest_price = product.price
                expencive_product = product
        return expencive_product

    def cheapest_product(self, products):
        lowest_price = None
        cheaper_product = None

        for product in products:
            if lowest_price is None or product.price < lowest_price:
                lowest_price = product.price
                cheaper_product = product
        return cheaper_product

    def product_by_category(self, products, category):
        result = []

        for product in products:
            if product.category == category:
                result.append(product)
        return result

    def product_by_supplier(self, products, supplier):
        result = []

        for product in products:
            if product.supplier == supplier:
                result.append(product)
        return result
