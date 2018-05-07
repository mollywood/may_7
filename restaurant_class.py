class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.is_open = "open"

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"The restaurant is {self.is_open}")

pizza_shop = Restaurant("Grimaldis", "pizza")

print(pizza_shop.cuisine_type)
print(pizza_shop.is_open)


pizza_shop.open_restaurant()
pizza_shop.describe_restaurant()
