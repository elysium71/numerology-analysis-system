import unittest
from numerology_calculator import calculate_lucky_number, determine_lucky_animal, is_master_number, find_generation, compare_birthdays, is_valid_date


class TestNumerologyFunctions(unittest.TestCase):

    def setUp(self):
        """Setup resources before each test."""
        self.valid_date = "01-06-2001"
        self.invalid_date = "00-11-2001"
        print("Setup complete.")

    def test_is_valid_date(self):
        """Test the is_valid_date function."""
        test_cases = [
            (self.valid_date, True),
            ("29-02-2020", True),  # Leap year
            ("29-02-2019", False),  # Non-leap year
            ("32-12-2020", False),  # Invalid day
            ("01-13-2020", False),  # Invalid month
            ("31-04-2020", False),  # Invalid day for the month
            (self.invalid_date, False),  # Student name based date

            # BVA testing
            ("01-01-2023", True),  # Boundary for day (lower bound)
            ("31-01-2023", True),  # Boundary for day (upper bound)
            ("32-01-2023", False),  # Boundary beyond valid day
            ("01-01-2023", True),  # Boundary for month (lower bound)
            ("01-12-2023", True),  # Boundary for month (upper bound)
            ("01-13-2023", False),  # Boundary beyond valid month
            ("01-01-1901", True),  # Boundary for year (lower bound)
            ("31-12-2024", True),  # Boundary for year (upper bound)
        ]
        for date, expected in test_cases:
            with self.subTest(date=date):
                self.assertEqual(is_valid_date(date), expected)
    def test_calculate_lucky_number(self):
        """Test the calculate_lucky_number function."""
        test_cases = [
            (self.valid_date,1),
            ("01-06-2001", 1),
            ("01-06-2003", 3),
            ("01-06-2004", 4),
            ("01-06-2005", 5),
            ("01-06-2006", 6),
            ("01-06-2007", 7),
            ("01-06-2008", 8),
            ("01-06-2009", 9),
            ("01-06-2002", 11),
            ("13-11-1906", 22),
            ("09-09-1905", 33),
            (self.invalid_date, "Invalid Date"),
        ]
        for date, expected in test_cases:
            with self.subTest(date=date):
                self.assertEqual(calculate_lucky_number(date), expected)

    def test_determine_lucky_animal(self):
        """Test the determine_lucky_animal function."""
        test_cases = [
            (1, "Parrot"),
            (2, "Rabbit"),
            (3, "Elephant"),
            (4, "Beetles"),
            (5, "Bears"),
            (6, "Deer"),
            (7, "Crane"),
            (8, "Horse"),
            (9, "Fish"),
            (11, "Dolphin"),
            (22, "Lion"),
            (33, "Turtle"),
            (0, "Unknown Animal"),
            (100, "Unknown Animal"),
        ]
        for lucky_number, expected in test_cases:
            with self.subTest(lucky_number=lucky_number):
                self.assertEqual(determine_lucky_animal(lucky_number), expected)

    def test_is_master_number(self):
        """Test the is_master_number function."""
        test_cases = [
            (11, True),
            (22, True),
            (33, True),
            (5, False),
            (8, False),
            
            #BVA test
            (10, False),
            (12, False),  
            (21, False),
            (23, False),  
            (32, False),
            (34, False),  
        ]
        for number, expected in test_cases:
            with self.subTest(number=number):
                self.assertEqual(is_master_number(number), expected)

    def test_find_generation(self):
        """Test the find_generation function."""
        test_cases = [
            (self.valid_date, "Generation Z"),
            ("19-09-1907", "Silent Generation"),
            ("19-09-1950", "Baby Boomers"),
            ("19-09-1967", "Generation X"),
            ("19-09-1987", "Millennials"),
            ("19-09-1997", "Generation Z"),
            ("19-09-2017", "Generation Alpha"),
            ("01-01-1700", "Invalid Date"),
            ("01-01-2100", "Invalid Date"),
            (self.invalid_date, "Invalid Date"),
            ("20-06-2061", "Invalid Date"), #Student ID-based date
            
            # BVA testing
            ("00-01-1901", "Invalid Date"),
            ("01-01-1901", "Silent Generation"),
            ("31-12-1901", "Silent Generation"),
            ("32-12-1901", "Invalid Date"),
            ("00-01-1946", "Invalid Date"),
            ("01-01-1946", "Baby Boomers"),
            ("31-12-1964", "Baby Boomers"),
            ("32-12-1964", "Invalid Date"),
            ("00-01-1965", "Invalid Date"),
            ("01-01-1965", "Generation X"),
            ("31-12-1979", "Generation X"),
            ("32-12-1979", "Invalid Date"),
            ("00-01-1980", "Invalid Date"),
            ("01-01-1980", "Millennials"),
            ("31-12-1994", "Millennials"),
            ("32-12-1994", "Invalid Date"),
            ("00-01-1995", "Invalid Date"),
            ("01-01-1995", "Generation Z"),
            ("31-12-2009", "Generation Z"),
            ("32-12-2009", "Invalid Date"),
            ("00-01-2010", "Invalid Date"),
            ("01-01-2010", "Generation Alpha"),
            ("31-12-2024", "Generation Alpha"),
            ("32-12-2024", "Invalid Date"),
        ]
        for date, expected in test_cases:
            with self.subTest(date=date):
                self.assertEqual(find_generation(date), expected)

    def test_compare_birthdays(self):
        """Test the compare_birthdays function."""
        test_cases = [
            ("31-12-2024", "01-01-2010", "Different"),
            ("03-02-2010", "02-03-2001", "Same"),
        ]
        for date1, date2, expected in test_cases:
            with self.subTest(date1=date1, date2=date2):
                result = compare_birthdays(date1, date2)
                self.assertIn("Lucky Numbers: " + expected, result)
                self.assertIn("Lucky Animals: " + expected, result)
                
    def tearDown(self):
        """Clean up resources after each test."""
        self.default_test_data = None
        print("Teardown complete.")



if __name__ == '__main__':
    unittest.main()


