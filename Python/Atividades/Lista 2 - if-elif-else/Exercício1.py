# Exercício 1: Verificação de Número Par ou Ímpar

# Peça ao usuário para digitar um número

numero = int(input("DIGITE UM NÚMERO: "))

# Determine se é par ou ímpar.
# != diferente
# and "e"

 
if numero % 2 == 0 and numero != 0 :
    print("SEU NÚMERO É PAR")

elif numero % 2 == 1 :
  print("SEU NÚMERO É ÍMPAR")

else:
   print("O NÚMERO E ZERO")
    
