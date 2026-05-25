# Importar o conector do sqlite
import sqlite3

def conectar():
    conexao = sqlite3.connect("financas.db")
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            tipo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            data TEXT NOT NULL
                )
""")
    

    conexao.commit()
    conexao.close()

def inserir_transacao(descricao, valor, tipo, categoria, data):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO trasacoes (descricao, valor, tipo, categoria, data)
        VALUES (?, ?, ?, ?, ?)
""", (descricao, valor, tipo, categoria, data))
    
    conexao.commit()
    conexao.close()

def buscar_transacoes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM transacoes")
    transacoes = cursor.fetchall()

    conexao.close
    return transacoes

def deletar_transacoes(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM transacoes WHERE id = ?", (id,))

    conexao.commit()
    conexao.close()

def buscar_por_tipo(tipo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM transacoes WHERE tipo = ?", (tipo,))
    transacoes = cursor.fetchall()

    conexao.close()
    return transacoes

if __name__ == '__main__':
    criar_tabela()
    print("Banco criado com sucesso!")