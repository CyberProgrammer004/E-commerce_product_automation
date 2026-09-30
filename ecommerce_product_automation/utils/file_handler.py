import csv
import json
from models.product import Product
import inspect

print(inspect.signature(Product))

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        products = []

        for row in reader:
            product = Product(
                int(row['id']),
                row['name'],
                row['category'],
                float(row['price']),
                int(row['stock']),
                row['supplier']
            )
            products.append(product)

    return products

def write_csv(filename, products):
    with open(filename, 'w') as file:
        writer = csv.DictWriter(
            file,
            fieldnames = ['id', 'name', 'category', 'price', 'stock', 'supplier']
        )
        writer.writeheader()
        writer.writerows(products)

def write_json(filename, products):
    with open(filename, 'w') as file:
        json.dump(products, file)
