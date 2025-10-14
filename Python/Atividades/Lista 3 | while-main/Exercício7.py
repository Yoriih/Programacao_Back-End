# Exercício 7: Fatorial

# Peça ao usuário para digitar um número 

contador = int(input("Digite um número para calcular o fatorial: "))  # Solicita ao usuário um número inteiro
contador2 = contador                                                  # Armazena o número original para exibir no final
fatorial = 1                                                          # Inicializa o fatorial em 1
# Calcule o fatorial desse número usando um loop.

while contador > 0:                                                   # Enquanto o contador for maior que 0
    fatorial *= contador                                              # Multiplica o fatorial pelo contador
    contador = contador - 1                                           # Decrementa o contador em 1
print(f"O Fatorial de {contador2} é {fatorial}.")                     # Imprime o fatorial atual
