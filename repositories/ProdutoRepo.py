import sqlite3
from typing import List, Optional
from models.Produto import Produto
from sql.ProdutoSql import *
from util.Database import criar_conexao

class ProdutoRepo:
    @classmethod
    def criar_tabela(cls) -> bool:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_CRIAR_TABELA)
                return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    @classmethod
    def inserir(cls, produto: Produto) -> Produto or None:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR, (produto.nome, ))
                if cursor.rowcount > 0:
                    produto.id = cursor.lastrowid
                    return produto
        except sqlite3.Error as e:
            print(e)
            return None
        
    @classmethod
    def obter_todos(cls) -> List[Produto]:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                produtos = cursor.execute(SQL_OBTER_TODOS).fetchall()
                return [Produto(*p) for p in produtos]
        except sqlite3.Error as e:
            print(e)
            return None
                
    @classmethod
    def alterar(cls, produto: Produto) -> Produto or None:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_ALTERAR, (produto.nome, produto.id))
                if cursor.rowcount > 0:
                    return produto                
        except sqlite3.Error as e:
            print(e)
            return None
        
    @classmethod
    def excluir(cls, id_produto: int) -> bool or False:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_EXCLUIR, (id_produto,))
                if cursor.rowcount > 0:
                    return True                
        except sqlite3.Error as e:
            print(e)
            return None
        
    @classmethod
    def obter_um(cls, id_produto: int) -> Produto or None:
        try:
            with criar_conexao() as conexao:
                cursor = conexao.cursor()
                produto = cursor.execute(SQL_OBTER_UM, (id_produto, )).fetchone()
                return Produto(*produto)
        except sqlite3.Error as e:
            print(e)
            return None