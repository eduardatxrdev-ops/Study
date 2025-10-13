# def linha (): #criar uma função
#     print('-'*30)

# linha()
# linha()
# linha()
# linha()
# linha()

#def mensagem (msg): #criar uma função com parâmetro
 #   print(msg)
#mensagem ('Olá, Mundo!')

#def soma (a, b): #criar uma função com dois parâmetros
#a = 3
#b = 14 
#r= a + b
#print(r)

#a = 12
#b = 4
#r = a + b

#print(r)

#a = 16
#b = 15
#r = a + b

#print(r)
import os
os.system ("cls")

def soma (a, b): #criar uma função com dois parâmetros
    r = a + b
    print(r)
    
    #programa principal
soma (3, 14)
soma (12, 4)
soma (16, 15)

def subtrai (a, b):
    r = a - b
    print(r)
    
subtrai (10, 5)
subtrai (20, 8)
subtrai (50, 25)

r1 = int(input("Digite o número 01: "))
r2 = int(input("Digite o número 02: "))
soma (r1, r2)
