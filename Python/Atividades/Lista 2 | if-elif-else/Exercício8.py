# Exercício 8: Verificação de Vogal ou Consoante

# Solicite ao usuário para digitar uma letra

letra = input("DIGITE UMA LETRA: ")
vogais = "aeiouAEIOU" 
 
# Determine se é uma vogal ou uma consoante.

if letra in vogais:
    print("É uma vogal!")
else:
    print("É uma consoante!")

