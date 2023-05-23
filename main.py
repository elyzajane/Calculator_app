from user_interface import UserInterface
from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division

def operate(num1, num2, operation):
    if operation == 1:
        return Addition.execute(num1, num2)
    elif operation == 2:
        return Subtraction.execute(num1, num2)
    elif operation == 3:
        return Multiplication.execute(num1, num2)
    elif operation == 4:
        return Division.execute(num1, num2)
    else:
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