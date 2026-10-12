def show_menu():
    print("\n===== CAMPUS UTILITY DESK =====")
    print("1. Quick Calculator")
    print("2. Unit Converter")
    print("3. Study Sprint Checker")
    print("4. Exit")


def quick_calculator():
    print("\n--- Quick Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        elif operator == "*":
            answer = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            answer = num1 / num2
        else:
            print("Invalid operator.")
            return

        print("Answer:", answer)

    except ValueError:
        print("Please enter valid numbers.")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")

    choice = input("Choose a conversion (1 or 2): ")

    if choice == "1" or choice == "2":
        try:
            distance = float(input("Enter the distance: "))

            if distance < 0:
                print("Distance cannot be negative.")
            elif choice == "1":
                print("Distance in miles:", distance * 0.621371)
            else:
                print("Distance in kilometres:", distance / 0.621371)

        except ValueError:
            print("Please enter a valid distance.")
    else:
        print("Invalid conversion choice.")


def study_sprint_checker():
    print("\n--- Study Sprint Checker ---")

    try:
        minutes = int(input("How many minutes do you have to study? "))

        if minutes <= 0:
            print("Enter a positive number of minutes.")
            return

        print("\nChoose your energy level:")
        print("1. Low")
        print("2. Moderate")
        print("3. High")

        energy = input("Enter your choice (1-3): ")

        if energy == "1":
            if minutes < 20:
                print("Suggestion: Review a few important notes.")
            else:
                print("Suggestion: Revise a topic slowly and take breaks.")

        elif energy == "2":
            if minutes < 20:
                print("Suggestion: Review key definitions.")
            else:
                print("Suggestion: Study a topic and answer practice questions.")

        elif energy == "3":
            if minutes < 20:
                print("Suggestion: Solve a challenging question.")
            else:
                print("Suggestion: Practise coding or solve difficult questions.")

        else:
            print("Invalid energy level.")

    except ValueError:
        print("Please enter a whole number of minutes.")


def main():
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            quick_calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            study_sprint_checker()
        elif choice == "4":
            print("Thank you for using Campus Utility Desk. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
