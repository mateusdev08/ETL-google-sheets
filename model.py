import os
import sqlite3 as con_sqlite
import mysql.connector as con_mysql
from dotenv import load_dotenv

load_dotenv()


def conectar_db_producao():
    global conexao_sqlite, cursor_sqlite

    conexao_sqlite = con_sqlite.connect(os.getenv('DB_PRODUCAO'))
    cursor_sqlite = conexao_sqlite.cursor()
    print('Conectado SQLITE')


def desconectar_db_producao():
    cursor_sqlite.close()
    conexao_sqlite.close()
    print('Desconectado SQLITE')


def conectar_db_dw():
    global conexao_mysql, cursor_mysql

    dados_mysql = {
        'host': os.getenv('HOST_DW'),
        'port': os.getenv('PORT_DW'),
        'user': os.getenv('USER_DW'),
        'password': os.getenv('PASSWORD_DW'),
        'database': os.getenv('DATABASE_DW')
    }

    conexao_mysql = con_mysql.connect(**dados_mysql)
    cursor_mysql = conexao_mysql.cursor()
    print('Conectado MySQL')


def desconectar_db_dw():
    cursor_mysql.close()
    conexao_mysql.close()
    print('Desconectado MySQL')
