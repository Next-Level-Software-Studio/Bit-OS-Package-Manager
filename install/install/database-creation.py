import os, sqlite3
def init_db():
    db_path = "/var/lib/bpm/main.db"
    try: os.makedirs(os.path.dirname(db_path), exist_ok=True)
    except PermissionError:
        print("Erro: Sem permissão para criar o diretório '/var/lib/bpm/'.\nExecute o script como superusuário (sudo python3 init_db.py).")
        return
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("CREATE TABLE IF NOT EXISTS packages (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, version TEXT NOT NULL, provider TEXT NOT NULL, owner TEXT);")
        cursor.execute("CREATE TABLE IF NOT EXISTS package_files (package_id INTEGER NOT NULL, file_path TEXT NOT NULL UNIQUE, FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE);")
        for table in ['rdepend', 'depend', 'idepend', 'bdepend', 'ndepend', 'fdepend']:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} (package_id INTEGER NOT NULL, dependency_id INTEGER NOT NULL, FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE, FOREIGN KEY (dependency_id) REFERENCES packages(id) ON DELETE CASCADE);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_files_path ON package_files(file_path);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_files_pkg_id ON package_files(package_id);")
        for t in ['rdepend', 'depend', 'idepend', 'bdepend', 'ndepend', 'fdepend']:
            cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{t}_pkg_id ON {t}(package_id);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_rdepend_dep_id ON rdepend(dependency_id);")
        conn.commit()
        print(f"Banco de dados inicializado com sucesso em: {db_path}")
    except sqlite3.Error as e: print(f"Erro ao interagir com o SQLite: {e}")
    except PermissionError: print(f"Erro: Sem permissão para gravar em '{db_path}'. Execute como sudo.")
    finally:
        if 'conn' in locals(): conn.close()
if __name__ == "__main__": init_db()