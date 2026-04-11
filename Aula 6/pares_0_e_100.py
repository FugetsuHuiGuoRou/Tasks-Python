






# Método 1: usar `range(start, stop, step)` com passo 2 para gerar apenas números pares
for batman in range(0, 101, 2):  # gera 0, 2, 4, ..., 100
	print(f"{batman}")  # imprime o valor atual de batman


# Método 2: iterar por todos os números e filtrar os pares com o operador módulo
for batman in range(101):  # gera 0, 1, 2, ..., 100
	if batman % 2 == 0:  # verifica se o resto da divisão de `batman` por 2 é zero (ou seja, `batman` é par)
		print(f"{batman}")  # imprime batman
  

