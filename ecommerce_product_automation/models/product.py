class Product:
    def __init__(self, id, name, price, category, stock, supplier):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        self.supplier = supplier

    def __str__(self):
        return (f'ID: {self.id} | Name: {self.name} | Price: {self.price} | Category: {self.category} '
                f'| stock: {self.stock} | Supplier: {self.supplier}')
