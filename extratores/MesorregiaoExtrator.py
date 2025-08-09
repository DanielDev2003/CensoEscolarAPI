# extratores/MesorregiaoExtrator.py
import requests
from models.Mesorregiao import Mesorregiao
from helpers.database import db
from helpers.logging import logger

def extrair_mesorregioes():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/mesorregioes'
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        for item in dados:
            meso = Mesorregiao(
                co_mesorregiao=item['id'],
                no_mesorregiao=item['nome'],
                co_uf=item['UF']['id']
            )
            db.session.merge(meso)
        db.session.commit()
        logger.info(f"{len(dados)} mesorregiões inseridas com sucesso.")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao inserir mesorregiões: {e}")
