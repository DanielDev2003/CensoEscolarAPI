from flask import Flask, jsonify, request
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
    
@app.post("/instituicao")
def postInstituicaoResource():
    nova_instituicao = request.json

    if "CO_ENTIDADE" not in nova_instituicao:
        return jsonify({"erro": "Campo 'CO_ENTIDADE' obrigatório"}), 400
    if nova_instituicao["CO_ENTIDADE"] in instituicoes_dict:
        return jsonify({"erro": "CO_ENTIDADE já existe"}), 400

    # Adiciona à lista e ao dicionário
    instituicoes_lista.append(nova_instituicao)
    instituicoes_dict[nova_instituicao["CO_ENTIDADE"]] = nova_instituicao

    # Persiste no arquivo
    escreverInstituicoes(instituicoes_lista)

    return jsonify(nova_instituicao), 201

@app.put("/instituicao/<int:id>")
def putInstituicaoByIdResource(id):
    dados_atualizados = request.json

    if id not in instituicoes_dict:
        return jsonify({"erro": "Instituição não encontrada"}), 404

    dados_atualizados["CO_ENTIDADE"] = id

    instituicoes_dict[id] = dados_atualizados

    for i, inst in enumerate(instituicoes_lista):
        if inst["CO_ENTIDADE"] == id:
            instituicoes_lista[i] = dados_atualizados
            break

    escreverInstituicoes(instituicoes_lista)

    return jsonify(dados_atualizados), 200

@app.delete("/instituicao/<int:id>")
def deleteInstituicaoByIdResource(id):
    if id in instituicoes_dict:
        instituicao = instituicoes_dict.pop(id)
        instituicoes_lista.remove(instituicao)
        escreverInstituicoes(instituicoes_lista)
        return jsonify({"mensagem": "Instituição removida com sucesso"}, instituicao), 200
    else:
        return jsonify({"erro": "Instituição não encontrada"}), 404