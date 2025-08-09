from helpers.logging import logger
from helpers.database import db

from flask_restful import Resource, marshal
from flask import request
from marshmallow import ValidationError

from models.Municipio import Municipio, municipio_fields, MunicipioSchema

class MunicipioResource(Resource):
    def get(self):
        logger.info("Get - Municipios")

        try:
            page = request.args.get("page",1, type = int)
            limit = request.args.get("limit",10, type = int)

            stmt = db.select(Municipio)
            pagination = db.paginate(stmt, page=page, per_page=limit)
            municipios = pagination.items

        except ValidationError as e:
            return {"mensagem": "Problema com o banco de dados."}, 500

        return marshal(municipios, municipio_fields), 200

    def post(self):
        pass