import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while numeros: 

    input(f"\nEnter para sortear o número")
    
    numero_sorteado = random.choice(numeros) 

    print(f"\nnúmero sorteado: {numero_sorteado}")

    numeros.remove(numero_sorteado) 

print("\nTodos os números foram sorteados.")