import biblioteca.sql_bib.bib_cruder as crud


def con_nome(termo_pesquisa):
    string = termo_pesquisa
    sql_command = """SELECT * FROM livros WHERE titulo like '%{}%';""".format(
        string)
    resultado = crud.cruder(sql_command)
    resultado_trimmed = resultado
    print(*resultado_trimmed, sep="\n")


termo_pesquisa = input("Digite o nome do livro desejado: ")
con_nome(termo_pesquisa)
