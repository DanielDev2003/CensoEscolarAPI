from flask_restful import fields as flaskFields
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from helpers.database import db

entidade_fields = {
    "co_entidade": flaskFields.Integer,
    "no_entidade": flaskFields.String,
    "co_uf": flaskFields.Integer,
    "uf.no_uf": flaskFields.String,
    "uf.sg_uf": flaskFields.String,
    "co_municipio": flaskFields.Integer,
    "municipio.no_municipio": flaskFields.String,
    "co_mesorregiao": flaskFields.Integer,
    "mesorregiao.no_mesorregiao": flaskFields.String,
    "co_microrregiao": flaskFields.Integer,
    "microrregiao.no_microrregiao": flaskFields.String,
    "qt_mat_bas": flaskFields.Integer,
    "qt_mat_inf": flaskFields.Integer,
    "qt_mat_fund": flaskFields.Integer,
    "qt_mat_med": flaskFields.Integer,
    "qt_mat_med_ct": flaskFields.Integer,
    "qt_mat_med_nm": flaskFields.Integer,
    "qt_mat_prof": flaskFields.Integer,
    "qt_mat_prof_tec": flaskFields.Integer,
    "qt_mat_eja": flaskFields.Integer,
    "qt_mat_esp": flaskFields.Integer
}


class Entidade(db.Model):
    __tablename__ = 'tb_entidades'

    id: Mapped[int] = mapped_column(primary_key=True)
    co_entidade: Mapped[int] = mapped_column()
    no_entidade: Mapped[str] = mapped_column(String)
    
    co_uf: Mapped[int] = mapped_column(ForeignKey("tb_uf.co_uf"))
    co_municipio: Mapped[int] = mapped_column(ForeignKey("tb_municipio.co_municipio"))
    co_mesorregiao: Mapped[int] = mapped_column(ForeignKey("tb_mesorregiao.co_mesorregiao"))
    co_microrregiao: Mapped[int] = mapped_column(ForeignKey("tb_microrregiao.co_microrregiao"))


    uf = relationship("Uf", back_populates="entidades")
    municipio = relationship("Municipio", back_populates="entidades")
    mesorregiao = relationship("Mesorregiao", back_populates="entidades")
    microrregiao = relationship("Microrregiao", back_populates="entidades")

    qt_mat_bas: Mapped[int] = mapped_column()
    qt_mat_inf: Mapped[int] = mapped_column()
    qt_mat_fund: Mapped[int] = mapped_column()
    qt_mat_med: Mapped[int] = mapped_column()
    qt_mat_med_ct: Mapped[int] = mapped_column()
    qt_mat_med_nm: Mapped[int] = mapped_column()
    qt_mat_prof: Mapped[int] = mapped_column()
    qt_mat_prof_tec: Mapped[int] = mapped_column()
    qt_mat_eja: Mapped[int] = mapped_column()
    qt_mat_esp: Mapped[int] = mapped_column()
    ano_censo: Mapped[int] = mapped_column()

    def __init__(self, co_entidade, no_entidade, co_uf, no_uf, sg_uf ,co_municipio ,no_municipio, 
    co_mesorregiao, no_mesorregiao, co_microrregiao, no_microrregiao, qt_mat_bas, qt_mat_inf, qt_mat_fund, qt_mat_med, 
    qt_mat_med_ct, qt_mat_med_nm, qt_mat_prof, qt_mat_prof_tec, qt_mat_eja, qt_mat_esp):
        self.co_entidade = co_entidade
        self.no_entidade = no_entidade
        self.co_uf = co_uf
        self.no_uf = no_uf
        self.sg_uf = sg_uf
        self.co_municipio = co_municipio
        self.no_municipio = no_municipio
        self.co_mesorregiao = co_mesorregiao
        self.no_mesorregiao = no_mesorregiao
        self.co_microrregiao = co_microrregiao
        self.no_microrregiao = no_microrregiao
        self.qt_mat_bas = qt_mat_bas
        self.qt_mat_inf = qt_mat_inf
        self.qt_mat_fund = qt_mat_fund
        self.qt_mat_med = qt_mat_med
        self.qt_mat_med_ct = qt_mat_med_ct
        self.qt_mat_med_nm = qt_mat_med_nm
        self.qt_mat_prof = qt_mat_prof
        self.qt_mat_prof_tec = qt_mat_prof_tec
        self.qt_mat_eja = qt_mat_eja
        self.qt_mat_esp = qt_mat_esp
    def __repr__(self):
        return f"{self.__class__.__name__}({self.no_entidade!r})"