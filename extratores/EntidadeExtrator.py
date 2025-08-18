import requests
import pandas as pd
from typing import Dict, Tuple, Optional
from pathlib import Path

from models.Entidade import Entidade
from helpers.database import db
from helpers.logging import logger

IBGE_MUNICIPIOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"


def _build_municipio_map(timeout: int = 30) -> Dict[int, Tuple[Optional[int], Optional[int]]]:
    """
    Retorna { co_municipio: (co_microrregiao_id_IBGE, co_mesorregiao_id_IBGE) }.
    """
    logger.info("Baixando mapa de municípios -> micro/meso do IBGE...")
    resp = requests.get(IBGE_MUNICIPIOS_URL, timeout=timeout)
    resp.raise_for_status()
    muni_map: Dict[int, Tuple[Optional[int], Optional[int]]] = {}

    for m in resp.json():
        co_mun = m.get("id")
        micro_id = None
        meso_id = None

        # Estrutura padrão
        if m.get("microrregiao"):
            try:
                micro_id = m["microrregiao"]["id"]
                meso_id = m["microrregiao"]["mesorregiao"]["id"]
            except (KeyError, TypeError):
                micro_id = None
                meso_id = None
        # (Fallback raro) Alguns registros antigos vêm com região imediata/intermediária
        elif m.get("regiao-imediata"):
            try:
                # Não há micro/meso nessa rota: manter None
                micro_id = None
                meso_id = None
            except (KeyError, TypeError):
                micro_id = None
                meso_id = None

        if isinstance(co_mun, int):
            muni_map[co_mun] = (micro_id, meso_id)

    logger.info(f"Mapa IBGE carregado: {len(muni_map)} municípios mapeados.")
    return muni_map


def _iter_chunks(csv_path: Path, chunksize: int, usecols):
    return pd.read_csv(
        csv_path,
        encoding="latin-1",
        delimiter=";",
        usecols=usecols,
        chunksize=chunksize,
        low_memory=False,
    )


def armazenar_entidades_csv(
    csv_path: Path,
    muni_map: Dict[int, Tuple[Optional[int], Optional[int]]],
    *,
    chunksize: int = 10000,
    strict: bool = True,  # strict=True: se não achar micro/meso, pula a linha (evita FK quebrar)
):
    cols = [
        "CO_ENTIDADE", "NO_ENTIDADE", "CO_UF", "CO_MUNICIPIO",
        # CSV tem CO_MESO/CO_MICRO mas serão ignorados/substituídos pelos do IBGE:
        "CO_MESORREGIAO", "CO_MICRORREGIAO",
        "QT_MAT_BAS", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED",
        "QT_MAT_MED_CT", "QT_MAT_MED_NM", "QT_MAT_PROF", "QT_MAT_PROF_TEC",
        "QT_MAT_EJA", "QT_MAT_ESP", "NU_ANO_CENSO",
    ]

    total = 0
    skipped = 0

    try:
        for chunk in _iter_chunks(csv_path, chunksize, cols):
            chunk.fillna(0, inplace=True)
            registros = chunk.to_dict(orient="records")

            for row in registros:
                co_mun = int(row["CO_MUNICIPIO"])
                micro_id, meso_id = muni_map.get(co_mun, (None, None))

                if strict and (micro_id is None or meso_id is None):
                    skipped += 1
                    continue  # evita violar FK

                ent = Entidade(
                    co_entidade=int(row["CO_ENTIDADE"]),
                    no_entidade=str(row["NO_ENTIDADE"]),
                    co_uf=int(row["CO_UF"]),
                    co_municipio=co_mun,
                    co_mesorregiao=meso_id,     # ← IDs IBGE corretos
                    co_microrregiao=micro_id,   # ← IDs IBGE corretos
                    qt_mat_bas=int(row["QT_MAT_BAS"]),
                    qt_mat_inf=int(row["QT_MAT_INF"]),
                    qt_mat_fund=int(row["QT_MAT_FUND"]),
                    qt_mat_med=int(row["QT_MAT_MED"]),
                    qt_mat_med_ct=int(row["QT_MAT_MED_CT"]),
                    qt_mat_med_nm=int(row["QT_MAT_MED_NM"]),
                    qt_mat_prof=int(row["QT_MAT_PROF"]),
                    qt_mat_prof_tec=int(row["QT_MAT_PROF_TEC"]),
                    qt_mat_eja=int(row["QT_MAT_EJA"]),
                    qt_mat_esp=int(row["QT_MAT_ESP"]),
                    ano_censo=int(row["NU_ANO_CENSO"]),
                )
                db.session.merge(ent)

            db.session.commit()
            total += len(registros)
            logger.info(f"{len(registros)} entidades processadas e inseridas.")

        msg_skip = f" (skipped={skipped})" if skipped else ""
        logger.info(f"Total final: {total} entidades inseridas com sucesso{msg_skip}.")

    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao processar CSV {csv_path}: {e}")
    finally:
        db.session.close()


def main():

    csv_2023 = Path(r"C:\Users\Daniel\Documents\Programação\IFPB-2025.1\PWeb II\microdados_censo_escolar_2023\dados\microdados_ed_basica_2023.csv")
    csv_2024 = Path(r"C:\Users\Daniel\Documents\Programação\IFPB-2025.1\PWeb II\microdados_censo_escolar_2024\dados\microdados_ed_basica_2024.csv")

    logger.info("Iniciando importação de entidades do Censo Escolar.")
    muni_map = _build_municipio_map()

    # strict=True evita violar FK (pula linhas sem mapeamento). Troque para False se suas FKs permitirem NULL.
    armazenar_entidades_csv(csv_2023, muni_map, chunksize=10000, strict=True)
    armazenar_entidades_csv(csv_2024, muni_map, chunksize=10000, strict=True)

    logger.info("Importação concluída.")
