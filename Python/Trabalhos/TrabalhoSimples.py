# TRABALHO DE CADASTRO E AVALIAÇÃO DE FILMES

cadastros = []
for i in range(3):

   # INPUT DE NOME COM VALIDAÇÃO:
    while True:
        nome = input("Digite o seu nome: ")
        if nome.isalpha():
            print("=======================================================")
            print("Que nome bonito em",nome)
            print("=======================================================")
            break  # Sai do loop se a entrada for válida
        else:
            print("=======================================================")
            print("Vish, deu erro. Digite apenas letras.")
            print("=======================================================")

    # INPUT DE FILME COM VALIDAÇÃO:
    while True:
        filme = input("Digite o nome do filme que assistiu: ")
        if filme != "":
            print("=======================================================")
            print("Que bacana!")
            print("=======================================================")
            break # Sai do loop se a entrada for válida
        else:
            print("=======================================================")
            print("CARACTERES INVÁLIDOS")
            print("=======================================================")

    # INPUT DE NOTA DO FILME COM VALIDAÇÃO:
    nota = float(input("De 0 a 10, Qual nota você daria para o filme? ").replace(",", ".").strip())
    while nota < 0 or nota > 10:
          print("=======================================================")
          print("NOTA INVÁLIDA")
          print("=======================================================")
          nota = float(input("De 0 a 10, Qual nota você daria para o filme? ").replace(",", ".").strip())
          print("=======================================================")

    # ARMAZENANDO NO VETOR:   
    cadastros.append([nome, filme, nota])

print("\n--- DADOS COLETADOS ---")
print("=======================================================")

    # EXIBIR DADOS COLETADOS (3):
for cadastro in cadastros:
        print(f"{cadastro[0]} - FILME: {cadastro[1]} | NOTA DO FILME: {cadastro[2]:.2f}")
        print("=======================================================")


    
    