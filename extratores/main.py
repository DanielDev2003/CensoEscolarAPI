from .UfExtrator import extrair_ufs
from .MesorregiaoExtrator import extrair_mesorregioes
from .MicrorregiaoExtrator import extrair_microrregioes
from .MunicipioExtrator import extrair_municipios
from .EntidadeExtrator import main as importar_entidades
from helpers.logging import logger
from helpers.application import app


def main():
    with app.app_context():
        logger.info("🔹 Iniciando processo de ETL do Censo Escolar e IBGE 🔹")
        extrair_ufs()
        extrair_mesorregioes()
        extrair_microrregioes()
        extrair_municipios()
        importar_entidades()
        logger.info("✅ Processo completo! Todas as entidades foram carregadas.")

if __name__ == "__main__":
    main()