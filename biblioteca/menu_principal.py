import livros.livro as livro
if __name__ == "__main__":

    def menu():
        opcao = input(" [1]Login\n[2]Consultar catalogo\n")
        if int(opcao) == 1:
            livro.liv_menui()
        elif int(opcao) == 2:
            livro.co.con_nome("cliente")
        else:
            print("Por favor, digite uma opcao valida.\n")
            menu()
