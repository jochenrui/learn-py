from abc import ABC, abstractmethod
from .pizza import Pizza
from .prosciutto_pizza import ProsciuttoPizza
from .hawai_pizza import HawaiPizza


class PizzaFactory(ABC):

    @abstractmethod
    def order_pizza(self, type: str) -> Pizza:
        pass
