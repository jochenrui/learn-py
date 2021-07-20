from decorator_pattern.classes import HouseBlend, Mocha, Soy
from factory_pattern import NYPizzaFactory, Customer


if __name__ == "__main__":
    # decorator pattern
    # hb = HouseBlend()

    # mocha = Mocha(hb)
    # print(mocha.get_description())
    # print(mocha.get_cost())

    # doubleMochaHouseBlend = Mocha(mocha)
    # print(doubleMochaHouseBlend.get_description())

    # doubleMochaSoyHouseBlend = Soy(doubleMochaHouseBlend)
    # print(doubleMochaSoyHouseBlend.get_description())

    # factory pattern
    customer = Customer()
    customer.update_pizza_plaze("NYPizza")
    pizza = customer.order_pizza("hawai")
    print(pizza.get_description())
