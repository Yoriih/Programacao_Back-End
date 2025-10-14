cadastro = []
total = 0

print("========| GASTO DE CLIENTE EM LOJA |========")
while True:
    
    # Cliente
    while True:
        cliente = input("\nInforme o nome do cliente: ")
        print("============================================")
        if not cliente.isalpha():
            print("Dados inválidos. Informe um nome!")
            print("============================================")
        else:
            break
            
    # Gasto do cliente
    while True:
        gasto = input("Informe qual foi o total gasto pelo cliente em reais(Apenas valor inteiro):  ")
        print("============================================")
        
        if not gasto.isdigit():
            print("Dados inválidos. Informe o total gasto inteiro!")
            print("============================================")
        else:
            gasto = int(gasto)
            break
    
    total += 1
    cadastro.append((cliente, gasto))
    
    # Pergunta 
    while True:
        pergunta = input("Deseja continuar o cadastro do cliente? (S/N): ").strip().upper()
        print("============================================")
        
        if pergunta not in ["SIM", "S", "NAO", "NÃO", "N"]:
            print("Dados inválidos. Informe 'Sim' ou 'Não': ")
            print("============================================")
        else:
            break
    
    if pergunta in ["NÃO","NAO","N"]:
        print("Encerrando sistema de cadastros...")
        print("============================================")
        break

print("\n========|CADASTROS REALIZADOS|========")

soma = sum(gasto for _, gasto in cadastro)
media = soma / len(cadastro)
maior_gasto = max(cadastro, key=lambda x:x[1])

print(f"Foram cadastrados um total de {total} clientes!")
print(f"O cliente com maior gasto na loja é: {maior_gasto[0]} com um total de R${maior_gasto[1]},00 " )
print(f"Média de gasto foi: {media:.2f}")
