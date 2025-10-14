# Exercício 9: Cálculo de Desconto com Condição

# Peça ao usuário o valor de um produto

valor = input("DIGITE O VALOR DO PRODUTO E DESCUBRA O VALOR COM DESCONTO: ")
valor = float(valor.replace(",",".").replace("R$","").strip())


# Calcule o valor com desconto apenas se o valor original for maior que R$ 100.


if valor > 100:
    desconto = (20 / 100) * valor
    final = valor - desconto
    print("OLHA SÓ! VOCÊ RECEBEU UM DESCONTO, SEU NOVO VALOR É: R$ {:.2f}".format(final))
else:
    print("QUE PENA...APENAS VALORES ACIMA DE R$100 RECEBE DESCONTO")