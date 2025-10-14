cadastros = []
total = 0
mais_novo = 0
mais_velho = 0
print("======|CADASTRO DE LIVROS PARA BIBLIOTECA|======")

while True:

    while True:
        # Título do livro
        titulo = input("\nDigite o título do livro: ").strip().title()
        print("=======================================================")

        if not titulo.isalpha():
            print("Título inválido. Informe apenas letras.")
            print("=======================================================")
        else:
            break
        
    while True:
        # Ano de publicação
        ano = input("Informe o ano de publicação do livro: ")
        print("=======================================================")

        if not ano.isdigit():
            print("Ano inválido. Informe apenas números inteiros.")
            print("=======================================================")
        elif ano not in [str(i) for i in range(1500, 2026)]:# str(i) para garantir que o ano seja um número entre 1000 e 2024 e verifica se o ano está no intervalo de 1000 a 2024                                                          
            print("Ano inválido. Informe um ano entre 1500 e 2025.")
            print("=======================================================")
        else:
            ano = int(ano)
            break

    while True:
        # Estado do livro
        estado = input("Informe o estado do livro (Novo/Usado): ").strip().title()
        print("=======================================================")

        if estado not in ["Novo", "Usado"]: 
            print("Estado inválido. Informe 'Novo' ou 'Usado'.")
            print("=======================================================")
        else:
            break

    total += 1
    cadastros.append((titulo, ano, estado))

    while True:
        pergunta = input("Deseja continuar o cadastro? (Sim/Não): ").strip().upper()
        print("=======================================================")

        if pergunta not in ["SIM", "NÃO", "NAO", "S"]: # Melhor que usar elif para cada condição, posso usar uma lista para verificar se a resposta é válida.
            print("Informe Sim ou Não!")
            print("=======================================================")
        else:
            break

    # Quando sair do loop, encerra tudo.
    if pergunta in ["NÃO", "NAO"]:
        print("Encerrando sistema de cadastro...")
        print("=======================================================")
        break

# Exibir os cadastros
print("\n======|CADASTRO DE LIVROS REGISTRADOS|======")

mais_antigo = min(cadastros, key=lambda x: x[1])
print(f"Total de livros cadastrados: {total} Livros")
print(f"Total de livros novos: {sum(1 for _, _, estado in cadastros if estado == 'Novo')} Livros")
print(f"Total de livros usados: {sum(1 for _, _, estado in cadastros if estado == 'Usado')} Livros")
print(f"O livro mais antigo: {mais_antigo[0]} de ({mais_antigo[1]})")


