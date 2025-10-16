import os
os.system ("Cls")

def volume (raio, altura):
    π = 3.1414592
    vol = π * raio * raio * altura
    return (vol)


raio = float(input("Digite o Raio do Cilindro: "))
altura = float(input("Digite a altura do Cilindro:"))

vol = volume (raio, altura)
print(f"O volume do cilindro é: {vol:2f}")
