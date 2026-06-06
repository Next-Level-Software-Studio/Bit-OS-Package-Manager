PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS packages (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT NOT NULL UNIQUE,
    version  TEXT NOT NULL,
    provider TEXT NOT NULL,
    owner    TEXT
);
CREATE TABLE IF NOT EXISTS package_files (
    package_id INTEGER NOT NULL,
    file_path  TEXT NOT NULL UNIQUE,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS rdepend (
    package_id INTEGER NOT NULL,
    atom       TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS depend (
    package_id INTEGER NOT NULL,
    atom       TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS idepend (
    package_id INTEGER NOT NULL,
    atom       TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS bdepend (
    package_id INTEGER NOT NULL,
    atom       TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS ndepend (
    package_id INTEGER NOT NULL,
    atom       TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS fdepend (
    package_id INTEGER NOT NULL,
    atom       TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_files_path ON package_files(file_path);
CREATE INDEX IF NOT EXISTS idx_files_pkg_id ON package_files(package_id);
CREATE INDEX IF NOT EXISTS idx_rdepend_pkg_id ON rdepend(package_id);
CREATE INDEX IF NOT EXISTS idx_depend_pkg_id ON depend(package_id);