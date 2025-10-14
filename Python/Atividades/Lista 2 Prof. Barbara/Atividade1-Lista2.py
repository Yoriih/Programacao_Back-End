cadastros = []
total = 0

print("REGISTROS DE TURMA")
while True:
    
    while True:
        nome = input("DIGITE O NOME DO ALUNO: ").strip().title()
        print("=========================================")
        
        if not nome.isalpha():
            print("INFORMAÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            print("=========================================")
        else:
            break
    
    while True:    
        nota = input("INFORME A NOTA FINAL DO ALUNO: ")
        print("=========================================")
        
        if not nota.isdigit():
            print("INFORMAÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            print("=========================================")
        else:
            nota = int(nota)
            break
        
    total += 1    
    cadastros.append((nome, nota))
              
    while True:      
        pergunta = input("DESEJA CONTINUAR O CADASTRO? (SIM/NÃO):").strip().upper()
        print("=========================================")
            
        if pergunta == "NÃO":
            break       
        elif pergunta == "NAO":            
            break    
        elif pergunta == "S":
            break
        elif pergunta == "SIM":
            break
        elif pergunta.isdigit():
            print("INFORME SIM OU NÃO!")
            print("=========================================")
        elif pergunta == "":
            print("INFORME SIM OU NÃO!")
            print("=========================================")
        elif not pergunta.isalpha():
            print("INFORME SIM OU NÃO!")
            print("=========================================")
    
    # Quando sair do loop, encerra tudo.    
    if pergunta == "NÃO":
        print("ENCERRANDO SISTEMA DE CADASTRO...")
        print("=========================================")
        break       
    elif pergunta == "NAO":
        print("ENCERRANDO SISTEMA DE CADASTRO...")
        print("=========================================")
        break          
    
print("\n======|RESULTADO FINAL DOS CADASTROS|======")

soma = sum(nota for _,nota in cadastros) 
media = soma / len(cadastros)  
maior_nota = max(cadastros, key= lambda x:x[1])

print(f"FORAM CADASTRADOS UM TOTAL DE {total} DE ALUNOS.")
print(f"A MÉDIA DAS NOTAS DELES FORAM DE: {media:.2f}")
print(f"O ALUNO COM A MAIOR NOTA FOI: {maior_nota[0]} COM {maior_nota[1]}")