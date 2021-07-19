
# multiple inheritance possible
class Vehicle:

    def __init__(self, TOP_SPEED=80, *warnings, model):
        self.TOP_SPEED = TOP_SPEED
        # __prefix for variable = private variable
        self.__warnings: set = set(warnings)
        self.__model: str = model
        self.__passengers: list = []

    # similar to the .toString() method in Java
    def __repr__(self) -> str:
        print('Printing...')
        return f'model: {self.__model}'

    def __eq__(self, other: object):
        if other.__class__ is self.__class__:
            print("potato salad")
            return False
        else:
            return NotImplemented

    def __ne__(self, other: object):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def get_report(self):
        self.get_max_speed()
        self.get_warnings()

    # passes the Car class as "self"
    # self is automatically passed
    def get_max_speed(self):
        print(f'this car drives at max {self.TOP_SPEED} km/h')

    def get_warnings(self):
        for warning in self.__warnings:
            print(f'warning: {warning}')

    def add_warnings(self, *warnings):
        for warning in warnings:
            self.__warnings.add(warning)

    def remove_warnings(self, *warnings):
        for warning in warnings:
            if warning in self.__warnings:
                self.__warnings.remove(warning)

    def add_passenger(self, *passengers):
        for passenger in passengers:
            if passenger in self.__passengers:
                self.__passengers.remove(passenger)
            else:
                self.__passengers.append(passenger)
