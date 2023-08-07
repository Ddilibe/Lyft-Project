#!/usr/bin/env python
""" Script for creating the Sternman engine for the car """

from engine import Engine


class Sternman(Engine):
    """docstring for Sternman"""
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):

