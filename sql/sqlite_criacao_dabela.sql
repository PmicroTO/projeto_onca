DROP TABLE IF EXISTS livros;
DROP TABLE IF EXISTS usuarios;

-- Habilitar chaves estrangeiras para correlacionar livros com o cliente
PRAGMA foreign_keys = ON;

-- Criacao da tabela para o modulo livros
CREATE TABLE livros (
	cod_liv INTEGER PRIMARY KEY AUTOINCREMENT,
	isbn INTEGER(13) NOT NULL,
	titulo TEXT(50) NOT NULL,
	autores TEXT(255) NOT NULL,
	ano INTEGER(4) NOT NULL,
	editora TEXT(50) NOT NULL,
	categoria TEXT(50) NOT NULL,
	disponivel NUMERIC(1) NOT NULL,
	data_add TEXT(10) NOT NULL
);

-- Criacao da tabela para o modulo usuarios
CREATE TABLE usuarios (
	cod_usu INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT(8) NOT NULL,
	senha TEXT(24) NOT NULL,
	email TEXT(55) NOT NULL,
	nome TEXT(55) NOT NULL,
	cpf INTEGER NOT NULL,
	telefone INTEGER NOT NULL,
	cep INTEGER NOT NULL,
	bairro TEXT(255) NOT NULL,
	rua TEXT(255) NOT NULL,
	casa TEXT(10) NOT NULL,
	livro_1 INTEGER,
	livro_1_data TEXT(10),
	livro_2 INTEGER,
	livro_2_data TEXT(10),
	livro_3 INTEGER,
	livro_3_data TEXT(10),
	FOREIGN KEY (livro_1) REFERENCES livros(cod_liv),
	FOREIGN KEY (livro_2) REFERENCES livros(cod_liv),
	FOREIGN KEY (livro_3) REFERENCES livros(cod_liv)
);



