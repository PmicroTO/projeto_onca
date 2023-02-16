import datetime
import biblioteca.sql_bib.bib_cruder as crud


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

        crud.cruder(sql_insert)
    else:
        print("\nPor favor, preencha todos os dados\n")
        add_entrada()
