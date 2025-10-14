def main ():
    banco = ""
    nome = ""
    conta = "corrente" or "poupança"
    opcao = 0
    
    while True:
        print("========================================")
        print("  MENU DE CADASTRO - SISTEMA BANCÁRIO  ")
        print("========================================")
        print("1.Cadastrar banco")
        print("2.Cadastrar nome do cliente")
        print("3.Cadastrar tipo de conta")
        print("4.Exibir cadastro")
        print("5.Encerrar sistema")
        print("========================================")
        opcao = int(input("Digite uma opção: "))
    #OPÇÃO 1    
        if opcao == 1:
            banco = input("Digite o nome do banco: ")
            print("BANCO CADASTRADO COM SUCESSO!")
        
    #OPÇÃO 2        
        elif opcao == 2:
            nome = input("Digite o nome do cliente: ")
            print("USUÁRIO CADASTRADO COM SUCESSO!")
        
    #OPÇÃO 3            
        elif opcao == 3:
            print("Qual seu tipo de conta? ")
            conta = input("Corrente ou poupança? ")
            print("CONTA CADASTRADA COM SUCESSO!")   
              
    #OPÇÃO 4
        elif opcao == 4:
            if nome == "" or banco == "" or conta == "":
                print("NENHUM CADASTRO ENCONTRADO OU DADOS INCOMPLETOS")
            elif conta != "corrente" and "poupança":
                print("TIPO DE CONTA INVÁLIDA")
            else:
                print("========================================")
                print("DADOS CADASTRADOS COM SUCESSO!")
                print("========================================")
                print(f"Banco: {banco}")
                print(f"Cliente: {nome}")
                print(f"Tipo da conta: {conta}")
                print("========================================")          
    #OPÇÃO 5
        elif opcao == 5:
            print("ENCERRANDO SISTEMA...")
            break
        else:
            print("Opção Inválida")

main()

            