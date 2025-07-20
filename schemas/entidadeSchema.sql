
DROP TABLE IF EXISTS tb_entidades;

CREATE TABLE IF NOT EXISTS tb_entidades(
    id SERIAL PRIMARY KEY,
    co_entidade INTEGER,
    no_entidade VARCHAR(100) NOT NULL,
    co_uf INTEGER NOT NULL,
    co_municipio INTEGER NOT NULL,
    co_mesorregiao INTEGER NOT NULL,
    co_microrregiao INTEGER NOT NULL,
    qt_mat_bas INTEGER,
    qt_mat_inf INTEGER,
    qt_mat_fund INTEGER,
    qt_mat_med INTEGER,
    qt_mat_med_ct INTEGER,
    qt_mat_med_nm INTEGER,
    qt_mat_prof INTEGER,
    qt_mat_prof_tec INTEGER,
    qt_mat_eja INTEGER,
    qt_mat_esp INTEGER,
    ano_censo INTEGER NOT NULL,
    FOREIGN KEY (co_uf) REFERENCES tb_UF(co_uf),
    FOREIGN KEY (co_municipio) REFERENCES tb_municipio(co_municipio),
    FOREIGN KEY (co_mesorregiao) REFERENCES tb_mesorregiao(co_mesorregiao),
    FOREIGN KEY (co_microrregiao) REFERENCES tb_microrregiao(co_microrregiao)
);

