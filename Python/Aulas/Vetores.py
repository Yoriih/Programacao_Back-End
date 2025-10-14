# ARRAIS OU VETORES EM PYTHON
# [] - são usados para criar ou acessar elementos de lista (vetores) em Python.
# append - é para adicionar elementos a lista dos vetores.
# sort - organiza os elementos da lista em ordem crescente ou alfabética, dependendo do conteúdo.
# pop - exclui um elemento da lista.
# insert - insere um elemento no vetor.
# for i in range(): - loop para coletar dados.
# Cria a lista vazia de irá armazenar os dados das comissões dos funcionários

comissoes = []
# Loop que, neste caso, roda apenas 1 vez (poderia ser auemntado para mais funcionários)
for i in range(1):
    nome = input("Digite o nome do funcionário: ")
    comissao1 = float(input("Digite a sua comissão no primeiro mês: ").replace(",", ".").strip())
    comissao2 = float(input("Digite a sua comissão no segundo mês: ").replace(",", ".").strip())
    
# Calcula a média
media = (comissao1 + comissao2) / 2

# Adiciona os dados coletados á lista 'comissoes' no formato de dicionário
comissoes.append({
    "nome": nome,
    "Comissão 1": comissao1,
    "Comissão 2": comissao2,
    "Média": media
})
print("\n--- Resultado Final ---")

# Inicia um novo loop que percorre cada comissão da lista comissões

for comissao in comissoes:
    print(f"{comissao['nome']} - Comissão 1: {comissao['Comissão 1']} | Comissão 2: {comissao['Comissão 2']} | Média: {comissao['Média']:.2f}")
