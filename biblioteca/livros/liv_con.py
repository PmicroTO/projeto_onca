import biblioteca.sql_bib.bib_cruder as crud


def con_nome():
    termo_pesquisa = input(
        "Digite o nome do livro desejado ou ENTER para exibir todos: ")
    string = termo_pesquisa
    sql_command = """SELECT * FROM livros WHERE titulo like '%{}%';""".format(
        string)
    resultado = crud.cruder(sql_command)
    tuplas = print(*resultado, sep="\n")
    print(tuplas)
