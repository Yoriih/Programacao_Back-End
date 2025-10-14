cadastro = []
total = 0

print("======|CONTROLE DE VEÍCULOS NA GARAGEM|======") 
while True:

    while True:
        # Modelo do carro
        modelo = input("\nDigite o modelo do carro: ").strip().title()
        print("=======================================================")

        if not modelo.isalpha():
            print("Modelo inválido. Informe apenas letras.")
            print("=======================================================")
        else:
            break

    while True:
        # Dias de estacionamento
        dias = input("Informe quantos dias que o carro ficará no estacionamento: ")
        print("=======================================================")
        if not dias.isdigit():
            print("Valor inválido. Informe apenas números de dias inteiros.")
            print("=======================================================")
        else:
            dias = int(dias)
            break

    total += 1
    cadastro.append((modelo, dias))

    while True:
        pergunta = input("Deseja continuar o cadastro? (Sim/Não): ").strip().upper()
        print("=======================================================")

        if pergunta == "NÃO":
            break
        elif pergunta == "NAO":
            break
        elif pergunta == "S":
            break
        elif pergunta == "SIM":
            break
        elif pergunta.isdigit():
            print("Informe Sim ou Não!")
            print("=======================================================")
        elif pergunta == "":
            print("Informe Sim ou Não!")
            print("=======================================================")
        elif not pergunta.isalpha():
            print("Informe Sim ou Não!")
            print("=======================================================")

    # Quando sair do loop, encerra tudo.
    if pergunta == "NÃO":
        print("Encerrando sistema de cadastro...")
        print("=======================================================")
        break
    elif pergunta == "NAO":
        print("Encerrando sistema de cadastro...")
        print("=======================================================")
        break

print("\n======|RESULTADO FINAL DOS CADASTROS|======")

soma = sum(dias for _, dias in cadastro)
media = soma / len(cadastro)
mais_dias = max(cadastro, key=lambda x: x[1])

print(f"Total de veículos cadastrados: {total} veiculos")
print(f"Média de dias de estacionamento: {media:.2f} dias")
print(f"Veículo com mais dias de estacionamento: {mais_dias[0]} ({mais_dias[1]} dias)")