from decorator_pattern.classes import HouseBlend, Mocha, Soy


if __name__ == "__main__":
    # decorator pattern
    hb = HouseBlend()

    mocha = Mocha(hb)
    print(mocha.get_description())
    print(mocha.get_cost())

    doubleMochaHouseBlend = Mocha(mocha)
    print(doubleMochaHouseBlend.get_description())

    doubleMochaSoyHouseBlend = Soy(doubleMochaHouseBlend)
    print(doubleMochaSoyHouseBlend.get_description())
