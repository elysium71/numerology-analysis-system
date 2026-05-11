from numerology_calculator import * 

# Function to get a valid birthday input
def get_birthday_input(prompt="Enter your birthday (DD-MM-YYYY): "):
    while True:
        birthday = input(prompt)
        if is_valid_date(birthday):  # Validate date format
            return birthday
        print("Invalid date format. Please try again.")

# Handle the calculation of lucky number and animal
def handle_lucky_number_and_animal():
    birthday = get_birthday_input()
    try:
        lucky_number = calculate_lucky_number(birthday)
        animal = determine_lucky_animal(lucky_number)
        print("Lucky Number: " + str(lucky_number))
        print("Lucky Animal: " + animal)
    except ValueError as e:
        print("Error: " + str(e))

# Handle checking if a number is a master number
def handle_master_number_check():
    try:
        number = int(input("Enter a number to check: "))
        if is_master_number(number):
            print(str(number) + " is a master number!")
        else:
            print(str(number) + " is not a master number.")
    except ValueError:
        print("Please enter a valid number.")

# Handle checking the user's generation based on their birthday
def handle_generation_check():
    birthday = get_birthday_input()
    try:
        generation = find_generation(birthday)
        print("Generation: " + generation)
    except ValueError as e:
        print("Error: " + str(e))

# Handle comparing two birthdays
def handle_birthday_comparison():
    birthday1 = get_birthday_input("Enter the first birthday (DD-MM-YYYY): ")
    birthday2 = get_birthday_input("Enter the second birthday (DD-MM-YYYY): ")
    try:
        comparison = compare_birthdays(birthday1, birthday2)
        print(comparison)
    except ValueError as e:
        print("Error: " + str(e))

# Main function for the program menu
def main():
    print("Welcome to the Numerology Calculator!")
    while True:
        print("\nChoose an option:")
        print("1. Calculate lucky number and animal")
        print("2. Check if a number is a master number")
        print("3. Find generation based on birth year")
        print("4. Compare two birthdays")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            handle_lucky_number_and_animal()
        elif choice == "2":
            handle_master_number_check()
        elif choice == "3":
            handle_generation_check()
        elif choice == "4":
            handle_birthday_comparison()
        elif choice == "5":
            print("Thank you for using the Numerology Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


