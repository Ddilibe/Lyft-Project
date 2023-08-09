#!/usr/bin/env python
""" Script for declaring the class for the tire of the car """
from abc import ABC, abstractmethod
from typing import List


class Tire(ABC):

    @abstractmethod
    def needs_service(self):
        pass
