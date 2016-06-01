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
    "leite_uht": ("id", "lote_leite_uht", "local", "preco_leite_uht", "data"),
        #("id", "lote_leite_uht", "local", "preco_leite_uht", 
        #    "cnpj_cliente", "cnpj_transportadora", "data"),
    "lote_leite_uht": ("lote_leite_uht", "data_fab", "validade", "qualidade"), 
    "preco_leite_uht": ("preco_leite_uht", "margem_de_lucro"),
    "queijo": ("id", "lote_queijo", "local", "preco_queijo", "data"),
        #("id", "lote_queijo", "local", "preco_queijo", 
              #"cnpj_cliente", "cnpj_transportadora", "data"),
    "lote_queijo": ("lote_queijo", "data_fab", "validade", "qualidade"), 
    "preco_queijo": ("preco_queijo", "margem_de_lucro"),
    "manteiga": ("id", "lote_manteiga", "local", "preco_manteiga", "data"),
        #("id", "lote_manteiga", "local", "preco_manteiga",
        #    "cnpj_cliente", "cnpj_transportadora", "data"),
    "lote_manteiga": ("lote_manteiga", "data_fab", "validade", "qualidade"), 
    "preco_manteiga": ("preco_manteiga", "margem_de_lucro"),
    "pessoa": ("cpf", "nome", "telefone"),
    "estoque": ("local", "capacidade", "volume_atual"),
    "e_responsavel_por_transportadora": ("cpf", "cnpj"),
    "e_responsavel_por_fornecedor": ("cpf", "cnpj"),
    "e_responsavel_por_cliente": ("cpf", "cnpj"),
    "entrega_leite_uht": ("id", "cnpj", "data"),
    "entrega_queijo": ("id", "cnpj", "data"),
    "entrega_manteiga": ("id", "cnpj", "data"),
    "compra_leite_uht": ("id", "cnpj", "data"),
    "compra_queijo": ("id", "cnpj", "data"),
    "compra_manteiga": ("id", "cnpj", "data")
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
    "entrega_manteiga",
    "compra_leite_uht",
    "compra_queijo",
    "compra_manteiga"
]

TABLES_NUM = {
    "cliente": 234,
    "fornecedor": 158,
    "transportadora": 111,
    "estoque": 108,
    "lote_insumo": 243,
    "insumo": 9001,
    "preco_leite_uht": 92,
    "lote_leite_uht": 122,
    "leite_uht": 3321,
    "preco_queijo": 39,
    "lote_queijo": 183,
    "queijo": 2343,
    "lote_manteiga": 108,
    "preco_manteiga": 47,
    "manteiga": 3337,
    "pessoa": 643,
    "e_responsavel_por_transportadora": 132,
    "e_responsavel_por_fornecedor": 201,
    "e_responsavel_por_cliente": 310,
    "entrega_leite_uht": 2131,
    "entrega_queijo": 1322,
    "entrega_manteiga": 1123,
    "compra_leite_uht": 989,
    "compra_queijo": 560,
    "compra_manteiga": 729 
}

#foreign keys specification
#(param_posit, relation_name, relation_param_posit, prob_null)
DEPS = {
    "insumo": [
        ("lote_insumo", "lote_insumo", "lote_insumo", 0.0),
        ("cnpj", "fornecedor", "cnpj", 0.0)
    ],
    "leite_uht": [
        ("lote_leite_uht", "lote_leite_uht", "lote_leite_uht", 0.0),
        ("local", "estoque", "local", 0.0),
        ("preco_leite_uht", "preco_leite_uht", "preco_leite_uht", 0.0),
        #("cnpj_cliente", "cliente", "cnpj", 0.33),
        #("cnpj_transportadora", "transportadora", "cnpj", 0.0)
    ],
    "queijo": [
        ("lote_queijo", "lote_queijo", "lote_queijo", 0.0),
        ("local", "estoque", "local", 0.0),
        ("preco_queijo", "preco_queijo", "preco_queijo", 0.0),
        #("cnpj_cliente", "cliente", "cnpj", 0.33),
        #("cnpj_transportadora", "transportadora", "cnpj", 0.33)
    ],
    "manteiga": [
        ("lote_manteiga", "lote_manteiga", "lote_manteiga", 0.0),
        ("local", "estoque", "local", 0.0),
        ("preco_manteiga", "preco_manteiga", "preco_manteiga", 0.0),
        #("cnpj_cliente", "cliente", "cnpj", 0.33),
        #("cnpj_transportadora", "transportadora", "cnpj", 0.33)
    ],
    "e_responsavel_por_transportadora": [
        ("cpf", "pessoa", "cpf", 0.0),
        ("cnpj", "transportadora", "cnpj", 0.0)
    ],
    "e_responsavel_por_fornecedor": [
        ("cpf", "pessoa", "cpf", 0.0),
        ("cnpj", "fornecedor", "cnpj", 0.0)
    ],
    "e_responsavel_por_cliente": [
        ("cpf", "pessoa", "cpf", 0.0),
        ("cnpj", "cliente", "cnpj", 0.0)
    ],
    "entrega_leite_uht": [
        ("id", "leite_uht", "id", 0.0),
        ("cnpj", "transportadora", "cnpj", 0.0)
    ],
    "entrega_queijo": [
        ("id", "queijo", "id", 0.0),
        ("cnpj", "transportadora", "cnpj", 0.0)
    ],
    "entrega_manteiga": [
        ("id", "manteiga", "id", 0.0),
        ("cnpj", "transportadora", "cnpj", 0.0)
    ],
    "compra_leite_uht": [
        ("id", "leite_uht", "id", 0.0),
        ("cnpj", "cliente", "cnpj", 0.0)
    ],
    "compra_queijo": [
        ("id", "queijo", "id", 0.0),
        ("cnpj", "cliente", "cnpj", 0.0)
    ],
    "compra_manteiga": [
        ("id", "manteiga", "id", 0.0),
        ("cnpj", "cliente", "cnpj", 0.0)
    ]
}

"""
gets list of lines from text file
"""
def list_from_file(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]

"""
gets a value from list of values
"""
def get_val(lists, tp, index):
    values = lists[PARAMS_TYPES[tp]]
    return "'%s'" % values[index % len(values)]

"""
gets a random value from list of values
"""
def get_rand_val(values, prob_null=0.0):
    if rand.uniform(0.0, 1.0) < prob_null:
        return "null" 
    else:
        return "%s" % values[rand.randint(0, len(values)-1)]
        
"""
generates sql command
"""
def sql_cmd(table_name, table_values):
    return "INSERT INTO %s VALUES (%s)" % \
        (table_name, ",".join("%s" % n for n in table_values))

"""
generates tables values
"""
def gen(output):
    #connecting to database
    #print "connecting to database '%s' ... " % db_name,
    #conn = ppg.connect(database=db_name)
    #print "done"

    #cur = conn.cursor()

    output.write("SET datestyle = 'ISO, DMY';\n")
    #getting random values from files
    #assumes each type file is named 'type.txt'
    lists = dict((tp, list_from_file(RAND_DIR + "/" + tp + ".txt")) \
        for tp in TYPES)

    tables = {}

    for name in TABLES_ORDER:
        print "in relation '%s' ..." % name,
        types = TABLES[name]
        vals = {}        
        num = TABLES_NUM[name]

        if name in DEPS:
            #num = max([len(tables[n][t]) for __, n, t in DEPS[name]])
            for dep in DEPS[name]:
                tp, dep_name, dep_tp, prob_null = dep
                vals[tp] = tables[dep_name][dep_tp]
                v_num = len(vals[tp])
                if num > v_num:
                    vals[tp] += [get_rand_val(vals[tp], prob_null) \
                        for i in range(num - v_num)]
                else:
                    vals[tp] = vals[tp][:num]
                        #[vals[tp][rand.randint(0, len(vals[tp])-1)] \
                        #    for i in range(num - v_num)]
                        #[get_val(lists, tp, i) for i in range(num - v_num)]

        for tp in types:
            if not tp in vals:
                vals[tp] = [get_val(lists, tp, i) for i in range(num)]
         
        #for k, v in vals.iteritems():
        #    print "k=", k, "len(v)=", len(v)

        for i in range(num):
            tup_vals = [vals[tp][i] for tp in types]
            #print tup_vals
            cmd = sql_cmd(name, tup_vals)
            output.write(cmd + ";\n")
            #cur.execute(cmd)

        tables[name] = vals

        print "done"

    #conn.commit()
    #print "records created"
    #cur.close()
    #conn.close()

#usage: gen <out_filename>
def main():
    if len(sys.argv) < 2:
        print "usage: gen <out_filename>"
        exit()
    else:
        output = open(sys.argv[1], "w")

    gen(output)

    print "end of generation"

if __name__ == "__main__":
    main()
