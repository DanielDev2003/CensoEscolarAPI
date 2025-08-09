from helpers.logging import logger
from helpers.database import db

from flask_restful import Resource, marshal
from sqlalchemy.exc import SQLAlchemyError
from flask import request
from marshmallow import ValidationError

from models.Entidade import Entidade, entidade_fields, EntidadeSchema
from models.Uf import Uf
from models.Municipio import Municipio

class EntidadeResource(Resource):
    def get(self):
        logger.info("Get - Entidades")

        try:
            page = request.args.get("page",1, type = int)
            limit = request.args.get("limit",10, type = int)

            #entidades = Entidade.query.limit(limit).offset(offset).all()

            stmt = db.select(Entidade)
            pagination = db.paginate(stmt, page=page, per_page=limit)
            entidades = pagination.items

        except SQLAlchemyError as e:
            return {"mensagem": "Problema com o banco de dados."}, 500

        return marshal(entidades, entidade_fields), 200

    def post(self):
        pass

class EntidadeConsultaAnoResource(Resource):
    def get(self):
        logger.info("Get - Ano Instituições")
        try:

            stmt = db.select(Entidade.ano_censo).distinct().order_by(Entidade.ano_censo.desc())
            result = db.session.execute(stmt).all()
            lista_anos = [{"ano": row[0]} for row in result]

            return lista_anos, 200 
        
        except SQLAlchemyError as e:
            return {"mensagem": "Problema com o banco de dados."}, 500

class EntidadeConsultaMatriculaEstadoResource(Resource):
    def get(self):
        logger.info("Get - Quantidade de matrículas por estado")

        try:
            ano_censo = request.args.get("ano", default=2023, type=int)

            stmt = (
                db.select(
                    Uf.no_uf.label("estado"),
                    db.func.sum(Entidade.qt_mat_bas).label("matriculas")
                )
                .select_from(Uf)
                .join(Uf.entidades)  # Join usando o relationship UF -> Entidade
                .where(Entidade.ano_censo == ano_censo)
                .group_by(Uf.no_uf)
                .order_by(Uf.no_uf)
            )

            result = db.session.execute(stmt).all()

            lista = [
                {"estado": row.estado, "matriculas": row.matriculas}
                for row in result
            ]

            return lista, 200

        except ValidationError as e:
            logger.error(f"Erro no banco de dados: {e}")
            return {"mensagem": "Problema com o banco de dados."}, 500

class EntidadePConsultaMatriculaCidadeResource(Resource):
    def get(self):
        logger.info("Get - Quantidade de matriculas por cidade")
        
        try:
            ano_censo = request.args.get("ano", default=2023, type=int)
            sigla = request.args.get("sigla", default='PB', type=str)

            logger.info(f"Parâmetros recebidos: ano_censo={ano_censo}, sigla={sigla}")

            stmt = (
                db.select(
                    Municipio.no_municipio.label("municipio"),
                    db.func.sum(Entidade.qt_mat_bas).label("matriculas")
                )
                .select_from(Entidade)
                .join(Entidade.municipio)
                .join(Entidade.uf)
                .where(
                    Entidade.ano_censo == ano_censo,
                    Uf.sg_uf == sigla
                )
                .group_by(Municipio.no_municipio)
                .order_by(Municipio.no_municipio)
            )

            result = db.session.execute(stmt).all()

            lista = [
                {"municipio": row.municipio, "matriculas": row.matriculas}
                for row in result
            ]

            return lista, 200 
        
        except ValidationError as e:
            logger.error(f"Erro no banco de dados: {e}")
            return {"mensagem": "Problema com o banco de dados."}, 500