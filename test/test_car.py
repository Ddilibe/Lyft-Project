import unittest
from datetime import datetime

from car import create_car


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        new_car = create_car("calliope", *car_var)
        self.assertTrue(new_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        new_car = create_car("calliope", *car_var)
        self.assertFalse(new_car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        current_mileage = 30001
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        new_car = create_car("calliope", *car_var)
        self.assertTrue(new_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        current_mileage = 30000
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        new_car = create_car("calliope", *car_var)
        self.assertFalse(new_car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("gilssade", *car_var)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("gilssade", *car_var)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        current_mileage = 60001
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("gilssade", *car_var)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        current_mileage = 60000
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("gilssade", *car_var)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car_var = (today, last_service_date, warning_light_is_on)
        car = create_car("palindrome", *car_var)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car_var = (today, last_service_date, warning_light_is_on)
        car = create_car("palindrome", *car_var)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        warning_light_is_on = True

        car_var = (today, last_service_date, warning_light_is_on)
        car = create_car("palindrome", *car_var)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        warning_light_is_on = False

        car_var = (today, last_service_date, warning_light_is_on)
        car = create_car("palindrome", *car_var)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("rorschach", *car_var)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("rorschach", *car_var)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        current_mileage = 60001
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("rorschach", *car_var)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        current_mileage = 60000
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("rorschach", *car_var)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("thovex", *car_var)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("thovex", *car_var)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        current_mileage = 30001
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("thovex", *car_var)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date.replace(year=last_service_date.year-2)
        current_mileage = 30000
        last_service_mileage = 0

        car_var = (today, last_service_date, current_mileage, last_service_mileage)
        car = create_car("thovex", *car_var)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
