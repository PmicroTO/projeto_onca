def add_isbn(isbn):
	isbn = isbn.strip()
	isbn = isbn.replace("-", "")
	if isbn.isnumeric() == True and len(isbn) == 13:
		return isbn
	else:
		isbn = input("Digite o ISBN no formato correto, e.g. '978-3-16-148410-0': ")
		add_isbn(isbn)


def add_titulo(titulo):
	titulo = titulo.strip()
	if len(titulo) <= 255:
		return titulo
	else:
		titulo = input("O tamanho do titulo excede o numero maximo de caracteres(50), digite novamente: ")
		add_titulo(titulo)


def add_autor(auth):
	auth = auth.strip()
	if len(auth) <= 50:
		return auth
	else:
		auth = input("O nome do autor excede o numero maximo de caracteres(50), digite novamente: ")
		add_autor(auth)


def add_editora(editora):
	editora = editora.strip()
	if len(editora) <= 20:
		return editora
	else:
		editora = input("O nome da editora excede o numero maximo de caracteres(20), digite novamente: ")
		add_editora(editora)


def add_ano(ano):
	ano = ano.strip()
	if ano.isnumeric() == True and len(ano) == 4:
		return ano
	else:
		ano = input("Dgitite o ano no formato correto e.g. 2001: ")


def add_entrada():
	A = input("Digite o ISBN do livro: ")
	isbn = add_isbn(A)

	B = input("Digite o titulo do livro: ")
	titulo = add_titulo(B)

	C = input("Digite o(s) autor(res): ")
	auth = add_autor(C)

	D = input("Digite a Editora: ")
	editora = add_editora(D)

	E = input("Digite o ano do livro: ")
	ano = add_ano(E)

	entrada_livro = ",".join([isbn,titulo, auth, editora, ano])

	print(entrada_livro)


add_entrada()