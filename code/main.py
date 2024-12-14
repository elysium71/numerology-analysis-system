from numerology_calculator import *

def main():
    print("Welcome to the Numerology Calculator!")  # Display welcome message
    while True:  # Start an infinite loop to keep the menu running
        # Display menu options for the user to choose from
        print("\nChoose an option:")
        print("1. Calculate lucky number and animal")
        print("2. Check if a number is a master number")
        print("3. Find generation based on birth year")
        print("4. Compare two birthdays")
        print("5. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1-5): ")

        # If the user selects option 1, calculate lucky number and animal
        if choice == "1":
            birthday = input("Enter your birthday (DD-MM-YYYY): ")
            try:
                # Calculate lucky number using the birthday input
                lucky_number = calculate_lucky_number(birthday)
                # Determine the corresponding lucky animal based on the lucky number
                animal = determine_lucky_animal(lucky_number)
                print("Lucky Number: " + str(lucky_number))  # Display the lucky number
                print("Lucky Animal: " + animal)  # Display the lucky animal
            except ValueError as e:  # Handle any value errors that occur (e.g., invalid date format)
                print("Error: " + str(e))
        
        # If the user selects option 2, check if a number is a master number
        elif choice == "2":
            try:
                number = int(input("Enter a number to check: "))  # Get the number from the user
                if is_master_number(number):  # Check if the number is a master number
                    print(str(number) + " is a master number!")  # Inform the user if it's a master number
                else:
                    print(str(number) + " is not a master number.")  # Inform the user if it's not a master number
            except ValueError:  # Handle invalid input (non-integer values)
                print("Please enter a valid number.")

        # If the user selects option 3, find the generation based on birth year
        elif choice == "3":
            birthday = input("Enter your birthday (DD-MM-YYYY): ")
            try:
                # Find the generation based on the birthday
                generation = find_generation(birthday)
                print("Generation: " + generation)  # Display the generation
            except ValueError as e:  # Handle any errors (e.g., invalid date format)
                print("Error: " + str(e))

        # If the user selects option 4, compare two birthdays
        elif choice == "4":
            birthday1 = input("Enter the first birthday (DD-MM-YYYY): ")
            birthday2 = input("Enter the second birthday (DD-MM-YYYY): ")
            try:
                # Compare the two birthdays and display the result
                comparison = compare_birthdays(birthday1, birthday2)
                print(comparison)
            except ValueError as e:  # Handle any errors (e.g., invalid date format)
                print("Error: " + str(e))

        # If the user selects option 5, exit the program
        elif choice == "5":
            print("Thank you for using the Numerology Calculator. Goodbye!")  # Display exit message
            break  # Break the loop and exit the program

        else:  # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to start the program

