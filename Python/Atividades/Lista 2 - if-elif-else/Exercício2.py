# Exercício 2: Maior entre Dois Números

# Solicite dois números

numero1 = int(input("DIGITE SEU PRIMEIRO NÚMERO: "))
numero2 = int(input("DIGITE SEU SEGUNDO NÚMERO: "))

# Determine qual deles é o maior.

if (numero1 > numero2):
    print("O PRIMEIRO NÚMERO E MAIOR")

elif (numero2 > numero1):
    print("O SEGUNDO NÚMERO E MAIOR")
    
else:
    print ("OS NÚMEROS SÃO IGUAIS")
