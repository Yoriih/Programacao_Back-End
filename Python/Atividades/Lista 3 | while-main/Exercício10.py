# Exercício 10: Média de Notas com Condição de Saída
# Peça ao usuário para digitar notas até que ele digite um valor negativo. 
# Calcule e mostre a média das notas digitadas.

# Inicializa variáveis para somar as notas e contar quantas foram digitadas
soma = 0
quantidade = 0

# Pede a primeira nota

entrada = input("Digite uma nota (valor negativo para sair): ").replace(",", ".").strip()
nota = float(entrada)

# Loop enquanto a nota for válida (não-negativa)

while nota >= 0:                  
     soma = soma + nota
     quantidade = quantidade +1
     entrada = input("Digite outra nota (valor negativo para sair): ").replace(",", ".").strip()
     nota = float(entrada)
  
# Fora do while: aqui você pode calcular a média e exibir o resultado
# Lembre de verificar se pelo menos uma nota foi digitada antes de calcular

if quantidade > 0:
     media = soma / quantidade
     print(f"A média é {media}.")     
else:
     print("Você não digitou um valor válido")
     

