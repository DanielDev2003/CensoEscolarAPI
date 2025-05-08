from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('censoescolar.db')
    conn.row_factory = sqlite3.Row  # Permite acessar colunas como um dicionário
    return conn

@app.route("/")
def index():
    versao = {"versao": "0.0.1"}
    return jsonify(versao), 200

@app.get("/instituicao")
def get_all_instituicoes():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM tb_instituicao LIMIT 10 OFFSET 0")
    instituicoes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(instituicoes), 200

@app.get("/instituicao/<int:id>")
def get_instituicao_by_id(id):
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM tb_instituicao WHERE co_entidade = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify(dict(row)), 200
    else:
        return jsonify({"erro": "Instituição não encontrada"}), 404

@app.delete("/instituicao/<int:id>")
def delete_instituicao(id):
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM tb_instituicao WHERE co_entidade = ?", (id,))
    row = cursor.fetchone()
    if row:
        conn.execute("DELETE FROM tb_instituicao WHERE co_entidade = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Instituição removida com sucesso"}), 200
    else:
        conn.close()
        return jsonify({"erro": "Instituição não encontrada"}), 404
