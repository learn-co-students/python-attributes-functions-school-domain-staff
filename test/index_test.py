import unittest2 as unittest
from ipynb.fs.full.index import *

class TestObjectAttributes(unittest.TestCase):

    def test_driver_instance_methods_decorators(self):
        new_driver = Driver()
        new_driver.first = "Ron"
        new_driver.last = "Burgundy"
        new_driver.miles_driven = 20
        new_driver.rating = 3.0
        self.assertEqual(new_driver._first, "Ron")
        self.assertEqual(new_driver.first, "Ron")
        self.assertEqual(new_driver._last, "Burgundy")
        self.assertEqual(new_driver.last, "Burgundy")
        self.assertEqual(new_driver._miles_driven, 20)
        self.assertEqual(new_driver.miles_driven, 20)
        self.assertEqual(new_driver._rating, 3.0)
        self.assertEqual(new_driver.rating, 3.0)

    def test_passenger_instance_methods_decorators(self):
        new_passenger = Passenger()
        new_passenger.first = "Melissa"
        new_passenger.last = "Morris"
        new_passenger.email = "melissa.morris@gmail.com"
        self.assertEqual(new_passenger._first, "Melissa")
        self.assertEqual(new_passenger.first, "Melissa")
        self.assertEqual(new_passenger._last, "Morris")
        self.assertEqual(new_passenger.last, "Morris")
        self.assertEqual(new_passenger._email, "melissa.morris@gmail.com")
        self.assertEqual(new_passenger.email, "melissa.morris@gmail.com")
        self.assertEqual(new_passenger.yell_name(), "MELISSA MORRIS")
