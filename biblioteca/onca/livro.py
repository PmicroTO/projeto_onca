import biblioteca.livros.liv_add as ad
import biblioteca.livros.liv_alt as al
import biblioteca.livros.liv_con as co
import biblioteca.livros.liv_rem as rm


def liv_menu():
    opcao = input(
        " [1]adicionar livros \n [2]alterar livros \n [3]consultar livros \n [4]remover livros"
    )
    opcao = int(opcao)
    if opcao == 1:
        ad.add_entrada()
    elif opcao == 2:
        al.liv_alterar()
    elif opcao == 3:
        co.con_nome("cliente")
    elif opcao == 4:
        rm.liv_apagar()
    else:
        print("Por favor, digite uma alternativa valida...")
        liv_menu()


liv_menu()
