from . import PizzaFactory, NYPizzaFactory, Pizza


class Customer():

    def __init__(self, pizza_place=None):
        self.pizza_place = pizza_place

    def update_pizza_plaze(self, place: str):
        if (place == "NYPizza"):
            self.pizza_place = NYPizzaFactory()

    def order_pizza(self, type: str) -> Pizza:
        if self.pizza_place != None:
            return self.pizza_place.order_pizza(type)
        else:
            print("Please select a pizza place first")
            raise ValueError("No valid pizza")
