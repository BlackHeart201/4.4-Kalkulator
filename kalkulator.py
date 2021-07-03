import logging

logging.basicConfig(level=logging.DEBUG)


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def division(a, b):
    return a / b


def multiplication(a, b):
    return a * b


while True:
    operation = int(input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    first_number = int(input("Podaj pierwszą liczbę:"))
    second_number = int(input("Podaj drugą liczbę:"))


    def operation_list(x):
        return {
            1: [addition(first_number, second_number), "Dodawanie", "Dodaję"],
            2: [subtraction(first_number, second_number), "Odejmowanie", "Odejmuję"],
            3: [multiplication(first_number, second_number), "Mnożenie", "Mnożę"],
            4: [division(first_number, second_number), "Dzielenie", "Dzielę"],
        }[x]


    dictionary_description = operation_list(operation)
    operation_result = dictionary_description[0]
    operation_name = dictionary_description[1]
    operation_function = dictionary_description[2]

    print("{}: {} i {}".format(operation_function, first_number, second_number))
    print("Wynik to: {} ".format(operation_result))
