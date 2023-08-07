# from abc import ABC, abstractmethod


# class Car(ABC):
#     def __init__(self, last_service_date):
#         self.last_service_date = last_service_date

#     @abstractmethod
#     def needs_service(self):
#         pass

#!/usr/bin/env python
from models.battery.nubbin import Nubbin
from models.battery.spindler import Spindler
from models.engine.capulet import Capulet
from models.engine.sternman import Sternman
from models.engine.wiloughby import Wiloughby
from models.engine.engine import Engine
from models.battery.battery import Battery
from typing import TypeAlias
from datetime import Date



bat:TypeAlias = Battery
eng:TypeAlias = Engine

def create_car(name: str, *args: list):
    class Car():
        def __init__(battery: bat, engine: eng):
            self.battery, self.engine = battery, engine
            self.start_car(name, args)

        def start_car(string: str, *args):
            cars ={ "calliope": self.create_calliope, "gilssade": self.create_gilssage,
                "palindrome": self.create_palindrome, "rorschach": self.create_rorschach,
                "thovex": self.create_thovex
            }
            car = cars.get(string)(*args)
            self.undergoes_processes()
            return car

        def create_calliope(current_date: Date, last_service_date: Date, current_mileage: int, last_service_mileage: int):
            self.battery = self.battery.__init__(last_service_date, current_date)
            self.engine = self.engine.__init__(last_service_mileage, current_mileage)

        def create_gilssage(current_date: Date, last_service_date: Date, current_mileage: int, last_service_mileage: int):
            self.battery = self.battery.__init__(last_service_date, current_date)
            self.engine = self.engine.__init__(last_service_mileage, current_mileage)

        def create_palindrome(current_date: Date, last_service_date: Date, warning_light_on: bool):
            self.battery = self.battery.__init__(last_service_date, current_date)
            self.engine = self.engine.__init__(warning_light_on)

        def create_rorschach(current_date: Date, last_service_date: Date, current_mileage: int, last_service_mileage: int):
            self.battery = self.battery.__init__(last_service_date, current_date)
            self.engine = self.engine.__init__(last_service_mileage, current_mileage)

        def create_thovex(current_date: Date, last_service_date: Date, current_mileage: int, last_service_mileage: int):
            self.battery = self.battery.__init__(last_service_date, current_date)
            self.engine = self.engine.__init__(last_service_mileage, current_mileage)

        def undergoes_processes(self):
            self.battery.needs_service()
            self.engine.needs_service()
            return False

    cars ={
        "calliope": (Spindler, Capulet),
        "gilssade": (Spindler, Wiloughby),
        "palindrome": (Spindler, Sternman),
        "rorschach": (Nubbin, Wiloughby),
        "thovex": (Nubbin, Capulet),
    }
    new_car = Car(*cars.get(name)[0])
    return new_car
