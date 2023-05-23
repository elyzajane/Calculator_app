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
                print("An error occurred! Please enter a valid choice (1/2/3/4).")
        return operation
    
    def get_numbers():
        while True:
            try:
                num1 = float(input("Enter first number:"))
                num2 = float(input("Enter second number:"))
                break
            except ValueError:
                print("An error occurred! Please enter valid numbers.")
        return num1, num2
    
    def display_result(num1, operator_symbol, num2, result):
        print("{} {} {} = {}"(num1, operator_symbol, num2, result))

    def get_repeat_choice():
        while True:
            try:
                choice = input("Do you want to perform another calculation? (yes/no):")
                if choice.lower() == 'yes':
                    return True
                elif choice.lower() == 'no':
                    return False
                else:
                    raise ValueError
            except ValueError:
                print("An error occurred! Please enter 'yes' or 'no'.")