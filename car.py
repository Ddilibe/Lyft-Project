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
from models.tire.tire import Tire
from models.tire.carrigan import Carrigan
from models.tire.octoprime import Octoprime
from typing import TypeAlias, List
from datetime import date
import pdb



bat:TypeAlias = Battery
eng:TypeAlias = Engine
tir:TypeAlias = Tire

def create_car(name: str, *args: list):
    # pdb.set_trace()
    class Car():
        def __init__(self, battery: bat, engine: eng, tire: tir, *args, **kwargs):
            self.battery, self.engine, self.tire = battery, engine, tire
            self.start_car(name, *args)

        def start_car(self, string: str, *args):
            cars ={ "calliope": self.create_calliope, "gilssade": self.create_gilssage,
                "palindrome": self.create_palindrome, "rorschach": self.create_rorschach,
                "thovex": self.create_thovex
            }
            # pdb.set_trace()
            car = cars.get(string)(*args)
            return car

        def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensor: List):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(last_service_mileage, current_mileage)
            self.tire = self.tire(tire_sensor)

        def create_gilssage(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensor: List):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(last_service_mileage, current_mileage)
            self.tire = self.tire(tire_sensor)

        def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool, tire_sensor: List):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(warning_light_on)
            self.tire = self.tire(tire_sensor)

        def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensor: List):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(last_service_mileage, current_mileage)
            self.tire = self.tire(tire_sensor)

        def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_sensor: List):
            self.battery = self.battery(last_service_date, current_date)
            self.engine = self.engine(last_service_mileage, current_mileage)
            self.tire = self.tire(tire_sensor)

        def needs_service(self):
            return self.battery.needs_service() or self.engine.needs_service() or self.tire.needs_service()


    cars ={
        "calliope": (Spindler, Capulet, Carrigan),
        "gilssade": (Spindler, Wiloughby, Octoprime),
        "palindrome": (Spindler, Sternman, Carrigan),
        "rorschach": (Nubbin, Wiloughby, Octoprime),
        "thovex": (Nubbin, Capulet, Carrigan),
    }
    # pdb.set_trace()
    new_car = Car(*cars.get(name), *args)
    return new_car
