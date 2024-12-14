import unittest
from numerology_calculator import calculate_lucky_number, determine_lucky_animal, is_master_number, find_generation, compare_birthdays

class TestNumerologyFunctions(unittest.TestCase):

    # Test calculate_lucky_number function
    def test_calculate_lucky_number(self):
        self.assertEqual(calculate_lucky_number("09-07-2005"), 5)  # Example from assignment
        self.assertEqual(calculate_lucky_number("13-11-1987"), 4)  # Example from assignment
        self.assertEqual(calculate_lucky_number("22-05-2003"), 5)  # Fixed: Lucky number for this date is 5
        self.assertEqual(calculate_lucky_number("01-01-2020"), 6)  # Test for edge case (1+1+2+0+2+0)

        # Edge cases
        self.assertEqual(calculate_lucky_number("01-01-2000"), 4)  # Single digit date and month
        self.assertEqual(calculate_lucky_number("29-02-2020"), 8)  # Leap year date (valid)
        with self.assertRaises(ValueError):  # Invalid date (non-existent)
            calculate_lucky_number("32-13-2020")
            calculate_lucky_number("29-02-2019")

    # Test determine_lucky_animal function
    def test_determine_lucky_animal(self):
        self.assertEqual(determine_lucky_animal(5), "Bears")  # Lucky number 5
        self.assertEqual(determine_lucky_animal(9), "Fish")   # Lucky number 9
        self.assertEqual(determine_lucky_animal(11), "Dolphin")  # Master number 11
        self.assertEqual(determine_lucky_animal(33), "Turtle")  # Master number 33

        # Edge case: out-of-range lucky number
        self.assertEqual(determine_lucky_animal(44), "Unknown")  # Lucky number out of range

    # Test is_master_number function
    def test_is_master_number(self):
        self.assertTrue(is_master_number(11))  # Master number
        self.assertTrue(is_master_number(22))  # Master number
        self.assertTrue(is_master_number(33))  # Master number
        self.assertFalse(is_master_number(5))  # Not a master number
        self.assertFalse(is_master_number(7))  # Not a master number

        # Edge case: testing for a number that is not a master number but is valid
        self.assertFalse(is_master_number(7))  # Not a master number

    # Test find_generation function
    def test_find_generation(self):
        self.assertEqual(find_generation("09-07-2005"), "Generation Z")  # Year 2005
        self.assertEqual(find_generation("13-11-1987"), "Millennials")   # Year 1987
        self.assertEqual(find_generation("22-05-1963"), "Baby Boomers")  # Year 1963
        self.assertEqual(find_generation("01-01-2000"), "Generation Z")  # Year 2000 (Updated)
        self.assertEqual(find_generation("31-12-1945"), "Silent Generation")  # Year 1945

        # Edge cases for generation boundary years
        self.assertEqual(find_generation("01-01-1945"), "Silent Generation")  # Boundary year for Silent Generation
        self.assertEqual(find_generation("31-12-1994"), "Millennials")  # Boundary year for Millennials
        self.assertEqual(find_generation("01-01-2010"), "Generation Alpha")  # Boundary year for Generation Alpha
        self.assertEqual(find_generation("01-01-2100"), "Unknown Generation")  # Future year (out of range)

        # Edge case: Invalid generation year
        with self.assertRaises(ValueError):
            find_generation("31-02-2000")  # Invalid date in February

    # Test compare_birthdays function
    def test_compare_birthdays(self):
        result = compare_birthdays("09-07-2005", "13-11-1987")
        self.assertIn("Lucky Numbers: Different", result)
        self.assertIn("Lucky Animals: Different", result)

        result = compare_birthdays("22-05-2003", "22-05-2003")
        self.assertIn("Lucky Numbers: Same", result)
        self.assertIn("Lucky Animals: Same", result)

        # Edge case: comparing the same date
        result = compare_birthdays("01-01-2000", "01-01-2000")
        self.assertIn("Lucky Numbers: Same", result)
        self.assertIn("Lucky Animals: Same", result)

        # Edge case: invalid dates in comparison
        with self.assertRaises(ValueError):
            compare_birthdays("32-13-2020", "01-01-2000")  # Invalid date comparison

if __name__ == '__main__':
    unittest.main()


