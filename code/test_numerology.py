import unittest
from numerology_calculator import calculate_lucky_number, determine_lucky_animal, is_master_number, find_generation, compare_birthdays

class TestNumerologyFunctions(unittest.TestCase):

    def setUp(self):
        """Set up resources or data needed for the tests."""
        self.valid_birthday = "09-07-2005"
        self.invalid_birthday = "32-13-2020"
        self.lucky_number_5_birthday = "22-05-2003"
        self.lucky_number_4_birthday = "13-11-1987"
        self.lucky_number_6_birthday = "01-01-2020"
        self.leap_year_birthday = "29-02-2020"
        self.silent_gen_birthday = "31-12-1945"
        self.millennial_birthday = "13-11-1987"
        self.generation_z_birthday = "09-07-2005"

    def test_calculate_lucky_number(self):
        """Test the calculate_lucky_number function."""
        self.assertEqual(calculate_lucky_number(self.valid_birthday), 5)
        self.assertEqual(calculate_lucky_number(self.lucky_number_4_birthday), 4)
        self.assertEqual(calculate_lucky_number(self.lucky_number_5_birthday), 5)
        self.assertEqual(calculate_lucky_number(self.lucky_number_6_birthday), 6)

    def test_determine_lucky_animal(self):
        """Test the determine_lucky_animal function."""
        self.assertEqual(determine_lucky_animal(5), "Bears")
        self.assertEqual(determine_lucky_animal(9), "Fish")
        self.assertEqual(determine_lucky_animal(11), "Dolphin")
        self.assertEqual(determine_lucky_animal(33), "Turtle")

    def test_is_master_number(self):
        """Test the is_master_number function."""
        self.assertTrue(is_master_number(11))
        self.assertTrue(is_master_number(22))
        self.assertTrue(is_master_number(33))
        self.assertFalse(is_master_number(5))

    def test_find_generation(self):
        """Test the find_generation function."""
        self.assertEqual(find_generation(self.silent_gen_birthday), "Silent Generation")
        self.assertEqual(find_generation(self.millennial_birthday), "Millennials")
        self.assertEqual(find_generation(self.generation_z_birthday), "Generation Z")
        self.assertEqual(find_generation("31-12-1994"), "Millennials")

    def test_compare_birthdays(self):
        """Test the compare_birthdays function."""
        result = compare_birthdays(self.valid_birthday, self.millennial_birthday)
        self.assertIn("Lucky Numbers: Different", result)
        self.assertIn("Lucky Animals: Different", result)

        result = compare_birthdays(self.lucky_number_5_birthday, self.lucky_number_5_birthday)
        self.assertIn("Lucky Numbers: Same", result)
        self.assertIn("Lucky Animals: Same", result)

    def tearDown(self):
        """Clean up any resources or reset state after tests."""
        # No resources need to be cleaned up in this case, but you can put any cleanup code here if needed.
        pass

if __name__ == '__main__':
    unittest.main()

