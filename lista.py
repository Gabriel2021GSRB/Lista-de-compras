import os # limpa o terminal

lista = []

while True: #bolco de opções do usuario
    print("selecione uma opção")
    opcao = input("[i] inserir [a] apagar [l] listar: ")

    if opcao == 'i':
        os.system("clear")
        valor = input("Item: ")
        lista.append(valor) #O método append() é um recurso em Python que permite
        #adicionar um elemento ao final de uma lista existente. Essa função é extremamente
        # útil quando você precisa expandir uma lista com mais itens dinamicamente, sem precisar 
        # criar uma nova lista a cada vez
    
    elif opcao == 'a':
        indice_str = input(
            'Escolha um indice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
#todos os except são para tratar futuros erros causados pelo usuario.
        except ValueError:
            print("Por favor digite um numero inteiro")
        except IndexError:
            print("Este indice não existe na lista")
        except Exception:
            print("Erro desconhecido")
    
    elif opcao == 'l':
        os.system("clear")

        if len(lista) == 0: #lista os valores (sempre começando do 0)Len ()
        # é uma função integrada ao Python que é utilizada para obter o número
        # de itens em um determinado objeto, string, array, listas, entre outros.
            print("Nada para listar")

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print("Opção invalida")