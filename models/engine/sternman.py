#!/usr/bin/env python
""" Script for creating the Sternman engine for the car """

from .engine import Engine


class Sternman(Engine):
    """docstring for Sternman"""
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return True if self.warning_light_on else False

