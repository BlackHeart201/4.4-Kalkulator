while True:
    operation = int(input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    first_number = int(input("Podaj pierwszą liczbę:"))
    second_number = int(input("Podaj drugą liczbę:"))


    def addition(a, b):
        return a + b


    addition_function = addition(first_number, second_number)


    def subtraction(a, b):
        return a - b


    subtraction_function = subtraction(first_number, second_number)


    def division(a, b):
        return a / b


    division_function = division(first_number, second_number)


    def multiplication(a, b):
        return a * b


    multiplication_function = multiplication(first_number, second_number)


    def operation_list(x):
        return {
            1: [addition_function, "Dodawanie"],
            2: [subtraction_function, "Odejmowanie"],
            3: [division_function, "Mnożenie"],
            4: [multiplication_function, "Dzielenie"],
        }[x]

    dictionary_description = operation_list(operation)

    operation_result = dictionary_description[0]
    operation_name = dictionary_description[1]

    print(operation_result)
    # print(operation_name)

""" dict = {
    1: ["a","b"],
    2: ["c","d"]
}

first = dict.get(1)

nazwa = first[1]

print(nazwa) """
