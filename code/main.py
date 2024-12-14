from numerology_calculator import * 
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
            birthday = input("Enter your birthday (DD-MM-YYYY): ")
            try:
                lucky_number = calculate_lucky_number(birthday)
                animal = determine_lucky_animal(lucky_number)
                print(f"Lucky Number: {lucky_number}")
                print(f"Lucky Animal: {animal}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                number = int(input("Enter a number to check: "))
                if is_master_number(number):
                    print(f"{number} is a master number!")
                else:
                    print(f"{number} is not a master number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            birthday = input("Enter your birthday (DD-MM-YYYY): ")
            try:
                generation = find_generation(birthday)
                print(f"Generation: {generation}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            birthday1 = input("Enter the first birthday (DD-MM-YYYY): ")
            birthday2 = input("Enter the second birthday (DD-MM-YYYY): ")
            try:
                comparison = compare_birthdays(birthday1, birthday2)
                print(comparison)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            print("Thank you for using the Numerology Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
