from flask import Flask, jsonify
from instituicoes import *

app = Flask(__name__)

instituicoes_lista = lerInstituicoes()
instituicoes_dict = listaToDict(instituicoes_lista)

@app.route("/")
def index():
    versao = {"versao":"0.0.1"}
    return jsonify(versao), 200

@app.get("/instituicao")
def getInstituicaoResource():
    return jsonify(instituicoes_lista), 200

@app.get("/instituicao/<int:id>")
def getInstituicaoByIdResource(id):
    instituicao = instituicoes_dict.get(id)
    if instituicao:
        return jsonify(instituicao), 200
    else:
        return jsonify({"erro": "Instituição não encontrada"}), 404

@app.delete("/instituicao/<int:id>")
def deleteInstituicaoByIdResource(id):
    if id in instituicoes_dict:
        instituicao = instituicoes_dict.pop(id)
        instituicoes_lista.remove(instituicao)
        escreverInstituicoes(instituicoes_lista)
        return jsonify({"mensagem": "Instituição removida com sucesso"}, instituicao), 200
    else:
        return jsonify({"erro": "Instituição não encontrada"}), 404