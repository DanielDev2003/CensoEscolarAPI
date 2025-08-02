from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://censo_user:123456@localhost:5434/censo_escolar"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"


api = Api(app)