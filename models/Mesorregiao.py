from flask_restful import fields as flaskFields
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow import Schema, fields, validate

from helpers.database import db

mesorregiao_fields = {
    'co_mesorregiao': flaskFields.Integer,
    'no_mesorregiao': flaskFields.String,
    'co_uf': flaskFields.Integer
}

class Mesorregiao(db.Model):
    __tablename__ = 'tb_mesorregiao'

    co_mesorregiao : Mapped[int] = mapped_column(primary_key=True)
    no_mesorregiao: Mapped[str] = mapped_column(String)
    co_uf: Mapped[int] = mapped_column(ForeignKey("tb_uf.co_uf"))
    entidades = relationship("Entidade", back_populates="mesorregiao")
    def __init__(self, co_mesorregiao:int, no_mesorregiao:str, co_uf:int):
        self.co_mesorregiao = co_mesorregiao
        self.no_mesorregiao = no_mesorregiao
        self.co_uf = co_uf
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.no_mesorregiao!r})"


class MesorregiaoSchema(Schema):
    co_mesorregiao = fields.Integer(required=True)
    no_mesorregiao = fields.String(required=True)
    co_uf = fields.Integer(required=True)