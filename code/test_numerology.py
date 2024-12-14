import unittest
from numerology_calculator import calculate_lucky_number, determine_lucky_animal, is_master_number, find_generation, compare_birthdays

class TestNumerologyFunctions(unittest.TestCase):

    # Test calculate_lucky_number function
    def test_calculate_lucky_number(self):
        self.assertEqual(calculate_lucky_number("09-07-2005"), 5)
        self.assertEqual(calculate_lucky_number("13-11-1987"), 4)
        self.assertEqual(calculate_lucky_number("01-01-2020"), 6)

    # Test determine_lucky_animal function
    def test_determine_lucky_animal(self):
        self.assertEqual(determine_lucky_animal(5), "Bears")
        self.assertEqual(determine_lucky_animal(11), "Dolphin")
        self.assertEqual(determine_lucky_animal(44), "Unknown")  # Out-of-range lucky number

    # Test is_master_number function
    def test_is_master_number(self):
        self.assertTrue(is_master_number(11))
        self.assertFalse(is_master_number(7))

    # Test find_generation function
    def test_find_generation(self):
        self.assertEqual(find_generation("09-07-2005"), "Generation Z")
        self.assertEqual(find_generation("13-11-1987"), "Millennials")
        self.assertEqual(find_generation("31-12-1945"), "Silent Generation")

    # Test compare_birthdays function
    def test_compare_birthdays(self):
        result = compare_birthdays("09-07-2005", "13-11-1987")
        self.assertIn("Lucky Numbers: Different", result)
        self.assertIn("Lucky Animals: Different", result)

        result = compare_birthdays("22-05-2003", "22-05-2003")
        self.assertIn("Lucky Numbers: Same", result)
        self.assertIn("Lucky Animals: Same", result)

if __name__ == '__main__':
    unittest.main()

