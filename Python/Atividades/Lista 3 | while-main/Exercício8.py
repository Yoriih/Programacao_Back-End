# Exercício 8: Sequência de Fibonacci

#F1=1 | F2=1 | F3=F1+F2=2 | F4=F2+F3=3 | F5=F3+F4=5
#F6=F4+F5=8 | F7=F5+F6=13 | F8=F6+F7=21 
contador = 0                                                                # Inicializa o contador em 0
f1 = 0
f2 = 1

# Peça ao usuário para digitar um número 

numero = int(input("Digite quantos números da sequência de Fibonacci quer saber: "))  # Solicita ao usuário um número inteiro

# Mostre os primeiros números dessa sequência.

while contador <= numero:                                                   # Enquanto o contador for menor ou igual ao número
    proximo = f1 + f2                                                       # Calcula o próximo número da sequência
    f1 = f2                                                                 # Atualiza f1 para o valor de f2
    f2 = proximo                                                            # Atualiza f2 para o próximo número da sequência
    print(f"{proximo}")                                                     # Imprime o próximo número da sequência
    contador = contador + 1                                                 # Incrementa o contador em 1