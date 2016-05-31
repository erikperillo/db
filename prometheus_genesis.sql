SET datestyle TO postgres, dmy; 

create table cliente (
	cnpj bigint,
	razao_social varchar(64),
	primary key(cnpj)
);

create table fornecedor (
	cnpj bigint,
	razao_social varchar(64),
	primary key(cnpj)
);

create table transportadora (
	cnpj bigint,
	razao_social varchar(64),
	primary key(cnpj)
);

create table estoque (
	local varchar(256),
	capacidade integer,
	volume_atual integer,
	primary key(local),
	check(volume_atual < capacidade)
);

create table lote_insumo (
	lote_insumo integer,
	data_fab date,
	validade integer,
	primary key(lote_insumo)
);

create table insumo (
	id bigint,
	lote_insumo integer,
	preco integer,
	tipo_gado_origem varchar(64),
	cnpj bigint,
	data date,
	primary key(id),
	foreign key(lote_insumo) references lote_insumo(lote_insumo),
	foreign key(cnpj) references fornecedor(cnpj)
);

create table preco_leite_uht (
	preco_leite_uht integer,
	margem_de_lucro real,
	primary key(preco_leite_uht)
);

create table lote_leite_uht (
	lote_leite_uht integer,
	data_fab date,
	validade integer,
	qualidade varchar(32),
	primary key(lote_leite_uht)
);

create table leite_uht (
	id bigint ,
	lote_leite_uht integer,
	local varchar(256),
	preco_leite_uht integer,
	cnpj_cliente bigint,
	cnpj_transportadora bigint,
	data date,
	primary key(id),
	foreign key(lote_leite_uht) references lote_leite_uht(lote_leite_uht),
	foreign key(local) references estoque(local),
	foreign key(preco_leite_uht) references preco_leite_uht(preco_leite_uht),
	foreign key(cnpj_cliente) references cliente(cnpj),
	foreign key(cnpj_transportadora) references transportadora(cnpj)
);

create table preco_queijo (
	preco_queijo integer,
	margem_de_lucro real,
	primary key(preco_queijo)
);

create table lote_queijo (
	lote_queijo integer  ,
	data_fab date,
	validade integer,
	qualidade varchar(32),
	primary key(lote_queijo)
);

create table queijo (
	id bigint,
	lote_queijo integer,
	local varchar(256),
	preco_queijo integer,
	cnpj_cliente bigint,
	cnpj_transportadora bigint,
	data date,
	primary key(id),
	foreign key(lote_queijo) references lote_queijo(lote_queijo),
	foreign key(local) references estoque(local),
	foreign key(preco_queijo) references preco_queijo(preco_queijo),
	foreign key(cnpj_cliente) references cliente(cnpj),
	foreign key(cnpj_transportadora) references transportadora(cnpj)
);

create table lote_manteiga (
	lote_manteiga integer  ,
	data_fab date,
	validade integer,
	qualidade varchar(50),
	primary key(lote_manteiga)
);

create table preco_manteiga (
	preco_manteiga integer,
	margem_de_lucro real,
	primary key(preco_manteiga)
);

create table manteiga (
	id bigint ,
	lote_manteiga integer,
	local varchar(256),
	preco_manteiga integer,
	cnpj_cliente bigint,
	cnpj_transportadora bigint,
	data date,
	primary key(id),
	foreign key(lote_manteiga) references lote_manteiga(lote_manteiga),
	foreign key(local) references estoque(local),
	foreign key(preco_manteiga) references preco_manteiga(preco_manteiga),
	foreign key(cnpj_cliente) references cliente(cnpj),
	foreign key(cnpj_transportadora) references transportadora(cnpj)
);

create table pessoa (
	cpf bigint,
	nome varchar(256),
	telefone bigint,
	primary key(cpf)
);

/*is this really necessary? I don't think so.
create table gera_leite_uht (
	id_insumo integer,
	id_produto integer,
	id_leite_uht integer,
	primary key(id_insumo, id_produto),
	foreign key(id_insumo) references insumo(id),
	foreign key(id_leite_uht) references leite_uht(id)
);

create table gera_queijo (
	id_insumo integer,
	id_produto integer,
	id_queijo integer,
	primary key(id_insumo, id_produto),
	foreign key(id_insumo) references insumo(id),
	foreign key(id_queijo) references leite_uht_queijo(id)
);

create table gera_manteiga (
	id_insumo integer,
	id_produto integer,
	id_manteiga integer,
	primary key(id_insumo, id_produto),
	foreign key(id_insumo) references insumo(id),
	foreign key(id_manteiga) references manteiga(id)
);*/

create table e_responsavel_por_transportadora (
	cpf bigint,
	cnpj bigint,
	primary key(cpf, cnpj),
	foreign key(cpf) references pessoa(cpf),
	foreign key(cnpj) references transportadora(cnpj)
);

create table e_responsavel_por_fornecedor (
	cpf bigint,
	cnpj bigint,
	primary key(cpf, cnpj),
	foreign key(cpf) references pessoa(cpf),
	foreign key(cnpj) references fornecedor(cnpj)
);

create table e_responsavel_por_cliente (
	cpf bigint,
	cnpj bigint,
	primary key(cpf, cnpj),
	foreign key(cpf) references pessoa(cpf),
	foreign key(cnpj) references cliente(cnpj)
);

create table entrega_leite_uht (
	id bigint,
	cnpj bigint,
	data date,
	primary key(id),
	foreign key(id) references leite_uht(id),
	foreign key(cnpj) references transportadora(cnpj)
);

create table entrega_queijo (
	id bigint,
	cnpj bigint,
	data date,
	primary key(id),
	foreign key(id) references queijo(id),
	foreign key(cnpj) references transportadora(cnpj)
);

create table entrega_manteiga (
	id bigint,
	cnpj bigint,
	data date,
	primary key(id),
	foreign key(id) references manteiga(id),
	foreign key(cnpj) references transportadora(cnpj)
);
