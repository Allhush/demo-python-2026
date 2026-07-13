class Product:
    def __init__(self, name, cals, price_per_kg):
        self.name = name
        self.cals = cals
        self.price = price_per_kg

# instance of a product
banana = Product("banana", cals = 200, price_per_kg = 0.77)

tomato = Product("tomato", cals = 110, price_per_kg = 1.50)

print(banana.cals)
print(tomato.price)