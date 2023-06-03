class UserInterface:

    def display_greeting():
        print("\033[1;35;40m╦ ╦ ╦═╗╦  ╦  ╔═╗")
        print("\033[1;35;40m╠═╣ ╠═ ║  ║  ║ ║")
        print("\033[1;35;40m╩ ╩ ╩═╝╩═╝╩═╝╚═╝")

    def display_warning():
        print("\033[1;31;40mKindly use the calculator app wisely!\033[0m")

    def display_options():
        print("\033[1;33;40mPlease choose the operation.\033[0m")
        print("\033[1;32;40m1. Addition\033[0m")
        print("\033[1;36;40m2. Subtraction\033[0m")
        print("\033[1;34;40m3. Multiplication\033[0m")
        print("\033[1;35;40m4. Division\033[0m")
        print("\033[1;39;40m4. Power\033[0m")

    def get_operation_choice():
        while True:
            try:
                operation = int(input("\033[1;33;40mEnter your chosen operation (1/2/3/4/5): \033[0m"))
                if operation < 1 or operation > 5:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31;40mAn error occurred! Please enter a valid choice (1/2/3/4/5).\033[0m")
        return operation
    
    def get_numbers():
        while True:
            try:
                num1 = float(input("\033[1;33;40mEnter first number: \033[0m"))
                num2 = float(input("\033[1;33;40mEnter second number: \033[0m"))
                break
            except ValueError:
                print("\033[1;31;40mAn error occurred! Please enter valid numbers.\033[0m")
        return num1, num2
    
    def display_result(num1, operator_symbol, num2, result):
        print("\033[1;34;40m{} {} {} = {}\033[0m".format(num1, operator_symbol, num2, result))

    def get_repeat_choice():
        while True:
            try:
                choice = input("\033[1;33;40mDo you want to perform another calculation? (yes/no): \033[0m")
                if choice.lower() == 'yes':
                    return True
                elif choice.lower() == 'no':
                    return False
                else:
                    raise ValueError
            except ValueError:
                print("\033[1;31;40mAn error occurred! Please enter 'yes' or 'no'.\033[0m")
                