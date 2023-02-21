import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(50, 100)

    def test_init_creates_all_attributes(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive(self):
        self.vehicle.drive(20)
        self.assertEqual(25, self.vehicle.fuel)

    def test_refuel_with_fuel_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(60)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_fuel_less_than_capacity(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(20)
        self.assertEqual(45, self.vehicle.fuel)

    def test_represent_method(self):
        result = f"The vehicle has 100 " \
               f"horse power with 50 fuel left and 1.25 fuel consumption"
        expected_result = str(self.vehicle)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
