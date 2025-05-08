class InstituicaoEnsino():
    def __init__(self, id, co_entidade, no_regiao, no_uf, no_municipio, no_entidade, qt_mat_bas, qt_mat_fund, qt_mat_med, no_mesorregiao,no_microrregiao):
        self.id = id
        self.co_entidade = co_entidade
        self.no_regiao = no_regiao
        self.no_uf = no_uf
        self.no_municipio = no_municipio
        self.no_entidade = no_entidade
        self.qt_mat_bas = qt_mat_bas
        self.qt_mat_fund = qt_mat_fund
        self.qt_mat_med = qt_mat_med
        self.no_mesorregiao = no_mesorregiao
        self.no_microrregiao = no_microrregiao

    def toDict(self):
        return {
            "id": self.id,
            "co_entidade": self.co_entidade,
            "no_regiao": self.no_regiao,
            "no_uf": self.no_uf,
            "no_municipio": self.no_municipio,
            "no_entidade": self.no_entidade,
            "qt_mat_bas": self.qt_mat_bas,
            "qt_mat_fund": self.qt_mat_fund,
            "qt_mat_med": self.qt_mat_med,
            "no_mesorregiao": self.no_mesorregiao,
            "no_microrregiao": self.no_microrregiao
        }