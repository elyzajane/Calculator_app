from user_interface import UserInterface
from calculations import Calculations

def operate(num1, num2, operation):
    add = Calculations.addition(num1, num2)
    subtract = Calculations.subtraction(num1, num2)
    multiply = Calculations.multiplication(num1, num2)
    divide = Calculations.division(num1, num2)
    
    if operate:
        raise ValueError("\033[1;31;40mInvalid operation!\033[0m")

def calculate():
    UserInterface.display_options()
    operation = UserInterface.get_operation_choice()
    num1, num2 = UserInterface.get_numbers()
    operator_symbol = ""

    if operation == 1:
        result = operate(num1, num2, 1)
        operator_symbol = "+"
    elif operation == 2:
        result = operate(num1, num2, 2)
        operator_symbol = "-"
    elif operation == 3:
        result = operate(num1, num2, 3)
        operator_symbol = "*"
    elif operation == 4:
        result = operate(num1, num2, 4)
        operator_symbol = "/"
    else:
        return

    UserInterface.display_result(num1, operator_symbol, num2, result)

    if UserInterface.get_repeat_choice():
        calculate()
    else:
        print("\033[1;31;40mThank you and have a good day!\033[0m")

def main():
        UserInterface.display_greeting()
        UserInterface.display_warning()
        calculate()

if __name__ == '__main__':
        main()    

