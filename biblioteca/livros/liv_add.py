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


def newauth():
    C2 = input(
        "Digite 'S' para Adicionar um novo autor, 'C' pra continuar.").lower()
    auth = ""
    while C2 == "s" and C2 != "c":
        C = input("Digite o proximo autor(C para continuar): ")
        if C.lower() == "c":
            break
        auth += "; " + add_autor(C.strip())
        print(auth)
    return auth


def add_entrada():
    A = input("Digite o ISBN do livro: ")
    isbn = add_isbn(A)

    B = input("Digite o titulo do livro: ")
    titulo = add_titulo(B)

    C = input("Digite o autor: ")
    autor = add_autor(C.strip())
    #    auth_ph_s = newauth()
    #    autores = "\"" + auth_p + auth_s + "\""

    D = input("Digite a Editora: ")
    editora = add_editora(D)

    E = input("Digite o ano do livro: ")
    ano = add_ano(E)

    F = input("Digite a categoria do livro")
    categoria = F

    G = datetime.datetime.now()
    data = G.strftime("%d-%m-%Y")

    sql_insert = """INSERT INTO livros VALUES(NULL, {}, \'{}\', \'{}\', {}, \'{}\', \'{}\', NULL, NULL, \'{}\');""".format(
        isbn, titulo, autor, ano, editora, categoria, data)

    print(sql_insert)

    crud.cruder(sql_insert)


add_entrada()
