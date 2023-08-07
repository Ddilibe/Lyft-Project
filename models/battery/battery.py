from abc import ABC, abstractmethod


class Battery(ABC):

    @abstractmethod
    def need_services(self, *args, **kwargs):
        pass
