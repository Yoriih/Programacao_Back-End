# Exercício 7: Verificação de Número Divisível por 3 e 5

# Peça ao usuário para digitar um número 

numero = float(input("DIGITE UM NÚMERO, E DIREI SE ELE E DIVISÍL POR 3 E 5 AO MESMO TEMPO: "))

# Verifique se é divisível por 3 e 5 ao mesmo tempo.

if numero % 3 == 0 and numero % 5 == 0:

    print("É DIVISÍVEL POR 3 E 5 AO MESMO TEMPO.")

else:
    
    print("NÃO É DIVISÍVEL AO MESMO TEMPO")
