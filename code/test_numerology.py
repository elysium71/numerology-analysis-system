import unittest
from numerology_calculator import calculate_lucky_number, determine_lucky_animal, is_master_number, find_generation, compare_birthdays


class TestNumerologyFunctions(unittest.TestCase):



    def setUp(self):
        """Set up test cases and shared attributes."""
        self.invalid_birthday = "32-13-2024"  # Invalid date for testing
        self.valid_birthday = "01-06-2001"  # Valid birthday for testing
        self.millennial_birthday = "15-08-1995"  # Millennial generation birthday
        self.lucky_number_5_birthday = "01-06-2005"  # Birthday with lucky number 5
        
        
    def test_calculate_lucky_number(self):
        """Test the calculate_lucky_number function."""
        # Valid test cases (EP)
        self.assertEqual(calculate_lucky_number("01-06-2001"), 1)
        self.assertEqual(calculate_lucky_number("01-06-2003"), 3)
        self.assertEqual(calculate_lucky_number("01-06-2004"), 4)
        self.assertEqual(calculate_lucky_number("01-06-2005"), 5)
        self.assertEqual(calculate_lucky_number("01-06-2006"), 6)
        self.assertEqual(calculate_lucky_number("01-06-2007"), 7)
        self.assertEqual(calculate_lucky_number("01-06-2008"), 8)
        self.assertEqual(calculate_lucky_number("01-06-2009"), 9)
        self.assertEqual(calculate_lucky_number("01-06-2002"), 11)
        self.assertEqual(calculate_lucky_number("13-11-1906"), 22)
        self.assertEqual(calculate_lucky_number("09-09-1905"), 33)
        
        # Invalid test case (EP)
        self.assertEqual(calculate_lucky_number(self.invalid_birthday), "Invalid Date")
        
        # Boundary test cases (BVA)
        self.assertEqual(calculate_lucky_number("01-01-0001"), 3)  # Min boundary
        self.assertEqual(calculate_lucky_number("31-12-9999"), 7)  # Max boundary

    def test_determine_lucky_animal(self):
        """Test the determine_lucky_animal function."""
        # Valid lucky numbers (EP)
        self.assertEqual(determine_lucky_animal(1), "Parrot")
        self.assertEqual(determine_lucky_animal(2), "Rabbit")
        self.assertEqual(determine_lucky_animal(3), "Elephant")
        self.assertEqual(determine_lucky_animal(4), "Beetles")
        self.assertEqual(determine_lucky_animal(5), "Bears")
        self.assertEqual(determine_lucky_animal(6), "Deer")
        self.assertEqual(determine_lucky_animal(7), "Crane")
        self.assertEqual(determine_lucky_animal(8), "Horse")
        self.assertEqual(determine_lucky_animal(9), "Fish")
        self.assertEqual(determine_lucky_animal(11), "Dolphin")
        self.assertEqual(determine_lucky_animal(22), "Lion")
        self.assertEqual(determine_lucky_animal(33), "Turtle")
        
        # Invalid lucky numbers (EP)
        self.assertEqual(determine_lucky_animal(0), "Unknown Animal")
        self.assertEqual(determine_lucky_animal(100), "Unknown Animal")
        
        # Boundary test cases (BVA)
        self.assertEqual(determine_lucky_animal(0), "Unknown Animal")
        self.assertEqual(determine_lucky_animal(44), "Unknown Animal")

    def test_is_master_number(self):
        """Test the is_master_number function."""
        # Valid master numbers (EP)
        self.assertTrue(is_master_number(11))
        self.assertTrue(is_master_number(22))
        self.assertTrue(is_master_number(33))
        
        # Non-master numbers (EP)
        self.assertFalse(is_master_number(5))
        self.assertFalse(is_master_number(8))
        
        # Boundary test cases (BVA)
        self.assertFalse(is_master_number(10))  # Just before master number
        self.assertFalse(is_master_number(12))  # Just after master number

    def test_find_generation(self):
        """Test the find_generation function."""
        # Valid test cases (EP)
        self.assertEqual(find_generation("19-09-1907"), "Silent Generation")
        self.assertEqual(find_generation("19-09-1950"), "Baby Boomers")
        self.assertEqual(find_generation("19-09-1967"), "Generation X")
        self.assertEqual(find_generation("19-09-1987"), "Millennials")
        self.assertEqual(find_generation("19-09-1997"), "Generation Z")
        self.assertEqual(find_generation("19-09-2017"), "Generation Alpha")
        
        # Invalid test cases (EP)
        self.assertEqual(find_generation("01-01-1700"), "Invalid Date")
        self.assertEqual(find_generation("01-01-2100"), "Invalid Date")
        
        # Boundary test cases (BVA)
        self.assertEqual(find_generation("00-01-1901"), "Invalid Date")
        self.assertEqual(find_generation("01-01-1901"), "Silent Generation") 
        self.assertEqual(find_generation("31-12-1901"), "Silent Generation") 
        self.assertEqual(find_generation("32-12-1901"), "Invalid Date")
        
        self.assertEqual(find_generation("00-01-1946"), "Invalid Date")
        self.assertEqual(find_generation("01-01-1946"), "Baby Boomers") 
        self.assertEqual(find_generation("31-12-1964"), "Baby Boomers") 
        self.assertEqual(find_generation("32-12-1964"), "Invalid Date")
        
        self.assertEqual(find_generation("00-01-1965"), "Invalid Date")
        self.assertEqual(find_generation("01-01-1965"), "Generation X") 
        self.assertEqual(find_generation("31-12-1979"), "Generation X")
        self.assertEqual(find_generation("32-12-1979"), "Invalid Date")
        
        self.assertEqual(find_generation("00-01-1980"), "Invalid Date")
        self.assertEqual(find_generation("01-01-1980"), "Millennials") 
        self.assertEqual(find_generation("31-12-1994"), "Millennials")
        self.assertEqual(find_generation("32-12-1994"), "Invalid Date")
        
        self.assertEqual(find_generation("00-01-1995"), "Invalid Date") 
        self.assertEqual(find_generation("01-01-1995"), "Generation Z") 
        self.assertEqual(find_generation("31-12-2009"), "Generation Z")
        self.assertEqual(find_generation("32-12-2009"), "Invalid Date")
        
        self.assertEqual(find_generation("00-01-2010"), "Invalid Date") 
        self.assertEqual(find_generation("01-01-2010"), "Generation Alpha") 
        self.assertEqual(find_generation("31-12-2024"), "Generation Alpha") 
        self.assertEqual(find_generation("32-12-2024"), "Invalid Date") 

    def test_compare_birthdays(self):
        """Test the compare_birthdays function."""
        # Different birthdays (EP)
        result = compare_birthdays(self.valid_birthday, self.millennial_birthday)
        self.assertIn("Lucky Numbers: Different", result)
        self.assertIn("Lucky Animals: Different", result)

        # Same birthdays (EP)
        result = compare_birthdays(self.lucky_number_5_birthday, self.lucky_number_5_birthday)
        self.assertIn("Lucky Numbers: Same", result)
        self.assertIn("Lucky Animals: Same", result)

        # Boundary test cases (BVA)
        result = compare_birthdays("01-01-0001", "31-12-9999")  # Edge case birthdays
        self.assertIn("Lucky Numbers: Different", result)
        self.assertIn("Lucky Animals: Different", result)

if __name__ == '__main__':
    unittest.main()

