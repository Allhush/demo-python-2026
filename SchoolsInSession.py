class Product:
    def __init__(self, name, cals, price_per_kg):
        self.name = name
        self.calories = cals
        self.price = price_per_kg

    def do_something(self):
        print(f"this is a {self.name}")

# instance of a product
banana = Product("banana", cals= 200, price_per_kg = 0.77)

tomato = Product("tomato", cals = 110, price_per_kg = 1.50)

print(banana.calories)
print(tomato.price)
tomato.do_something()