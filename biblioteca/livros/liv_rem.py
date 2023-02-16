import biblioteca.sql_bib.bib_cruder as crud
import biblioteca.livros.liv_con as con


def liv_apagar():
    con.con_nome()
    livro = input("\n Digite o codigo do livro a ser removido: ")
    sql_command = """DELETE FROM livros WHERE cod_liv={};""".format(livro)
    crud.cruder(sql_command)
