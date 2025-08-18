import requests
from models.Municipio import Municipio
from helpers.database import db
from helpers.logging import logger

def extrair_municipios():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        for item in dados:
            co_municipio = item['id']
            no_municipio = item['nome']
            if item.get('microrregiao'):
                co_uf = item['microrregiao']['mesorregiao']['UF']['id']
            else:
                co_uf = item['regiao-imediata']['regiao-intermediaria']['UF']['id']

            municipio = Municipio(
                co_municipio=co_municipio,
                no_municipio=no_municipio,
                co_uf=co_uf
            )
            db.session.merge(municipio)
        db.session.commit()
        logger.info(f"{len(dados)} municípios inseridos com sucesso.")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao inserir municípios: {e}")
