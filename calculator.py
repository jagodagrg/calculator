import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator_substract_and_divide(arg1, arg2):
    if intro == 2:
        logging.info("Odejmuję %d od %d" % (arg2, arg1))
        result = arg1 - arg2
    if intro == 4:
        logging.info("Dzielę %d przez %d" % (arg1, arg2))
        result = arg1 / arg2
    logging.info(f"Wynik to {result}")

def calculator_add_and_multiply(arguments):
    if intro == 1:
        calculations = "Dodaję liczby: "
        for argument in arguments:
            calculations = (calculations + f"{argument} ")
        logging.info(calculations)
        result = sum(arguments)
    if intro == 3:
        calculations = "Mnożę liczby: "
        result = 1
        for argument in arguments:
            calculations = (calculations + f"{argument} ")
            result = result * argument
        logging.info(calculations)
    logging.info(f"Wynik to {result}")

if __name__ == "__main__":
    intro = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    if intro == 2 or intro == 4:
        arg1 = int(input("Podaj pierwszą liczbę: "))
        arg2 = int(input("Podaj drugą liczbę: "))
        calculator_substract_and_divide(arg1, arg2)        
    if intro == 1 or intro == 3:
        arguments = []
        while True:
            try:
                argument = int(input("Podaj liczbę, którą chcesz poddać działaniu lub zaakceptuj pustą wartość, by wykonać obliczenie :"))
                arguments.append(argument)
            except ValueError:
                break
        calculator_add_and_multiply(arguments)