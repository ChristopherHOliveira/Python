t1 = float(input("Digite uma temperatura qualquer: "))
res = "s"

while res == "s" or res == "S":
    print(f"Para converter {t1} °Celsius para Fahrenheit, digite F.")
    con = input(f"Ou para converter {t1} °Fahrenheit para Celsius, digite C: ")

    while con != "F" and con != "f" and con != "C" and con != "c":
        print("Caractere inválido, digite novamente.")
        print(f"Para converter {t1} °Celsius para Fahrenheit, digite F.")
        con = input(f"Ou para converter {t1} °Fahrenheit para Celsius, digite C: ")

    if con == "F" or con == "f":
        tF = t1 * (9/5) + 32
        print(t1, " °C é igual a ", tF, " °F.")
    elif con == "C" or con =="c":
        tC = (t1 - 32) * (5/9)
        print(t1, " °F é igual a ", tC, " °C.")

    res = input("Deseja continuar? (S/N): ")
    if res == "s" or res == "S":
        t1 = float(input("Digite uma temperatura qualquer: "))