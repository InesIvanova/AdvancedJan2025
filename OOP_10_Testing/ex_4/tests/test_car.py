from OOP_10_Testing.ex_4.car import Car


from unittest import TestCase, main

class TestCar(TestCase):
    def setUp(self):
        self.car = Car("test", "testov", 10, 50)

    def test_init(self):
        self.assertEqual("test", self.car.make)
        self.assertEqual("testov", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_empty_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
            self.car.make = None
            self.car.make = []

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_set_model_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
            self.car.model = None
            self.car.model = []

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))


    def test_fuel_consumption_0_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_less_than_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))


    def test_fuel_0_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_above_capacity_sets_to_capacity(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.assertEqual(50, self.car.fuel_capacity)

        self.car.refuel(60)

        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_exact_amount_drives(self):
        self.car.fuel_amount = 10

        self.car.drive(100)

        self.assertEqual(0, self.car.fuel_amount)

    def test_drive_left_amount_fuel(self):
        self.car.fuel_amount = 11
        self.car.drive(100)
        self.assertEqual(1, self.car.fuel_amount)

    def test_drive_not_enough_fuel_raises(self):
        self.car.fuel_amount = 1
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))




if __name__ == "__main__":
    main()