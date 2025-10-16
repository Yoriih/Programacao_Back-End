# Exercício 4: Verificação de Número Positivo, Negativo ou Zero

# Solicite um número 

numero = float(input("DIGITE UM NÚMERO POSITIVO, NEGATIVO OU ZERO QUE IREI DESCOBRIR QUAL USOU: "))

# Determine se é positivo, negativo ou zero.

if numero > 0:
    print("SEU NÚMERO E POSITIVO")

elif numero < 0:
    print("SEU NÚMERO E NEGATIVO")

else:
    print("SEU NÚMERO E ZERO")
