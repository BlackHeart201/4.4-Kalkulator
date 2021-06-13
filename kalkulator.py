import logging

logging.basicConfig(level=logging.DEBUG)


def operation_list(x):
    return {
        "Dodawanie": 1,
        "Odejmowanie": 2,
        "Mnożenie": 3,
        "Dzielenie": 4,
    }[x]


while True:
    operation = input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

    first_number = float(input("Podaj pierwszą liczbę:"))
    second_number = float(input("Podaj drugą liczbę:"))
    if operation == "1":
        sum_result = first_number + second_number
        logging.debug("Dodaję: ", first_number, " ", "i ", second_number)
        print("Wynik to: ", sum_result)

    elif operation == "2":
        result = first_number - second_number
        logging.debug("Odejmuję: ", first_number, "i ", second_number)
        print("Wynik to: ", result)
    elif operation == "3":
        result = first_number * second_number
        logging.debug("Mnożę: ", first_number, "i ", second_number)
        print("Wynik to: ", result)
    elif operation == "4":
        if second_number == 0:
            print("Nie dziel przez zero!")
        else:
            result = first_number / second_number
            logging.debug("Dzielę: ", first_number, "przez ", second_number)
            print("Wynik to: ", result)
    else:
        print("Brak funkcji dla podanej wartości")
