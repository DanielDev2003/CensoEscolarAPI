import sqlite3
import json
# 1 - Abri a conexão
connection = sqlite3.connect('censoescolar.db')

# 2 - Cursor

# 3 - Executar

conn = sqlite3.connect('censoescolar.db')
cursor = conn.cursor()

with open('schemas.sql', 'r', encoding='utf-8') as f:
    schema = f.read()
    cursor.executescript(schema)

conn.commit()
conn.close()

with open('instituicoes.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

conn = sqlite3.connect('censoescolar.db')
cursor = conn.cursor()

for inst in dados:
    cursor.execute('''
        INSERT OR REPLACE INTO tb_instituicao (
            co_entidade, no_regiao, no_uf, no_municipio, no_entidade,
            qt_mat_bas, qt_mat_fund, qt_mat_med,
            no_mesorregiao, no_microrregiao
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        inst['CO_ENTIDADE'],
        inst['NO_REGIAO'],
        inst['NO_UF'],
        inst['NO_MUNICIPIO'],
        inst['NO_ENTIDADE'],
        inst['QT_MAT_BAS'],
        inst['QT_MAT_FUND'],
        inst['QT_MAT_MED'],
        inst['NO_MESORREGIAO'],
        inst['NO_MICRORREGIAO']
    ))

conn.commit()
conn.close()

# 4 - Commit ou fecth
connection.commit()

# 5 - Fechar
connection.close()

