from ..baseclass import Beverage, CondimentDecorator


class Mocha(CondimentDecorator):

    def __init__(self, beverage: Beverage) -> None:
        super().__init__()
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def get_cost(self) -> float:
        return self.beverage.get_cost() + 0.2
