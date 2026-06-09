import os, sqlite3
db = "/var/lib/bpm/main.db"
deps = ['rdepend', 'depend', 'idepend', 'bdepend', 'ndepend', 'fdepend']
try:
    os.makedirs(os.path.dirname(db), exist_ok=True)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("CREATE TABLE IF NOT EXISTS packages (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, version TEXT NOT NULL, provider TEXT NOT NULL, owner TEXT);")
    cursor.execute("CREATE TABLE IF NOT EXISTS package_files (package_id INTEGER NOT NULL, file_path TEXT NOT NULL UNIQUE, FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE);")
    for t in deps:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {t} (package_id INTEGER NOT NULL, dependency_id INTEGER NOT NULL, FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE, FOREIGN KEY (dependency_id) REFERENCES packages(id) ON DELETE CASCADE, PRIMARY KEY (package_id, dependency_id));")
        cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{t}_pkg_id ON {t}(package_id);")
        cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{t}_dep_id ON {t}(dependency_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_files_path ON package_files(file_path);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_files_pkg_id ON package_files(package_id);")
    conn.commit()
    print(f"Banco inicializado: {db}")
except (sqlite3.Error, PermissionError) as e:
    print(f"Erro: {e}. Certifique-se de rodar como sudo.")
finally:
    if 'conn' in locals(): conn.close()