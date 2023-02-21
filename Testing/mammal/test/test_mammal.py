from project.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Test_type", "Tesstt")

    def test_init_creates_all_attributes(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Test_type", self.mammal.type)
        self.assertEqual("Tesstt", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        expected_result = f"Test makes Tesstt"
        self.assertEqual(expected_result, result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected_result = "animals"
        self.assertEqual(expected_result, result)

    def test_info(self):
        result = self.mammal.info()
        expected_result = f"Test is of type Test_type"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()