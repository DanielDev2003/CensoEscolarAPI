import json

def lerInstituicoes():
    with open("instituicoes.json", "r", encoding="utf-8") as meu_json:
        instituicoes_lista = json.load(meu_json)
    return instituicoes_lista

def escreverInstituicoes(lista):
    with open("instituicoes.json", "w") as meu_json:
        json.dump(lista, meu_json)

def listaToDict(array):
    instituicoes_dict = {item["CO_ENTIDADE"]: item for item in array}
    return instituicoes_dict


