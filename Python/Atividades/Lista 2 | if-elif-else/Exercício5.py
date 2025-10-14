# Exercício 5: Classificação de Triângulos

# Peça ao usuário os comprimentos dos três lados de um triângulo 

comprimentos = input("INFORME O COMPRIMENTO DOS 3 LADOS DO TRIÂNGULO. OBS:PODE CONTER VIRGULA: ")
virgula = comprimentos.replace(",",".").split()
n1, n2, n3 = map(float, virgula)

# Determine se é equilátero, isósceles ou escaleno.

if n1 == n2 == n3 :
    print("SEU TRIÂNGULO É EQUILÁTERO")

elif (n1 == n2) or (n2 == n3) or (n3 == n1):
    print("SEU TRIÂNGULO É ISÓSCELES")

else:
    print("SEU TRIÂNGULO É ESCALENO ")