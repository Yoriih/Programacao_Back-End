# Exercício 6: Adivinhar Número

# Pense em um número e faça com que o usuário adivinhe até acertar. 

import random
secreto = random.randint(1, 100)                                # Gera um número aleatório entre 1 e 100
palpite = 0                                                     # Inicializa o palpite do usuário
tentativas = 0                                                  # Inicializa o contador de tentativas

# Forneça dicas se o palpite for muito alto ou muito baixo.

while palpite != secreto:                                       # Enquanto o palpite não for igual ao número secreto
    palpite = int(input("Adivinhe o número entre 1 e 100: "))   # Solicita ao usuário um palpite
    tentativas = tentativas + 1                                 # Incrementa o contador de tentativas

    if palpite < secreto:                                       # Se o palpite for menor que o número secreto
        print("Muito baixo! Tente novamente.")
    elif palpite > secreto:                                     # Se o palpite for maior que o número secreto
        print("Muito alto! Tente novamente.")
    else:                                                       # Se o palpite for igual ao número secreto
        print(f"Parabéns! Você acertou o número {secreto} em {tentativas} tentativas.")
        break                                                   # Encerra o loop
