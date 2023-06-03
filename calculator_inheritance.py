from calculations import Calculations

class CalculatorInheritance(Calculations):

    def power (self, base, exponent):
        result = base ^ exponent
        return result
