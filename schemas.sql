DROP TABLE IF EXISTS tb_instituicao;

CREATE TABLE tb_instituicao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    co_entidade INTEGER,
    no_regiao TEXT NOT NULL,
    no_uf TEXT NOT NULL,
    no_municipio TEXT NOT NULL,
    no_entidade TEXT NOT NULL,
    qt_mat_bas INTEGER,
    qt_mat_fund INTEGER,
    qt_mat_med INTEGER,
    no_mesorregiao TEXT NOT NULL,
    no_microrregiao TEXT NOT NULL
);