from battery import Battery
from datetime import Date



class Spindler(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if (self.current_date - self.last_service_date) >= 4:
            return True