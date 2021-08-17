from .pizza import Pizza


class ProsciuttoPizza(Pizza):

    def __init__(self):
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)

    def get_description(self):
        return "Pizza Prosciutto with ham and mushrooms"

    def get_cost(self):
        return 8.50
