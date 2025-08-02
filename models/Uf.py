from flask_restful import fields as flaskFields
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow import Schema, fields, validate

from helpers.database import db

uf_fields ={
    "co_uf": flaskFields.Integer,
    "no_uf": flaskFields.String,
    "sg_uf": flaskFields.String,
}

class Uf(db.Model):
    __tablename__ = "tb_uf"

    co_uf: Mapped[int] = mapped_column(primary_key=True)
    no_uf: Mapped[str] = mapped_column(String)
    sg_uf: Mapped[str] = mapped_column(String)
    entidades = relationship("Entidade", back_populates="uf")

    def __init__(self, co_uf:int, no_uf:str, sg_uf:str):
        self.co_uf = co_uf
        self.no_uf = no_uf
        self.sg_uf = sg_uf

    def __repr__(self):
        return f"{self.__class__.__name__}({self.no_uf!r})"
    
class UfSchema(Schema):
    co_uf = fields.Integer(required=True)
    no_uf = fields.String(required=True, validate=validate.Length(min=2, max=100))
    sg_uf = fields.String(required=True, validate=validate.Length(equal=2))