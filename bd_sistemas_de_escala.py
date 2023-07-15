import sqlite3
from datetime import datetime, date
from sqlite3 import Error
import os

def conexao_banco():
    dir = os.path.dirname(__file__)
    caminho = f"{dir}/banco_sistema_de_escala.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
        return con
    except Error as error:
        print(error)
def inserir(insert):
    try:
        con = conexao_banco()
        cursor = con.cursor()
        cursor.execute(insert)
        con.commit()
        con.close()
        print("Inserido com sucesso")
    except Error as error:
        print(error)

def atualizar(update):
    try:
        con = conexao_banco()
        cursor = con.cursor()
        cursor.execute(update)
        con.commit()
        con.close()
        print("Atualizado com sucesso")
    except Error as error:
        print(error)

def deletar(delete):
    try:
        con = conexao_banco()
        cursor = con.cursor()
        cursor.execute(delete)
        con.commit()
        con.close()
        print("Removido com sucesso")
    except Error as error:
        print(error)

def consultar(consultar):
    try:
        con = conexao_banco()
        cursor = con.cursor()
        cursor.execute(consultar)
        valores = cursor.fetchall()
        con.close()
        return valores
    except Error as error:
        print(error)

def consultar_usuarios(consultar):
    try:
        con = conexao_banco()
        cursor = con.cursor()
        cursor.execute(consultar)
        dados = cursor.fetchall()
        lista = []
        for tupla in dados:
            for valores in tupla:
                lista.append(valores)
        #dados = " ".join("".join(var) for var in dados)
        return lista
    except Error as error:
        print(error)