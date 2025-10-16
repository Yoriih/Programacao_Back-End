# Exercício 10: Classificação de Idade

# Solicite a idade do usuário

idade = int(input("DIGITE A SUA IDADE, E DIREI A SUA FAIXA ETÁRIA: "))
 
# Classifique-a em "Criança", "Adolescente", "Adulto Jovem" ou "Adulto".

if idade <= 12 :
    print("Você é uma Criança")

elif 13 <= idade <= 17 :
    print("Você é um Adolescente")

elif 18 <= idade <= 24 :
    print("Você é um apenas um Adulto Jovem")

else:
    print("Você é Adulto")
