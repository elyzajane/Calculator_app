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
        raise ValueError("Invalid operation!")