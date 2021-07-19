
from vehicle import Vehicle

# NewCar inherits from Vehicle


class NewCar(Vehicle):

    def honk(self):
        print("honk honk")


car: NewCar = NewCar(160, "Windshield is broken",
                     "Oil level is low", model="Ford Mustang")
car.get_report()
car.add_warnings("Oil filter needs to be changed")
car.get_report()
car.remove_warnings("Oil filter needs to be changed")
car.get_report()
car.remove_warnings("Faulty Error Code")
car.get_report()
print(car)
