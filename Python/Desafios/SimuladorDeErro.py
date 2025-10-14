def menu():
    print("\n=== Simulador de Erros Python ===")
    print("1 - ValueError")
    print("2 - ZeroDivisionError")
    print("3 - TypeError")
    print("4 - IndexError")
    print("5 - KeyError")
    print("6 - FileNotFoundError")
    print("7 - NameError")
    print("8 - AttributeError")
    print("0 - Sair")

def simular_erro(opcao):
    try:
        if opcao == "1":
            int("abc")
        elif opcao == "2":
            resultado = 10 / 0
        elif opcao == "3":
            soma = "texto" + 5
        elif opcao == "4":
            lista = [1, 2, 3]
            print(lista[10])
        elif opcao == "5":
            dicionario = {"nome": "Nicolas"}
            print(dicionario["idade"])
        elif opcao == "6":
            open("arquivo_que_nao_existe.txt")
        elif opcao == "7":
            print(x)  # x não existe
        elif opcao == "8":
            numero = 123
            numero.append(5)
        else:
            print("Opção inválida.")
    except ValueError:
        print("🚫 ValueError: valor inválido para tipo.")
    except ZeroDivisionError:
        print("🚫 ZeroDivisionError: divisão por zero.")
    except TypeError:
        print("🚫 TypeError: operação entre tipos incompatíveis.")
    except IndexError:
        print("🚫 IndexError: índice fora do alcance.")
    except KeyError:
        print("🚫 KeyError: chave inexistente em dicionário.")
    except FileNotFoundError:
        print("🚫 FileNotFoundError: arquivo não encontrado.")
    except NameError:
        print("🚫 NameError: variável não declarada.")
    except AttributeError:
        print("🚫 AttributeError: atributo/método inexistente.")
    except Exception as e:
        print(f"🚫 Outro erro: {type(e).__name__} - {e}")

def main():
    while True:
        menu()
        escolha = input("Escolha um erro para simular (0 para sair): ").strip()
        if escolha == "0":
            print("Encerrando o simulador...")
            break
        simular_erro(escolha)

if __name__ == "__main__":
    main()
