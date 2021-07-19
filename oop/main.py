from car import Car


def main():
    fordMustang = Car(260, "Fuel is low", model="Ford Mustang GT")
    fordMustang2 = Car(260, "Fuel is low", model="Ford Mustang GT")
    toyotaPrius = Car(170, model="Toyota Prius")

    fordMustang.get_report()
    toyotaPrius.get_report()

    print(fordMustang.__ne__(toyotaPrius))
    print(fordMustang.__eq__(fordMustang2))


if __name__ == '__main__':
    main()
