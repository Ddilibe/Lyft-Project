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
from datetime import date
import pdb



bat:TypeAlias = Battery
eng:TypeAlias = Engine

def create_car(name: str, *args: list):
    # pdb.set_trace()
    class Car():
        def __init__(self, battery: bat, engine: eng, *args, **kwargs):
            self.battery, self.engine = battery, engine
            self.start_car(name, *args)

        def start_car(self, string: str, *args):
            cars ={ "calliope": self.create_calliope, "gilssade": self.create_gilssage,
                "palindrome": self.create_palindrome, "rorschach": self.create_rorschach,
                "thovex": self.create_thovex
            }
            # pdb.set_trace()
            car = cars.get(string)(*args)
            return car

        def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(last_service_mileage, current_mileage)

        def create_gilssage(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(last_service_mileage, current_mileage)

        def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(warning_light_on)

        def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(last_service_mileage, current_mileage)

        def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(last_service_mileage, current_mileage)

        def needs_service(self):
            if self.battery.needs_service() or self.engine.needs_service():
                return True
            return False

    cars ={
        "calliope": (Spindler, Capulet),
        "gilssade": (Spindler, Wiloughby),
        "palindrome": (Spindler, Sternman),
        "rorschach": (Nubbin, Wiloughby),
        "thovex": (Nubbin, Capulet),
    }
    # pdb.set_trace()
    new_car = Car(*cars.get(name), *args)
    return new_car
