import biblioteca.sql_bib.bib_cruder as crud
import biblioteca.livros.liv_con as con


def liv_alterar():
    con.con_nome()
    livro = input("Digite o codigo do livro a ser alterado: ")
    coluna = int(
        input(
            "Digite qual coluna deseja alterar: \n [1]Titulo \n [2]Autores \n [3]Ano \n [4]Editora \n [5]Categoria \n [6]ISBN"
        ))
    if coluna == 1:
        alterada = "titulo"
        valor_novo = input("Digite o valor novo para")
    elif coluna == 2:
        alterada = "autores"
        valor_novo = input("Digite o valor novo para")
    elif coluna == 3:
        alterada = "ano"
        valor_novo = input("Digite o valor novo para")
    elif coluna == 4:
        alterada = "editora"
        valor_novo = input("Digite o valor novo para")
    elif coluna == 5:
        alterada = "categoria"
        valor_novo = input("Digite o valor novo para")
    elif coluna == 6:
        alterada = "isbn"
        valor_novo = input("Digite o valor novo para")
    else:
        print("Por favor digite uma opcao valida:")
        liv_alterar()

    sql_command = """UPDATE livros SET {}='{}' WHERE cod_liv={};""".format(
        alterada, valor_novo, livro)
    crud.cruder(sql_command)
