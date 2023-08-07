#!/usr/bin/env python
""" Script for creating the capulet engine for the car """

from engine import Engine


class Capulet(Engine):
    """docstring for Capulet"""
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000


