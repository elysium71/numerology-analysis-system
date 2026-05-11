from datetime import datetime  # A combination of a date and a time

def is_valid_date(date_str):
    """
    Check if the given date string is a valid date in the format DD-MM-YYYY.
    
    :param date_str: str, date in the format 'DD-MM-YYYY'
    :return: bool, True if valid date, False otherwise
    """
    try:
        # Attempt to parse the date string
        datetime.strptime(date_str, "%d-%m-%Y")
        return True  # If no exception, it's a valid date
    except ValueError:
        return False  # If ValueError is raised, the date is invalid

def calculate_lucky_number(birthday):
    """
    Calculate the lucky number for a given birthday.
    :param birthday: str, in the format 'DD-MM-YYYY'
    :return: int, the lucky number or "Invalid Date" for invalid dates
    """
    if not is_valid_date(birthday):
        return "Invalid Date"  # Use is_valid_date for validation

    # Sum digits of day, month, and year
    day, month, year = birthday.split('-')
    lucky_number = sum(int(digit) for digit in day) + \
                   sum(int(digit) for digit in month) + \
                   sum(int(digit) for digit in year)

    # Reduce to single digit unless it's a master number
    while lucky_number > 9 and not is_master_number(lucky_number):
        lucky_number = sum(int(digit) for digit in str(lucky_number))

    return lucky_number

def determine_lucky_animal(lucky_number):
    """
    Determine the lucky animal based on the lucky number.
    :param lucky_number: int, the lucky number
    :return: str, the lucky animal
    """
    if lucky_number < 1 or lucky_number > 33:
        return "Unknown Animal"  # Edge case for numbers outside expected range
    
    animals = {
        1: "Parrot", 2: "Rabbit", 3: "Elephant", 4: "Beetles",
        5: "Bears", 6: "Deer", 7: "Crane", 8: "Horse",
        9: "Fish", 11: "Dolphin", 22: "Lion", 33: "Turtle"
    }
    return animals.get(lucky_number, "Unknown Animal")

def is_master_number(lucky_number):
    """
    Check if a lucky number is a master number.
    :param lucky_number: int, the lucky number
    :return: bool, True if it is a master number, False otherwise
    """
    return lucky_number in {11, 22, 33}

def find_generation(birthday):
    """
    Determine the generation of a person based on their birth year.
    :param birthday: str, in the format 'DD-MM-YYYY'
    :return: str, the generation name or "Invalid Date" for invalid dates
    """
    if not is_valid_date(birthday):
        return "Invalid Date"  # Use is_valid_date for validation

    year = int(birthday.split('-')[2])
    generation_map = {
        range(1901, 1946): "Silent Generation",
        range(1946, 1965): "Baby Boomers",
        range(1965, 1980): "Generation X",
        range(1980, 1995): "Millennials",
        range(1995, 2010): "Generation Z",
        range(2010, 2025): "Generation Alpha"
    }

    # Check for out-of-range years
    if year < 1901 or year > 2025:
        return "Invalid Date"

    for year_range, generation in generation_map.items():
        if year in year_range:
            return generation

    return "Unknown Generation"  # Default if no match

def compare_birthdays(birthday1, birthday2):
    """
    Compare the lucky numbers and animals of two birthdays.
    :param birthday1: str, first birthday in the format 'DD-MM-YYYY'
    :param birthday2: str, second birthday in the format 'DD-MM-YYYY'
    :return: str, the comparison result
    """
    if not is_valid_date(birthday1) or not is_valid_date(birthday2):
        raise ValueError("Invalid Date")  # Use is_valid_date for validation
    
    # Calculate lucky numbers and animals for each birthday
    lucky_number1 = calculate_lucky_number(birthday1)
    lucky_number2 = calculate_lucky_number(birthday2)
    animal1 = determine_lucky_animal(lucky_number1)
    animal2 = determine_lucky_animal(lucky_number2)

    # Build a comparison dictionary for clarity
    comparison = {
        "Lucky Numbers": "Same" if lucky_number1 == lucky_number2 else "Different",
        "Lucky Animals": "Same" if animal1 == animal2 else "Different"
    }

    # Format the comparison results
    result = ("Lucky Numbers: " + comparison['Lucky Numbers'],
              "Lucky Animals: " + comparison['Lucky Animals'])

    return result

