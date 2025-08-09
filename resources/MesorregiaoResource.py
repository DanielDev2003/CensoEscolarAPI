from helpers.logging import logger
from helpers.database import db

from flask_restful import Resource, marshal
from flask import request
from marshmallow import ValidationError

from models.Mesorregiao import Mesorregiao, mesorregiao_fields, MesorregiaoSchema

class MesorregiaoResource(Resource):
    def get(self):
        logger.info("Get - Mesorregião")

        try:
            page = request.args.get("page",1, type = int)
            limit = request.args.get("limit",10, type = int)

            stmt = db.select(Mesorregiao)
            pagination = db.paginate(stmt, page=page, per_page=limit)
            mesorregioes = pagination.items

        except ValidationError as e:
            return {"mensagem": "Problema com o banco de dados."}, 500

        return marshal(mesorregioes, mesorregiao_fields), 200

    def post(self):
        pass