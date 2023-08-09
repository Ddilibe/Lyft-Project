#!/usr/bin/env python
""" Script for defining the carrigan tyre class """
from .tire import Tire
from typing import List


class Carrigan(Tire):

    def __init__(self, new_tire_sensors: List):
        self.new_tire_sensors = new_tire_sensors

    def needs_service(self):
        tire_sensor = [i for i in self.new_tire_sensors if i >= 0.9]
        return True if len(tire_sensor) >= 1 else False
