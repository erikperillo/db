create table cliente (
    cnpj integer,
    razao_social varchar(64),
	primary key(cnpj)
);

create table fornecedor (
    cnpj integer,
    razao_social varchar(64),
	primary key(cnpj)
);

create table transportadora (
    cnpj integer,
    razao_social varchar(64),
	primary key(cnpj)
);

create table insumo (
	id integer,
	lote_insumo integer,
	preco integer,
	tipo_gado_origem varchar(64),
	cnpj integer,
	data date,
	primary key(id),
	foreign key(lote_insumo) references lote_insumo(lote_insumo),
	foreign key(cnpj) references fornecedor(cnpj)
);

create table lote_insumo (
	lote_insumo integer  ,
	data_fab date,
	validade date,
	primary key(lote_insumo)
);

create table leite_uht (
	id integer ,
	lote_leite integer,
	local varchar(64),
	preco_leite integer,
	cnpj integer,
	data date,
	primary key(id),
	foreign key(lote_leite) references lote_leite(lote_leite),
	foreign key(local) references estoque(local),
	foreign key(preco_leite) references preco_leite(preco_leite),
	foreign key(cnpj) references empresa(cnpj)
);

create table lote_leite (
	lote_leite integer,
	data_fab date,
	validade date,
	qualidade varchar(32),
	primary key(lote_leite)
);

create table preco_leite (
	preco_leite integer,
	margem_de_lucro real,
	primary key(preco_leite)
);

create table queijo (
	id integer,
	lote_queijo integer,
	local varchar(50),
	preco_queijo integer,
	cnpj integer,
	data date,
	primary key(id),
	foreign key(lote_queijo) references lote_queijo(lote_queijo),
	foreign key(local) references estoque(local),
	foreign key(preco_queijo) references preco_queijo(preco_queijo),
	foreign key(cnpj) references empresa(cnpj)
);

create table lote_queijo (
	lote_queijo integer  ,
	data_fab date,
	validade date,
	qualidade varchar(32),
	primary key(lote_queijo)
);

create table preco_queijo (
	preco_queijo integer,
	margem_de_lucro real,
	primary key(preco_queijo)
);

create table manteiga (
	id integer ,
	lote_manteiga integer,
	local varchar(64),
	preco_manteiga integer,
	cnpj integer,
	data date,
	primary key(id),
	foreign key(lote_manteiga) references lote_manteiga(lote_manteiga),
	foreign key(local) references estoque(local),
	foreign key(preco_manteiga) references preco_manteiga(preco_manteiga),
	foreign key(cnpj) references empresa(cnpj)
);

create table lote_manteiga (
	lote_manteiga integer  ,
	data_fab date,
	validade date,
	qualidade varchar(50),
	primary key(lote_manteiga)
);

create table preco_manteiga (
	preco_manteiga integer,
	margem_de_lucro real,
	primary key(preco_manteiga)
);

create table pessoa (
	cpf integer,
	nome varchar(256),
	telefone integer,
	primary key(cpf)
);

create table estoque (
	local varchar(64),
	capacidade integer,
	volume_atual integer,
	primary key(local),
	check(volume_atual < capacidade)
);

/*is this really necessary? I don't think so.
create table gera_leite (
	id_insumo integer,
	id_produto integer,
	id_leite integer,
	primary key(id_insumo, id_produto),
	foreign key(id_insumo) references insumo(id),
	foreign key(id_leite) references leite_uht(id)
);

create table gera_queijo (
	id_insumo integer,
	id_produto integer,
	id_queijo integer,
	primary key(id_insumo, id_produto),
	foreign key(id_insumo) references insumo(id),
	foreign key(id_queijo) references leite_queijo(id)
);

create table gera_manteiga (
	id_insumo integer,
	id_produto integer,
	id_manteiga integer,
	primary key(id_insumo, id_produto),
	foreign key(id_insumo) references insumo(id),
	foreign key(id_manteiga) references manteiga(id)
);*/

create table e_responsavel_por (
	cpf integer,
	cnpj integer,
	primary key(cpf, cnpj),
	foreign key(cpf) references pessoa(cpf),
	foreign key(cnpj) references empresa(cnpj)
);

create table entrega_leite (
	id integer,
	cnpj integer,
	data date,
	primary key(id),
	foreign key(id) references leite_uht(id),
	foreign key(cnpj) references transportadora(cnpj)
);

create table entrega_queijo (
	id integer,
	cnpj integer,
	data date,
	primary key(id),
	foreign key(id) references queijo(id),
	foreign key(cnpj) references transportadora(cnpj)
);

create table entrega_manteiga (
	id integer,
	cnpj integer,
	data date,
	primary key(id),
	foreign key(id) references manteiga(id),
	foreign key(cnpj) references transportadora(cnpj)
);
