from datetime import datetime
from dateutil.relativedelta import relativedelta
import model as sql


def insert_db(*args):
    sql.conectar_db_producao()

    colunas = """INSERT INTO financeiro_flancamento(classe, grupo, natureza, dt_movimento, dt_vencimento, centro_de_custo, movimentacao, conta, cartao, status_movimento, forma_pagamento, qtde_parcela, parcela, valor, valor_parcela, descricao) VALUES("""

    valores = f"'{args[0]}', '{args[1]}', '{args[2]}', '{args[3]}', '{args[4]}', '{args[5]}', '{args[6]}', '{args[7]}', '{args[8]}', '{args[9]}', '{args[10]}', {args[11]}, {args[12]}, {args[13]}, {args[14]}, '{args[15]}');"

    query_insert = colunas + valores
    sql.cursor_sqlite.execute(query_insert)
    sql.conexao_sqlite.commit()

    sql.desconectar_db_producao()


def etl_tratamento(*args):
    qtde_parcela = int(args[11])
    valor_parcela = round(float(args[12].replace(',', '.')) / qtde_parcela, 2)
    dt_emissao = datetime.strptime(args[3], '%d/%m/%Y')
    dt_vencimento = datetime.strptime(args[4], '%d/%m/%Y')

    if int(args[11]) == 1:
        insert_db(args[0], args[1], args[2], dt_emissao.strftime('%Y-%m-%d'), dt_vencimento.strftime('%Y-%m-%d'), args[5], args[6], args[7], args[8], args[9],
                  args[10], args[11], args[11], args[12].replace(',', '.'), args[12].replace(',', '.'), args[13])

    elif int(args[11]) > 1:
        parcela = 1

        while True:
            insert_db(args[0], args[1], args[2], dt_emissao.strftime('%Y-%m-%d'), dt_vencimento.strftime('%Y-%m-%d'), args[5], args[6], args[7], args[8], args[9],
                      args[10], args[11], parcela, args[12].replace(',', '.'), valor_parcela, args[13])

            parcela += 1
            dt_vencimento = dt_vencimento + relativedelta(months=1)
            if parcela > qtde_parcela:
                break
