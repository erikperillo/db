#!/usr/bin/env python2.7

#import psycopg2 as ppg
import random as rand
import sys

RAND_DIR = "./rand"

TYPES = [
    "cnpj",
    "empresa",
    "lote",
    "nome",
    "preco",
    "gado",
    "data",
    "dias",
    "qualidade",
    "real",
    "endereco",
    "id",
    "gado",
    "qualidade",
    "cpf",
    "telefone",
    "inteiro",
    "inteiro_menor"
]

PARAMS_TYPES = {
    "cnpj": "cnpj",
    "razao_social": "empresa",
    "local": "endereco",     
    "capacidade": "inteiro",
    "volume_atual": "inteiro_menor",
    "lote_insumo": "lote",
    "data_fab": "data",
    "preco_leite_uht": "preco",
    "margem_de_lucro": "real",
    "lote_leite_uht": "lote",
    "validade": "dias",
    "qualidade": "qualidade",
    "cnpj_cliente": "cnpj",
    "cnpj_transportadora": "cnpj",
    "data": "data",
    "preco_queijo": "preco",
    "lote_queijo": "lote",
    "preco_manteiga": "preco",
    "lote_manteiga": "lote",
    "cpf": "cpf",
    "id": "id",
    "nome": "nome",
    "telefone": "telefone",
    "preco": "preco",
    "tipo_gado_origem": "gado"
}

TABLES = {
    "cliente": ("cnpj", "razao_social"),
    "fornecedor": ("cnpj", "razao_social"),
    "transportadora": ("cnpj", "razao_social"),
    "insumo":\
        ("id", "lote_insumo", "preco", "tipo_gado_origem", "cnpj", "data"),
    "lote_insumo": ("lote_insumo", "data_fab", "validade"), 
    "leite_uht":\
        ("id", "lote_leite_uht", "local", "preco_leite_uht", 
            "cnpj_cliente", "cnpj_transportadora", "data"),
    "lote_leite_uht": ("lote_leite_uht", "data_fab", "validade", "qualidade"), 
    "preco_leite_uht": ("preco_leite_uht", "margem_de_lucro"),
    "queijo": ("id", "lote_queijo", "local", "preco_queijo", 
                  "cnpj_cliente", "cnpj_transportadora", "data"),
    "lote_queijo": ("lote_queijo", "data_fab", "validade", "qualidade"), 
    "preco_queijo": ("preco_queijo", "margem_de_lucro"),
    "manteiga": ("id", "lote_manteiga", "local", "preco_manteiga",
                    "cnpj_cliente", "cnpj_transportadora", "data"),
    "lote_manteiga": ("lote_manteiga", "data_fab", "validade", "qualidade"), 
    "preco_manteiga": ("preco_manteiga", "margem_de_lucro"),
    "pessoa": ("cpf", "nome", "telefone"),
    "estoque": ("local", "capacidade", "volume_atual"),
    "e_responsavel_por_transportadora": ("cpf", "cnpj"),
    "e_responsavel_por_fornecedor": ("cpf", "cnpj"),
    "e_responsavel_por_cliente": ("cpf", "cnpj"),
    "entrega_leite_uht": ("id", "cnpj", "data"),
    "entrega_queijo": ("id", "cnpj", "data"),
    "entrega_manteiga": ("id", "cnpj", "data")
}

TABLES_ORDER = [
    "cliente",
    "fornecedor",
    "transportadora",
    "estoque",
    "lote_insumo",
    "insumo",
    "preco_leite_uht",
    "lote_leite_uht",
    "leite_uht",
    "preco_queijo",
    "lote_queijo",
    "queijo",
    "lote_manteiga",
    "preco_manteiga",
    "manteiga",
    "pessoa",
    "e_responsavel_por_transportadora",
    "e_responsavel_por_fornecedor",
    "e_responsavel_por_cliente",
    "entrega_leite_uht",
    "entrega_queijo",
    "entrega_manteiga"
]

#foreign keys specification
#(param_posit, relation_name, relation_param_posit)
DEPS = {
    "insumo": [
        ("lote_insumo", "lote_insumo", "lote_insumo"),
        ("cnpj", "fornecedor", "cnpj")
    ],
    "leite_uht": [
        ("lote_leite_uht", "lote_leite_uht", "lote_leite_uht"),
        ("local", "estoque", "local"),
        ("preco_leite_uht", "preco_leite_uht", "preco_leite_uht"),
        ("cnpj_cliente", "cliente", "cnpj"),
        ("cnpj_transportadora", "transportadora", "cnpj")
    ],
    "queijo": [
        ("lote_queijo", "lote_queijo", "lote_queijo"),
        ("local", "estoque", "local"),
        ("preco_queijo", "preco_queijo", "preco_queijo"),
        ("cnpj_cliente", "cliente", "cnpj"),
        ("cnpj_transportadora", "transportadora", "cnpj")
    ],
    "manteiga": [
        ("lote_manteiga", "lote_manteiga", "lote_manteiga"),
        ("local", "estoque", "local"),
        ("preco_manteiga", "preco_manteiga", "preco_manteiga"),
        ("cnpj_cliente", "cliente", "cnpj"),
        ("cnpj_transportadora", "transportadora", "cnpj")
    ],
    "e_responsavel_por_transportadora": [
        ("cpf", "pessoa", "cpf"),
        ("cnpj", "transportadora", "cnpj")
    ],
    "e_responsavel_por_fornecedor": [
        ("cpf", "pessoa", "cpf"),
        ("cnpj", "fornecedor", "cnpj")
    ],
    "e_responsavel_por_cliente": [
        ("cpf", "pessoa", "cpf"),
        ("cnpj", "cliente", "cnpj")
    ],
    "entrega_leite_uht": [
        ("id", "leite_uht", "id"),
        ("cnpj", "transportadora", "cnpj")
    ],
    "entrega_queijo": [
        ("id", "queijo", "id"),
        ("cnpj", "transportadora", "cnpj")
    ],
    "entrega_manteiga": [
        ("id", "manteiga", "id"),
        ("cnpj", "transportadora", "cnpj")
    ]
}

"""
gets list of lines from text file
"""
def list_from_file(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]

"""
gets a random value from a list
"""
def rand_val(lst):
    return lst[rand.randint(0, len(lst)-1)] 

"""
generates sql command
"""
def sql_cmd(table_name, table_values):
    return "INSERT INTO %s VALUES (%s)" % \
        (table_name, ",".join("'%s'" % n for n in table_values))

"""
generates tables values
"""
def gen(num, output):
    #connecting to database
    #print "connecting to database '%s' ... " % db_name,
    #conn = ppg.connect(database=db_name)
    #print "done"

    #cur = conn.cursor()

    #getting random values from files
    #assumes each type file is named 'type.txt'
    lists = dict((tp, list_from_file(RAND_DIR + "/" + tp + ".txt")) \
        for tp in TYPES)

    get_val = lambda tp: rand_val(lists[PARAMS_TYPES[tp]])

    tables = {}

    for name in TABLES_ORDER:
        types = TABLES[name]
        vals = {}        
        if name in DEPS:
            for dep in DEPS[name]:
                tp, dep_name, dep_tp = dep
                vals[tp] = tables[dep_name][dep_tp]
        for tp in types:
            if not tp in vals:
                vals[tp] = [get_val(tp) for __ in range(num)]

        for i in range(num):
            tup_vals = [vals[tp][i] for tp in types]
            cmd = sql_cmd(name, tup_vals)
            output.write(cmd + ";\n")
            #cur.execute(cmd)

        tables[name] = vals

    #conn.commit()
    #print "records created"
    #cur.close()
    #conn.close()

#usage: gen <num_tuples> [out_filename]
def main():
    if len(sys.argv) < 2:
        num = 10
    else:
        num = int(sys.argv[1])

    if len(sys.argv) > 2:
        output = open(sys.argv[2], "w")
    else:
        output = sys.stdout

    gen(num, output)

if __name__ == "__main__":
    main()
