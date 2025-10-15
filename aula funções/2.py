import os
os.system ("cls")

def calendario():
    meses = {
        1: ("janeiro", 31),
        2: ("fevereiro", 28),
        3: ("março", 29),
        4: ("abril", 30),
        5: ("maio", 31),
        6: ("junho", 30),
        7: ("julho", 31),
        8: ("agosto", 30),
        9: ("setembro", 30),
        10: ("outubro", 31),
        11: ("novembro", 29),
        12: ("dezembro", 31),
    }

    if 1<= calendario <=12:
        nome, dias = meses [calendario]
        print (f"{nome} tem {dias} dias")

mes = int(input("Digite o mês em número: "))
calendario (mes)

