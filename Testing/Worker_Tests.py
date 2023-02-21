from OOP.Testing.Worker import Worker

import unittest


class WokerTests(unittest.TestCase):

    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_energy_incremented_after_rest_method(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_worker_work_with_negative_or_equal_to_zer_energy(self):
        worker = Worker("Test", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
            self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_increased_after_work_with_salary(self):
        self.worker.work()
        self.assertEqual(self.worker.money, self.worker.salary)

    def test_worker_energy_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(9, self.worker.energy)

    def test_get_info(self):
        self.assertEqual('Test has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    unittest.main()
