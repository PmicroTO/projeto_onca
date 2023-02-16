-- excluir tabela livros caso ela exista.
drop table if exists livros;
-- excluir tabela usuarios caso ela exista.
drop table if exists usuarios;
-- habilitar chaves estrangeiras para correlacionar livros com o cliente
pragma foreign_keys = on;
-- criacao da tabela para o modulo usuarios
create table usuarios (
	cod_usu integer primary key autoincrement,
	username text(8) not null,
	senha text(24) not null,
	email text(55) not null,
	nome text(55) not null,
	cpf integer(11) not null,
	telefone integer(11) not null,
	cep integer(8) not null,
	bairro text(255) not null,
	rua text(255) not null,
	casa text(10) not null,
	genero text(1),
	funcionario integer(1)
);

-- criacao da tabela para o modulo livros
create table livros (
	cod_liv integer primary key autoincrement,
	isbn integer(13) not null,
	titulo text(50) not null,
	autores text(255) not null,
	ano integer(4) not null,
	editora text(50) not null,
	categoria text(50) not null,
	emprestimo_usuario integer(1),
	emprestimo_data text(10),
	data_add text(10) not null,
	foreign key (emprestimo_usuario) references usuarios(cod_usu)
);

