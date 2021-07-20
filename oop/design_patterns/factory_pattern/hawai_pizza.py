from .pizza import Pizza


class HawaiPizza(Pizza):

    def __init__(self):
        pass

    def get_description(self):
        return "Pizza Hawai with ham and pineapple"

    def get_cost(self):
        return 8.50
