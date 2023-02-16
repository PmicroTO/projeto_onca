from ..sql.bib_cruder import cruder
import datetime


def add_isbn(isbn):
    isbn = isbn.strip()
    isbn = isbn.replace("-", "")
    if isbn.isnumeric() is True and len(isbn) == 13:
        return isbn
    else:
        isbn = input(
            "Digite o ISBN no formato correto, e.g. '978-3-16-148410-0': ")
        add_isbn(isbn)


def add_titulo(titulo):
    titulo = titulo.strip()
    if len(titulo) <= 255:
        return titulo
    else:
        titulo = input(
            "O tamanho do titulo excede o numero maximo de caracteres(50), digite novamente: "
        )
        add_titulo(titulo)


def add_autor(auth):
    auth = auth.strip()
    if len(auth) <= 50:
        return auth
    else:
        auth = input(
            "O nome do autor excede o numero maximo de caracteres(50), digite novamente: "
        )
        add_autor(auth)


def add_editora(editora):
    editora = editora.strip()
    if len(editora) <= 20:
        return editora
    else:
        editora = input(
            "O nome da editora excede o numero maximo de caracteres(20), digite novamente: "
        )
        add_editora(editora)


def add_ano(ano):
    ano = ano.strip()
    if ano.isnumeric() is True and len(ano) == 4:
        return ano
    else:
        ano = input("Dgitite o ano no formato correto e.g. 2001: ")


def add_cat(categoria):
    categoria = categoria.strip()
    if len(categoria) <= 20:
        return categoria
    else:
        categoria = input(
            "O nome da categoria excede o numero maximo de caracteres(20), digite novamente: "
        )
        add_cat(categoria)


def add_entrada():
    A = input("Digite o ISBN do livro: ")
    isbn = add_isbn(A)

    B = input("Digite o titulo do livro: ")
    titulo = add_titulo(B)

    C = input("Digite o autor: ")
    autor = add_autor(C)

    D = input("Digite a Editora: ")
    editora = add_editora(D)

    E = input("Digite o ano do livro: ")
    ano = add_ano(E)

    F = input("Digite a categoria do livro: ")
    categoria = add_cat(F)

    G = datetime.datetime.now()
    data = G.strftime("%d-%m-%Y")

    if all([A, B, C, D, E, F, G]) is True and int(isbn) > 0:

        sql_insert = """INSERT INTO livros VALUES(NULL, {}, \'{}\', \'{}\', {}, \'{}\', \'{}\', NULL, NULL, \'{}\');""".format(
            isbn, titulo, autor, ano, editora, categoria, data)

        print(sql_insert)

        cruder(sql_insert)
    else:
        print("\nPor favor, preencha todos os dados\n")
        add_entrada()


# FUNCAO DE CONSULTA


def con_nome(usuario):
    termo_pesquisa = input(
        "Digite o titulo, autor, categoria, editora, ano ou ENTER para exibir todos: "
    )
    sql_command = """SELECT * FROM livros WHERE titulo like '%{t}%' or categoria like '%{t}%' or titulo like '%{t}%' or autores like '%{t}%' or ano like '%{t}%' or editora like '%{t}%' ;""".format(
        t=termo_pesquisa)
    resultado = cruder(sql_command)
    if resultado is not None:
        if usuario == "cliente":
            tabela = resultado
            print(*tabela, sep="\n")
        elif usuario == "funcionario":
            tabela = resultado
            print(
                '_' * 79,
                'COD|ISBN|TITLO|AUTOR(ES)|ANO|EDITORA|CATEGORIA|EMP_USU|EM_DATA|DATA_ADICIONADO',
                '_' * 79,
                *tabela,
                sep="\n")
    else:
        print("Nenhum resultado encontrado.")


#   FUNCAO DE ALTERACAO


def liv_alterar():
    con_nome()
    livro = input("Digite o codigo do livro a ser alterado: ")
    coluna = int(
        input(
            "Digite qual coluna deseja alterar: \n [1]Titulo \n [2]Autores \n [3]Ano \n [4]Editora \n [5]Categoria \n [6]ISBN"
        ))
    if coluna == 1:
        alterada = "titulo"
        valor_novo = input("Digite o valor novo para")
        add_titulo()
    elif coluna == 2:
        alterada = "autores"
        valor_novo = input("Digite o valor novo para")
        add_autor()
    elif coluna == 3:
        alterada = "ano"
        valor_novo = input("Digite o valor novo para")
        add_ano()
    elif coluna == 4:
        alterada = "editora"
        valor_novo = input("Digite o valor novo para")
        add_editora()
    elif coluna == 5:
        alterada = "categoria"
        valor_novo = input("Digite o valor novo para")
        add_cat()
    elif coluna == 6:
        alterada = "isbn"
        valor_novo = input("Digite o valor novo para")
    else:
        print("Por favor digite uma opcao valida:")
        liv_alterar()

    sql_command = """UPDATE livros SET {}='{}' WHERE cod_liv={};""".format(
        alterada, valor_novo, livro)
    cruder(sql_command)


# FUNCAO DE REMOCAO


def liv_apagar():
    con_nome("cliente")
    livro = input("\n Digite o codigo do livro a ser removido: ")
    sql_command = """DELETE FROM livros WHERE cod_liv={};""".format(livro)
    cruder(sql_command)


# FUNCAO PARA EXIBIR O MENU


def liv_menu():
    opcao = input(
        " [1]adicionar livros \n [2]alterar livros \n [3]consultar livros \n [4]remover livros"
    )
    opcao = int(opcao)
    if opcao == 1:
        add_entrada()
    elif opcao == 2:
        liv_alterar()
    elif opcao == 3:
        con_nome("cliente")
    elif opcao == 4:
        liv_apagar()
    else:
        print("Por favor, digite uma alternativa valida...")
        liv_menu()
