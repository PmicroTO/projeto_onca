import biblioteca.livros.liv_add as ad
import biblioteca.livros.liv_alt as al
import biblioteca.livros.liv_con as co
import biblioteca.livros.liv_rem as rm


def liv_menu():
    opcao = input(
        "Digite sua opcao: [1]adicionar\n [2]alterar\n [3]consultar\n [4]remover"
    )
    opcao = int(opcao)
    if opcao == 1:
        ad.add_entrada()
    elif opcao == 2:
        al.liv_alterar()
    elif opcao == 3:
        co.con_nome()
    elif opcao == 4:
        rm.liv_apagar()
    else:
        print("Por favor, digite uma alternativa valida...")
        liv_menu()


liv_menu()
