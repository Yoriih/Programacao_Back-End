import random

nomes = ["João", "Maria", "Pedro", "Ana", "Carlos"]
while nomes: # enquanto houver nomes

    input(f"\nPressione a tecla Enter para sortear o nome...")
    
    nome_sorteado = random.choice(nomes) # escolhe um nome aleatório da lista
    print(f"\nO nome sorteado foi: {nome_sorteado}")

    nomes.remove(nome_sorteado) # remove o nome sorteado da lista

print("\nTodos os nomes foram sorteados.")