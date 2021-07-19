from vehicle import Vehicle


class CarWithExtras(Vehicle):

    def __init__(self, TOP_SPEED=60):
        # call constructor from superclass via super()
        super().__init__(TOP_SPEED, model="BMW i8")
        self.bus_driver = "john"

    def update_driver(self, name):
        self.bus_driver = name


busOne = CarWithExtras()

busOne.get_report()
busOne.add_warnings("Oil filter needs to be changed")
busOne.get_report()
busOne.remove_warnings("Oil filter needs to be changed")
busOne.get_report()
busOne.remove_warnings("Faulty Error Code")
busOne.get_report()
print(busOne)
