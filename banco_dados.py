import sqlite3

def inicializar_banco():
    """Cria a tabela para armazenar os dados das crianças, se ainda não existir."""
    conn = sqlite3.connect('creche.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS criancas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL CHECK(idade > 0),
        nome_responsavel TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def adicionar_crianca(nome, idade, nome_responsavel):
    """Adiciona uma nova criança ao banco de dados."""
    try:
        conn = sqlite3.connect('creche.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO criancas (nome, idade, nome_responsavel)
        VALUES (?, ?, ?)
        ''', (nome, idade, nome_responsavel))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao adicionar criança: {e}")
        return False

def listar_criancas():
    """Retorna todos os registros das crianças no banco de dados."""
    try:
        conn = sqlite3.connect('creche.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM criancas')
        registros = cursor.fetchall()
        conn.close()
        return registros
    except Exception as e:
        print(f"Erro ao listar crianças: {e}")
        return []

def atualizar_crianca(id_crianca, nome, idade, nome_responsavel):
    """Atualiza os dados de uma criança existente."""
    try:
        conn = sqlite3.connect('creche.db')
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE criancas
        SET nome = ?, idade = ?, nome_responsavel = ?
        WHERE id = ?
        ''', (nome, idade, nome_responsavel, id_crianca))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao atualizar criança: {e}")
        return False

def remover_crianca(id_crianca):
    """Remove uma criança do banco de dados."""
    try:
        conn = sqlite3.connect('creche.db')
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM criancas
        WHERE id = ?
        ''', (id_crianca,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao remover criança: {e}")
        return False
