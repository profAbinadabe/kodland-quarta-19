import random

elementos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#%"

tamanho = int(input("Digite o comprimento da senha desejada."))

senha = " "

for i in range(tamanho):
    caractere = random.choice(elementos)

    senha = senha + caractere

print(f"O resultado da senha foi: " + senha)
