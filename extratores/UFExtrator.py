# extratores/UfExtrator.py
import requests
from models.Uf import Uf
from helpers.database import db
from helpers.logging import logger

def extrair_ufs():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        for item in dados:
            uf = Uf(
                co_uf=item['id'],
                no_uf=item['nome'],
                sg_uf=item['sigla']
            )
            db.session.merge(uf)  # atualiza ou insere
        db.session.commit()
        logger.info(f"{len(dados)} UFs inseridas com sucesso.")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao inserir UFs: {e}")
