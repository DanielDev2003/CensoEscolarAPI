from flask_restful import fields as flaskFields
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow import Schema, fields, validate

from helpers.database import db

microrregiao_fields = {
    'co_microrregiao': flaskFields.Integer,
    'no_microrregiao': flaskFields.String,
    'co_uf': flaskFields.Integer
}

class Microrregiao(db.Model):
    __tablename__ = 'tb_microrregiao'

    co_microrregiao : Mapped[int] = mapped_column(primary_key=True)
    no_microrregiao: Mapped[str] = mapped_column(String)
    co_uf: Mapped[int] = mapped_column(ForeignKey("tb_uf.co_uf"))
    entidades = relationship("Entidade", back_populates="microrregiao")
    def __init__(self, co_microrregiao:int, no_microrregiao:str, co_uf:int):
        self.co_microrregiao = co_microrregiao
        self.no_microrregiao = no_microrregiao
        self.co_uf = co_uf
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.no_microrregiao!r})"

class MicrorregiaoSchema(Schema):
    co_microrregiao = fields.Integer()
    no_microrregiao = fields.String()
    co_uf = fields.Integer()