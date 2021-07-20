
from . import Pizza, PizzaFactory, ProsciuttoPizza, HawaiPizza


class NYPizzaFactory(PizzaFactory):

    def order_pizza(self, type: str) -> Pizza:
        if (type == "prosciutto"):
            return ProsciuttoPizza()
        elif(type == "hawai"):
            return HawaiPizza()
        else:
            raise ValueError("No Pizza found")
