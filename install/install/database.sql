PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS packages (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT NOT NULL,
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
    package_id    INTEGER NOT NULL,
    dependency_id INTEGER NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE,
    FOREIGN KEY (dependency_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS depend (
    package_id    INTEGER NOT NULL,
    dependency_id INTEGER NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE,
    FOREIGN KEY (dependency_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS idepend (
    package_id    INTEGER NOT NULL,
    dependency_id INTEGER NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE,
    FOREIGN KEY (dependency_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS bdepend (
    package_id    INTEGER NOT NULL,
    dependency_id INTEGER NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE,
    FOREIGN KEY (dependency_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS ndepend (
    package_id    INTEGER NOT NULL,
    dependency_id INTEGER NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE,
    FOREIGN KEY (dependency_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS fdepend (
    package_id    INTEGER NOT NULL,
    dependency_id INTEGER NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE,
    FOREIGN KEY (dependency_id) REFERENCES packages(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_files_path ON package_files(file_path);
CREATE INDEX IF NOT EXISTS idx_files_pkg_id ON package_files(package_id);
CREATE INDEX IF NOT EXISTS idx_rdepend_pkg_id ON rdepend(package_id);
CREATE INDEX IF NOT EXISTS idx_rdepend_dep_id ON rdepend(dependency_id);
CREATE INDEX IF NOT EXISTS idx_depend_pkg_id ON depend(package_id);
CREATE INDEX IF NOT EXISTS idx_idepend_pkg_id ON idepend(package_id);
CREATE INDEX IF NOT EXISTS idx_bdepend_pkg_id ON bdepend(package_id);
CREATE INDEX IF NOT EXISTS idx_ndepend_pkg_id ON ndepend(package_id);
CREATE INDEX IF NOT EXISTS idx_fdepend_pkg_id ON fdepend(package_id);