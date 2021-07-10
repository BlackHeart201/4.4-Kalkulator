import logging

logging.basicConfig(level=logging.DEBUG)


def addition(a: int, b: int):
    return a + b


def subtraction(a: int, b: int):
    return a - b


def division(a: int, b: int):
    return a / b


def multiplication(a: int, b: int):
    return a * b


def operation_list(x: int):
    return {
        1: [addition, "Dodawanie", "Dodaję"],
        2: [subtraction, "Odejmowanie", "Odejmuję"],
        3: [multiplication, "Mnożenie", "Mnożę"],
        4: [division, "Dzielenie", "Dzielę"],
    }[x]


while True:
    operation = int(input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    first_number = int(input("Podaj pierwszą liczbę:"))
    second_number = int(input("Podaj drugą liczbę:"))


    def operation_list(x):
        return {
            1: [addition, "Dodawanie", "Dodaję"],
            2: [subtraction, "Odejmowanie", "Odejmuję"],
            3: [multiplication, "Mnożenie", "Mnożę"],
            4: [division, "Dzielenie", "Dzielę"],
        }[x]


    dictionary_description = operation_list(operation)
    operation_result = dictionary_description[0](first_number, second_number)
    operation_name = dictionary_description[1]
    operation_function = dictionary_description[2]

    print("{}: {} i {}".format(operation_function, first_number, second_number))
    print("Wynik to: {} ".format(operation_result))
