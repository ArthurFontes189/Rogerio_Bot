import sqlite3
from datetime import datetime


# Conexão com o banco
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()


# Criação da tabela de usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

#criação da tabela de anotações
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    note TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")
conn.commit()


# Registrar nome do usuario / Procurar usuario por ID
def register_name(user_id: int, name: str):
    cursor.execute("REPLACE INTO users (user_id, name) VALUES (?, ?)", (user_id, name))
    conn.commit()

def search_name(user_id: int):
    cursor.execute("SELECT name FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    return row[0] if row else None
############################################

def add_notes(user_id : int, note: str ):
    data = datetime.now().isoformat()
    cursor.execute("INSERT INTO notes (user_id, note, created_at) VALUES (?, ?, ?)", (user_id, note, data))
    conn.commit()

def list_notes(user_id: int):
    cursor.execute("SELECT id, note, created_at FROM notes WHERE user_id = ?", (user_id,))
    return cursor.fetchall()

def delete_note(note_id: int, user_id: int):
    cursor.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", (note_id, user_id))
    conn.commit()