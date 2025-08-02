from flask_restful import fields as flaskFields
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow import Schema, fields, validate

from models.Uf import UfSchema
from models.Mesorregiao import MesorregiaoSchema
from models.Microrregiao import MicrorregiaoSchema
from models.Municipio import MunicipioSchema

from helpers.database import db

entidade_fields = {
    "id": flaskFields.Integer,
    "co_entidade": flaskFields.Integer,
    "no_entidade": flaskFields.String,
    "co_uf": flaskFields.Integer,
    "uf": flaskFields.Nested({
        "co_uf": flaskFields.Integer,
        "no_uf": flaskFields.String,
        "sg_uf": flaskFields.String
    }),
    "co_municipio": flaskFields.Integer,
    "municipio": flaskFields.Nested({
        "co_municipio": flaskFields.Integer,
        "no_municipio": flaskFields.String
    }),
    "co_mesorregiao": flaskFields.Integer,
    "mesorregiao": flaskFields.Nested({
        "co_mesorregiao": flaskFields.Integer,
        "no_mesorregiao": flaskFields.String
    }),
    "co_microrregiao": flaskFields.Integer,
    "microrregiao": flaskFields.Nested({
        "co_microrregiao": flaskFields.Integer,
        "no_microrregiao": flaskFields.String
    }),
    "qt_mat_bas": flaskFields.Integer,
    "qt_mat_inf": flaskFields.Integer,
    "qt_mat_fund": flaskFields.Integer,
    "qt_mat_med": flaskFields.Integer,
    "qt_mat_med_ct": flaskFields.Integer,
    "qt_mat_med_nm": flaskFields.Integer,
    "qt_mat_prof": flaskFields.Integer,
    "qt_mat_prof_tec": flaskFields.Integer,
    "qt_mat_eja": flaskFields.Integer,
    "qt_mat_esp": flaskFields.Integer,
    "ano_censo":flaskFields.Integer
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

    def __init__(self, co_entidade, no_entidade, co_uf, co_municipio,
                 co_mesorregiao, co_microrregiao, qt_mat_bas, qt_mat_inf,
                 qt_mat_fund, qt_mat_med, qt_mat_med_ct, qt_mat_med_nm,
                 qt_mat_prof, qt_mat_prof_tec, qt_mat_eja, qt_mat_esp, ano_censo):
        self.co_entidade = co_entidade
        self.no_entidade = no_entidade
        self.co_uf = co_uf
        self.co_municipio = co_municipio
        self.co_mesorregiao = co_mesorregiao
        self.co_microrregiao = co_microrregiao
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
        self.ano_censo = ano_censo
    def __repr__(self):
        return f"{self.__class__.__name__}({self.no_entidade!r})"
    
class EntidadeSchema(Schema):
    co_entidade = fields.Integer(required=True)
    no_entidade = fields.String(required=True, validate=validate.Length(min=2, max=100))
    
    co_uf = fields.Integer(required=True)
    uf = fields.Nested(UfSchema, dump_only=True)

    co_municipio = fields.Integer(required=True)
    municipio = fields.Nested(MunicipioSchema, dump_only=True)

    co_mesorregiao = fields.Integer(required=True)
    mesorregiao = fields.Nested(MesorregiaoSchema, dump_only=True)

    co_microrregiao = fields.Integer(required=True)
    microrregiao = fields.Nested(MicrorregiaoSchema, dump_only=True)

    qt_mat_bas = fields.Integer(required=True)
    qt_mat_inf = fields.Integer(required=True)
    qt_mat_fund = fields.Integer(required=True)
    qt_mat_med = fields.Integer(required=True)
    qt_mat_med_ct = fields.Integer(required=True)
    qt_mat_med_nm = fields.Integer(required=True)
    qt_mat_prof = fields.Integer(required=True)
    qt_mat_prof_tec = fields.Integer(required=True)
    qt_mat_eja = fields.Integer(required=True)
    qt_mat_esp = fields.Integer(required=True)
    ano_censo = fields.Integer(required=True)