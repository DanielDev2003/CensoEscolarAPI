from flask import request
from flask_restful import Resource, marshal
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

from helpers.logging import logger
from helpers.database import db

from models.Uf import Uf ,uf_fields


class UfResource(Resource):

    def get(self):
        logger.info("Get - Ufs")
        try:
            stmt = db.select(Uf)
            result = db.session.execute(stmt).scalars()
            ufs = result.all()

        except SQLAlchemyError as e:
            return {"mensagem": "Problema com o banco de dados."}, 500

        return marshal(ufs, uf_fields), 200
        
        