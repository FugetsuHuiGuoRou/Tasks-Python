#Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre
#a seguinte soma:
#S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n

# Lê um valor inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Inicializa a soma
S = 0

# Calcula a soma de 1 + 1/2 + 1/3 + ... + 1/n
for i in range(1, n + 1):
    S += 1 / i

# Mostra o resultado
print(f"O valor da soma S é: {S:.2f}")  # Imprime o resultado formatado com 2 casas decimais e formata com 2f
# o valor resulta em números quebrados