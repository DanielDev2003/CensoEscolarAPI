# extratores/MicrorregiaoExtrator.py
import requests
from models.Microrregiao import Microrregiao
from helpers.database import db
from helpers.logging import logger

def extrair_microrregioes():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes'
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        for item in dados:
            micro = Microrregiao(
                co_microrregiao=item['id'],
                no_microrregiao=item['nome'],
                co_uf=item['mesorregiao']['UF']['id']
            )
            db.session.merge(micro)
        db.session.commit()
        logger.info(f"{len(dados)} microrregiões inseridas com sucesso.")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao inserir microrregiões: {e}")
