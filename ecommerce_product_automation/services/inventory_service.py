class InventoryService:

    def add_stock(self, product, quantity):
        product.stock += quantity
        return product.stock

    def remove_stock(self, product, quantity):
        if product.stock < quantity:
            return 'operation not allowed.'

        product.stock -= quantity
        return product.stock

    def check_stock(self, product):
        return product.stock
