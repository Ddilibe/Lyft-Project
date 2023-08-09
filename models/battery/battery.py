from abc import ABC, abstractmethod


class Battery(ABC):

    @abstractmethod
    def needs_service(self, *args, **kwargs):
        pass
