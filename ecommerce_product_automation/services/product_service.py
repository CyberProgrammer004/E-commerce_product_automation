class ProductService:
    def add_product(self, products, product):
        products.append(product)

    def remove_product(self, products, product_id):
        for product in products:
            if product.id == product_id:
                products.remove(product)
                return products

        return 'Product not found'

    def update_product(self, products, product_id):
        for product in products:
            if product.id == product_id:
                new_name = input('New name: ')
                new_price = input('New price: ')
                new_category = input('New category: ')
                new_stock = input('New stock: ')
                new_supplier = input('New supplier: ')
                product.name = new_name
                product.price = new_price
                product.category = new_category
                product.stock = new_stock
                product.supplier = new_supplier

    def search_product(self, products, product_id):
        for product in products:
            if product.id == product_id:
                return product

        return 'Product not found'

    def list_products(self, products):
        if len(products) == 0:
            return 'No products found'

        print('===LIST of PRODUCTS===')
        for product in products:
            print(product.id)
            print(product.name)
            print(product.price)
            print(product.category)
            print(product.stock)
            print(product.supplier)
            print('-='*20)

    def find_product_by_category(self, products, category):
        pass

    def low_stock_products(self, products):
        for product in products:
            if product.stock < 10:
                print(f'Low stock product:{product}')

    def products_by_category(self, products, category):
        result = []

        for product in products:
            if product.category == category:
                result.append(product)
        return result

    def total_stock_value(self, products):
        total = 0
        for product in products:
            total += product.price * product.stock
            print(f'Total: {total}')
        return total

    def find_product_by_supplier(self, products, supplier):
        result = []

        for product in products:
            if product.supplier == supplier:
                result.append(product)
        return result

    def avarege_price(self, products):
        total = 0
        count = 0

        for product in products:
            total += product.price
            count += 1
        avarege = total / count
        print(f'Avarege: {avarege}')
        return avarege

