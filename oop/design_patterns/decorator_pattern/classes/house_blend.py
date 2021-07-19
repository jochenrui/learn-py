from ..baseclass import Beverage


class HouseBlend(Beverage):

    def __init__(self):
        super(HouseBlend, self).__init__()

    def get_description(self):
        return "house blend"

    def get_cost(self):
        return 1.10
