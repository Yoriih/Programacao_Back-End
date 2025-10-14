# Desafio 
# Crie um programa que tenha um menu com as opções de cadastrar e exibir dados.

print("Deseja cadastrar seus dados?")
menu = int(input("1- Cadastrar 2- Não Cadastrar 3- Finalizar menu: "))

if menu == 1:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        print("Cadastro realizado com sucesso!")
elif menu == 2:
        print("Cadastro não realizado.")

elif menu == 3:
        print("Finalizando o menu.")
           
else:
        print("Opção inválida. Tente novamente.")


while True:
    menu == 1
    print("Deseja exibir seus dados?")
    dados = int(input("1- Exibir dados 2- Não exibir dados: "))
   
    if dados == 1:
        print(f"Nome: {nome}, Idade: {idade}")
        print("Dados exibidos com sucesso!")
    elif dados == 2:
        print("Dados não exibidos.")
        print("Finalizando o menu.")
    else:
        print("Opção inválida. Tente novamente.")
    break

    




