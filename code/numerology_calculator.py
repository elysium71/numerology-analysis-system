def calculate_lucky_number(birthday):
    """
    Calculate the lucky number for a given birthday.
    :param birthday: str, in the format 'DD-MM-YYYY'
    :return: int, the lucky number
    """
    day, month, year = birthday.split('-')

    # Sum digits of day, month, and year
    lucky_number = sum(int(digit) for digit in day) + \
                   sum(int(digit) for digit in month) + \
                   sum(int(digit) for digit in year)

    # Reduce to single digit unless it's a master number
    while lucky_number not in {11, 22, 33} and lucky_number > 9:
        lucky_number = sum(int(digit) for digit in str(lucky_number))

    return lucky_number

def determine_lucky_animal(lucky_number):
    """
    Determine the lucky animal based on the lucky number.
    :param lucky_number: int, the lucky number
    :return: str, the lucky animal
    """
    animals = {
        1: "Parrot", 2: "Rabbit", 3: "Elephant", 4: "Beetles",
        5: "Bears", 6: "Deer", 7: "Crane", 8: "Horse",
        9: "Fish", 11: "Dolphin", 22: "Lion", 33: "Turtle"
    }
    return animals.get(lucky_number, "Unknown")

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
    :return: str, the generation name
    """
    year = int(birthday.split('-')[2])

    generation_map = {
        range(1901, 1946): "Silent Generation",
        range(1946, 1965): "Baby Boomers",
        range(1965, 1980): "Generation X",
        range(1980, 1995): "Millennials",
        range(1995, 2010): "Generation Z",
        range(2010, 2025): "Generation Alpha"
    }

    for year_range, generation in generation_map.items():
        if year in year_range:
            return generation

    return "Unknown Generation"

def compare_birthdays(birthday1, birthday2):
    """
    Compare the lucky numbers and animals of two birthdays.
    :param birthday1: str, first birthday in the format 'DD-MM-YYYY'
    :param birthday2: str, second birthday in the format 'DD-MM-YYYY'
    :return: str, the comparison result
    """
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

