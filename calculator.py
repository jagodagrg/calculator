import logging
logging.basicConfig(level=logging.DEBUG)


def calculator_add(arguments):
    calculations = "Adding numbers: "
    result = 0
    for argument in arguments:
        calculations = calculations + f"{argument} "
        result += argument
    logging.info(calculations)
    logging.info(f"The result is {result}")


def calculator_subtract(arg1, arg2):
    logging.info("Subtracting %d from %d" % (arg2, arg1))
    result = arg1 - arg2
    logging.info(f"The result is {result}")


def calculator_multiply(arguments):
    calculations = "Multiplying numbers: "
    result = 1
    for argument in arguments:
        calculations = calculations + f"{argument} "
        result *= argument
    logging.info(calculations)
    if len(arguments) == 0:
        result = 0
    logging.info(f"The result is {result}")


def calculator_divide(arg1, arg2):
    logging.info("Dividing %d by %d" % (arg1, arg2))
    result = arg1 / arg2
    logging.info(f"The result is {result}")


if __name__ == "__main__":
    intro = int(input(
        "Select an operation using a number: 1 Add, 2 Subtract, 3 Multiply, 4 Divide: "))
    if intro == 1 or intro == 3:
        arguments = []
        while True:
            try:
                argument = int(input(
                    "Select a number you want to use for the opeartion or press enter to finish and get the result :"))
                arguments.append(argument)
            except ValueError:
                break
        if intro == 1:
            calculator_add(arguments)
        else:
            calculator_multiply(arguments)
    if intro == 2 or intro == 4:
        arg1 = int(input("Selected the first number: "))
        arg2 = int(input("Selected the second number: "))
        if intro == 2:
            calculator_subtract(arg1, arg2)
        else:
            calculator_divide(arg1, arg2)
