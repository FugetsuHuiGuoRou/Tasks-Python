#Faça um programa em Python que imprima os números de 1 a 50 de 1 em 1 e de 52 a
#100 de 2 em 2

for mulher_leopardo in range(1, 51):  # gera números de 1 a 50
    print(f"{mulher_leopardo}")  # imprime o valor atual de mulher_leopardo
    
for homem_aranha in range(52, 101, 2):  # gera números de 52 a 100 com passo 2 (ou seja, apenas os pares)
    print(f"{homem_aranha}")  # imprime o valor atual de homem_aranha
    
