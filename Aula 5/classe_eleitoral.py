idade = int(input("Digite a sua idade: "))
if idade <= 16:
    print ("Você não pode votar")
elif idade >= 18 and 65 > idade:
    print ("Você pode votar")
elif idade >= 16 and idade < 18 or idade >= 65:
    print ("O voto é opcional para você")
