from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate

from helpers.application import app

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)
migrate = Migrate(app, db)


#LEGADO
# def getConnection():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = psycopg2.connect(host="localhost",
#                                             port=5434,
#                                             database="censo_escolar",
#                                             user="censo_user",
#                                             password="123456")
#     return db

#Banco Teste para a criação das tabelas com SQLAlchemy
# def getConnection():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = psycopg2.connect(user="postgres",
#                                             password="123456",
#                                             host="localhost",
#                                             port="5434",
#                                             database="orm_teste")
#     return db
 
# @app.teardown_appcontext
# def closeConnection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

#Conexão para os Extratores
# def connectDb():
#     conn = psycopg2.connect(
#         host="localhost",
#         port=5434,
#         database="censo_escolar",
#         user="censo_user",
#         password="123456"
#     )
#     return conn
