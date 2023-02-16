import biblioteca.livros.liv_add as ad
import biblioteca.livros.liv_alt as al
import biblioteca.livros.liv_con as co
import biblioteca.livros.liv_rem as rm


def liv_menu():
    opcao = input(
        "Digite sua opcao: [1]adicionar, [2]alterar, [3]consultar, [4]remover")
    opcao = int(opcao)
    if opcao == 1:
        ad.add_entrada()
    elif opcao == 2:
        return
    elif opcao == 3:
        co.con_nome
    elif opcao == 4:
        rm.liv_apagar
    else:
        print("Por favor, digite uma alternativa valida...")
        liv_menu()


liv_menu()
