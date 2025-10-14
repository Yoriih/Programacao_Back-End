# Exercício 3: Soma de Números

# Peça ao usuário para digitar 5 números 

contador = 1                                                   # Inicializa o contador em 0
soma = 0                                                       # Inicializa a soma em 0

# Calcule a soma deles.

while contador <= 5:                                            # Enquanto o contador for menor que 5
    numero = int(input("Digite um número: "))                   # Solicita ao usuário um número inteiro
    soma = soma + numero                                        # Adiciona o número à soma
    contador = contador + 1                                     # Incrementa o contador em 1
print("Soma até agora:", soma)                                  # Imprime a soma atual

