#!/usr/bin/env python
""" Script for creating the default class for the engine """


from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def needs_service(self):
        pass
