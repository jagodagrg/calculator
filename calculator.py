import logging
logging.basicConfig(level=logging.DEBUG)


def calculator_add(arguments):
    calculations = "Dodaję liczby: "
    result = 0
    for argument in arguments:
        calculations = calculations + f"{argument} "
        result += argument
    logging.info(calculations)
    logging.info(f"Wynik to {result}")


def calculator_subtract(arg1, arg2):
    logging.info("Odejmuję %d od %d" % (arg2, arg1))
    result = arg1 - arg2
    logging.info(f"Wynik to {result}")


def calculator_multiply(arguments):
    calculations = "Mnożę liczby: "
    result = 1
    for argument in arguments:
        calculations = calculations + f"{argument} "
        result *= argument
    logging.info(calculations)
    if len(arguments) == 0:
        result = 0
    logging.info(f"Wynik to {result}")


def calculator_divide(arg1, arg2):
    logging.info("Dzielę %d przez %d" % (arg1, arg2))
    result = arg1 / arg2
    logging.info(f"Wynik to {result}")


if __name__ == "__main__":
    intro = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    if intro == 1 or intro == 3:
        arguments = []
        while True:
            try:
                argument = int(input("Podaj liczbę, którą chcesz poddać działaniu lub zaakceptuj pustą wartość, by wykonać obliczenie :"))
                arguments.append(argument)
            except ValueError:
                break
        if intro == 1:
            calculator_add(arguments)
        else:
            calculator_multiply(arguments)
    if intro == 2 or intro == 4:
        arg1 = int(input("Podaj pierwszą liczbę: "))
        arg2 = int(input("Podaj drugą liczbę: "))
        if intro == 2:
            calculator_subtract(arg1, arg2)
        else:
            calculator_divide(arg1, arg2)
