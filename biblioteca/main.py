import onca.livros.funcoes as livro
import onca.usuarios.funcoes as usu
if __name__ == "__main__":

    def menu():
        opcao = input(" [1]Login\n [2]Consultar catalogo\n [3]Registro\n")
        if int(opcao) == 1:
            usu.usu_menu()
        elif int(opcao) == 2:
            livro.con_nome("cliente")
        if int(opcao) == 3:
            usu.add_cadastro()
        else:
            print("Por favor, digite uma opcao valida.\n")
            menu()


menu()
