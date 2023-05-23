class UserInterface:

    def display_warning():
        print("Kindly use the calculator app wisely!")

    def display_options():
        print("Please choose the operation.")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

    def get_operation_choice():
        while True:
            try:
                operation = int(input("Enter your chosen operation (1/2/3/4):"))
                if operation < 1 or operation > 4:
                    raise ValueError
                break
            except ValueError:
                print("An error occurred! Please enter a valid choice (1/2/3/4):")
        return operation
    