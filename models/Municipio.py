from flask_restful import fields as flaskFields
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow import Schema, fields, validate

from helpers.database import db

municipio_fields = {
    'co_mesorregiao': flaskFields.Integer,
    'no_mesorregiao': flaskFields.String,
    'co_uf': flaskFields.Integer
}

class Municipio(db.Model):
    __tablename__ = 'tb_municipio'

    co_municipio : Mapped[int] = mapped_column(primary_key=True)
    no_municipio: Mapped[str] = mapped_column(String)
    co_uf: Mapped[int] = mapped_column(ForeignKey("tb_uf.co_uf"))
    entidades = relationship("Entidade", back_populates="municipio")
    def __init__(self, co_municipio:int, no_municipio:str, co_uf:int):
        self.co_municipio = co_municipio
        self.no_municipio = no_municipio
        self.co_uf = co_uf
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.no_municipio!r})"
    
class MunicipioSchema(Schema):
    co_municipio = fields.Integer()
    no_municipio = fields.String()
    co_uf = fields.Integer()
