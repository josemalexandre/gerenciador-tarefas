import sqlite3


DB_PATH = ('tarefas.db')


def conectar_bd():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON;')
    return conn


def criar_tabelas():
    conn = conectar_bd()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tarefas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarefa TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    print('Tabelas criadas com sucesso ✔')


if __name__ == '__main__':
    criar_tabelas()
    