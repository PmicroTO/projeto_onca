import re
from ..sql.bib_cruder import cruder

# funcoes de cadastro


def add_user(x):
    x = str(x)
    x = x.lower()
    x = x.strip()
    if len(x) <= 8:
        sql_command = """SELECT * FROM usuarios WHERE username='{}';""".format(
            x)
        resultado = cruder(sql_command)
        if bool(resultado) is False:
            return x
        else:
            print(resultado)
            x = input(" Usuario ja cadastrado, por favor, escolha outro nome: ")
            add_user(x)
    else:
        x = input(
            " O nome de usuario pode ter no maximo 8 letras, digite novamente: "
        )
        add_user(x)


def add_senha(x):
    x = str(x)
    x = x.strip()
    if len(x) <= 24:
        return x
    else:
        x = input(" Tamanho maximo da senha 24 caracteres.\n Digite novamente: "
                 ).strip()
        add_senha(x)


def add_email(x):
    x = str(x)
    x = x.strip()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if len(x) <= 55 and re.search(regex, x) is not None:
        sql_command = """SELECT * FROM usuarios WHERE email='{}';""".format(x)
        resultado = cruder(sql_command)
        if bool(resultado) is False:
            return x
        else:
            x = input(" Email ja cadastrado.\n Digite novamente: ").strip()
            add_email(x)
    else:
        x = input("E-mail em formato invalido.\n Digite novamente: ").strip()
        add_email(x)


def add_nome(x):
    x = str(x)
    x = x.strip()
    if len(x) <= 55:
        return x
    else:
        print("Seu nome excedeu o limite de caracteres(50).")
        x = input("Digite seu Nome: ").strip()
        add_nome(x)


def add_cpf(x):
    x = str(x)
    x = x.replace(".", "")
    x = x.replace("-", "")
    x = x.strip()
    if x.isnumeric() is True and len(x) == 11:
        return x
    else:
        print("Por favor, insira um cpf valido, apenas digitos.")
        x = input("CPF").strip()
        add_cpf(x)


def add_telefone(x):
    x = str(x)
    x = x.replace("(", "")
    x = x.replace(")", "")
    x = x.replace("-", "")
    x = x.strip()
    if x.isnumeric() is True and len(x) == 11:
        return x
    else:
        x = input("Por favor, insira um numero de celular valido(11 digitos).")
        add_telefone(x)


def add_cep(x):
    x = str(x)
    x = x.replace(".", "")
    x = x.replace("-", "")
    x = x.strip()
    if x.isnumeric() is True and len(x) == 8:
        return x
    else:
        x = input(" Por favor, insira um cep  valido:  ")
        add_cep(x)


def add_bairro(x):
    if len(str(x)) <= 255:
        return x
    else:
        x = input("Por favor abrevie o nome de seu Bairro: ")
        add_bairro(x)


def add_rua(x):
    if len(str(x)) <= 255:
        return x
    else:
        x = input(" Por favor, abrevie o nome de sua Rua: ")
        add_rua(x)


def add_casa(x):
    if len(str(x)) <= 10:
        return x
    else:
        x = input("Por favor, digite um valor valido, maximo 10 caracteres: ")
        add_casa(x)


def add_genero(x):
    x = str(x).lower()
    if x == "m" or x == "f" or x == "o":
        return x
    else:
        print("Por favor digite um valor valido.")
        x = input(" Por favor digite um valor valido. Genero\n [M]\n [F]\n [O]")
        add_genero(x)


def add_cadastro():
    a = add_user(input("Digite o nome do seu novo usuario:\n"))
    b = add_senha(input("Digite sua nova senha:\n"))
    c = add_email(input("Digite o seu email:\n"))
    d = add_nome(input("Digite seu Nome:\n"))
    e = add_cpf(input("CPF, apenas digitos:\n"))
    f = add_telefone(input("Celular, apenas numeros, com ddd:\n"))
    g = add_cep(input("CEP:\n"))
    h = add_bairro(input("Bairro:\n"))
    i = add_rua(input("Rua:\n"))
    j = add_casa(input("Casa:\n"))
    k = add_genero(input(" Genero:\n\n [M]\n [F]\n [O]\n"))

    sql_insert = """INSERT INTO usuarios VALUES(NULL, '{}', '{}', '{}', '{}', {}, {}, {}, '{}', '{}', '{}', '{}', NULL);""".format(
        a, b, c, d, e, f, g, h, i, j, k)
    print(sql_insert + "Usuario cadastrado com sucesso, Bem vindo")
    cruder(sql_insert)


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


def usu_alterar():
    con_nome()
    livro = input("Digite o codigo do livro a ser alterado: ")
    coluna = int(
        input(
            "Digite qual coluna deseja alterar: \n [1]Email \n [2]Senha \n [3]Telefone"
        ))
    if coluna == 1:
        alterada = "senha"
        valor_novo = input("Digite o valor novo.")
        add_senha()
    elif coluna == 2:
        alterada = "email"
        valor_novo = input("Digite o valor novo.")
        add_email()
    elif coluna == 3:
        alterada = "telefone"
        valor_novo = input("Digite o valor novo.")
        add_telefone()
    else:
        print("Por favor digite uma opcao valida:")
        usu_alterar()

    sql_command = """UPDATE usuarios SET {}='{}' WHERE cod_liv={};""".format(
        alterada, valor_novo, livro)
    cruder(sql_command)


# FUNCAO DE REMOCAO


def liv_apagar():
    con_nome("cliente")
    livro = input("\n Digite o codigo do livro a ser removido: ")
    sql_command = """DELETE FROM livros WHERE cod_liv={};""".format(livro)
    cruder(sql_command)


# FUNCAO PARA EXIBIR O MENU


def usu_menu():
    usuario = input("Digite seu username: ")
    senha = input("Digite sua senha: ")

    sql_command = """SELECT * FROM usuarios WHERE username='%{}%' and senha='%{}%';""".format(
        usuario, senha)
    resultado = cruder(sql_command)
    if resultado is not None:
        print(resultado)
    else:
        print("Usuario ou senha invalidos.")
