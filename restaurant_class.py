class Restaurant:
    """Beskriva saker om restauranger och deras typ av kök"""

    def __init__(self, restaurant_name, cuisine_type):
        """Ta in parameter för vilken namn och typ av kök restaurangen har"""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is a {self.cuisine_type} restaurant, called {self.restaurant_name}!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently open")

my_restaurant = Restaurant('KumbaYa', 'African')

print(f"We have a new place in town it's calle {my_restaurant.restaurant_name}")
print(f"It serves {my_restaurant.cuisine_type} food")

my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()
