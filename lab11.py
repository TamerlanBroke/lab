
def lab11n1():
    class Restauraht:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine
        def discribe_restaurant(self):
            print(f"В ресторане {self.name} подают блюда {self.cuisine} кухни")
        def open_restaurant(self):
            print(f"{self.name} сейчас открыт!")
    newRestaurant = Restauraht("China Town", "Китайской")
    print(newRestaurant.name)
    print(newRestaurant.cuisine)
    newRestaurant.discribe_restaurant()
    newRestaurant.open_restaurant()
    # lab11n2
    newRestaurant1 = Restauraht("Франция", "Французской")
    newRestaurant2 = Restauraht("Индия", "Индийской")
    newRestaurant3 = Restauraht("Мексика", "Мексиканской")
    newRestaurant1.discribe_restaurant()
    newRestaurant2.discribe_restaurant()
    newRestaurant3.discribe_restaurant()

def lab11n3():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}.")
            print(f"Рейтинг ресторана: {self.rating}")

        def update_rating(self, new_rating):
            self.rating = new_rating



    restaurant1 = Restaurant("Европа", "европейскую", 4.5)
    restaurant1.describe_restaurant()
    restaurant1.update_rating(4.7)
    restaurant1.describe_restaurant()

lab11n1()
