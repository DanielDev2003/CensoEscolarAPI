from helpers.logging import logger
from helpers.database import db

from flask_restful import Resource, marshal
from flask import request
from marshmallow import ValidationError

from models.Microrregiao import Microrregiao, microrregiao_fields, MicrorregiaoSchema

class MicrorregiaoResource(Resource):
    def get(self):
        logger.info("Get - Microrregião")

        try:
            page = request.args.get("page",1, type = int)
            limit = request.args.get("limit",10, type = int)

            stmt = db.select(Microrregiao)
            pagination = db.paginate(stmt, page=page, per_page=limit)
            microrregioes = pagination.items

        except ValidationError as e:
            return {"mensagem": "Problema com o banco de dados."}, 500

        return marshal(microrregioes, microrregiao_fields), 200

    def post(self):
        pass