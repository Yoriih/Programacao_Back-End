# Exercício 5: Números Pares entre Intervalo

# Solicite dois números ao usuário 

contador = 0                                            # Inicializa o contador em 0
numero1 = int(input("Digite o primeiro número: "))      # Solicita ao usuário o primeiro número inteiro
numero2 = int(input("Digite o segundo número: "))       # Solicita ao usuário o segundo número inteiro


# Mostre todos os números pares entre esses dois valores.

while numero1 <= numero2:                               # Enquanto o primeiro número for menor ou igual ao segundo número
    if numero1 % 2 == 0:                                # Se o número for par
        print(numero1)                                  # Imprime o número par
    numero1 = numero1 + 1                               # Incrementa o primeiro número em 1   
