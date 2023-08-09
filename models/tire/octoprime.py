#!/usr/bin/env python
""" Script for defining the octoprime for the Tire class """
from .tire import Tire
from typing import List


class Octoprime(Tire):

    def __init__(self, new_tire_sensors: List):
        self.new_tire_sensors = new_tire_sensors

    def needs_service(self):
        return True if sum(self.new_tire_sensors) >= 3 else False
