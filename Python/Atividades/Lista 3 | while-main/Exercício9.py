# Exercício 9: Números Primos

# Solicite um número ao usuário 

numero = int(input("VAMOS VERIFICAR SE SEU NÚMERO É PRIMO: "))

# Variáveis de controle

divisor = 1
quantidade_divisores = 0

# Verifique se ele é primo ou não.

while divisor <= numero:

    if numero % divisor == 0:
        quantidade_divisores += 1
    divisor += 1

if quantidade_divisores == 2:
     print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
