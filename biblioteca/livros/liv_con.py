import biblioteca.sql_bib.bib_cruder as crud


def con_nome(funcionario_ou_cliente):
    usuario = funcionario_ou_cliente
    termo_pesquisa = input(
        "Digite o nome do livro desejado ou ENTER para exibir todos: ")
    string = termo_pesquisa
    sql_command = """SELECT * FROM livros WHERE titulo like '%{}%';""".format(
        string)
    resultado = crud.cruder(sql_command)
    if resultado is not None:
        if usuario == "cliente":
            tabela = [(x[2], x[3], x[4], x[5]) for x in resultado]
        elif usuario == "funcionario":
            tabela = resultado

        print(*tabela, sep="\n")
    else:
        print("Nenhum resultado encontrado.")
