import os
os.system ("cls")

def fahrenheit_celcius (fahrenheit):
    c = (fahrenheit - 32.0) * (5.0/9.0)
    return c

f = float (input("Digite a Temperatura em Fahrenheit: "))
c = fahrenheit_celcius (f)

print(f"A temperatura em Celcius é: {c:.2f}°C")