from dk.topdanmark.pythonsampleapplication.calculator import Calculator


def calculator():
    calculator = Calculator()

    print('Addition: ', calculator.addition(1, 2))

if __name__ == "__main__":
    calculator()
