# Exercício 4: Tabuada

# Peça ao usuário para digitar um número 
contador = 1
numero = int(input("Digite um número: "))           # Solicita ao usuário um número inteiro

# Mostre a tabuada desse número (de 1 a 10).

while contador <= 10:                               # Enquanto o contador for menor ou igual a 10
    resultado = numero * contador                   # Calcula o resultado da multiplicação
    print(f"{numero} x {contador} = {resultado}")   # Imprime a tabuada
    contador = contador + 1                         # Incrementa o contador em 1
