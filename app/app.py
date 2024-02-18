from flask import Flask, jsonify, request
from singleton import Mapa
from jogador import Jogador
from territory import Territory
import json


app = Flask(__name__)
listIdentificationsPlayerMapa = ['%', '$', '*', '#']
mapa = Mapa.instance()
mapa.nomeMapa = 'Nether Minecraft'

@app.route('/setPlayers', methods=['POST'])
def setPlayers():
    try:
        data = request.json
        print(data['players'][1])
        if (len(data['players'])  < 4 and len(data['players']) > 0): 
            listPlayers = []
            for i in range(len(data['players'])): 
                listPlayers.append(Jogador(listIdentificationsPlayerMapa[i], data['players'][i], mapa))
            mapa.players = listPlayers
            resposta = {"mensagem": "Jogadores adicionados com sucesso!"}
            return jsonify(resposta)
        else: 
            resposta = {"mensagem": "Numero invalido de Jogadores"}
            return jsonify(resposta)

    except Exception as e:
        resposta_erro = {"erro": str(e)}
        return jsonify(resposta_erro), 400  

@app.route('/setTerritories', methods=['GET'])
def setTerritories(): 
    listTerritories = []
    for i in range(42): 
        listTerritories.append(Territory(i + 1, [0,0]))
    mapa.territories = listTerritories
    resposta = {"mensagem": "Territórios criados com sucesso"}
    return jsonify(resposta)

@app.route('/sortTerritories', methods=['GET'])
def sortTerritories(): 
    result = mapa.sortTerritories()
    resposta = {"mensagem": result}
    return jsonify(resposta)

@app.route('/testeMapa', methods=['GET'])
def testeMapa(): 
    result = mapa.testMapa()
    resposta = {"mensagem": result}
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)