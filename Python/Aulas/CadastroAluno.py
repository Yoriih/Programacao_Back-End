cadastros = []
for i in range(5):
    
    nome = input("Digite o nome do Aluno: ")
    nota1 = float(input("Digite a sua nota da Avaliação 1: ").replace(",", ".").strip())
    nota2 = float(input("Digite a sua nota da Avaliação 2: ").replace(",", ".").strip())
    
    media = (nota1 + nota2) / 2
    
    cadastros.append([nome, nota1, nota2, media])
    
print("\n--- Resultado Final ---")

for cadastro in cadastros:
    print(f"{cadastro[0]} - NOTA AV1: {cadastro[1]} | NOTA AV2: {cadastro[2]} | MÉDIA: {cadastro[3]:.2f}")
    print("=======================================================")
