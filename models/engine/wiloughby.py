#!/usr/bin/env python
""" Script for creating the Wiloughby engine for the car """

from engine import Engine


class Wiloughby(Engine):
    """docstring for Wiloughby"""
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
