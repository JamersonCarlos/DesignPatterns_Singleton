import pytest
from app.singleton import Mapa 
from app.territory import Territory
from app.jogador import Jogador

mapa = Mapa.instance(Mapa)
mapa.nomeMapa = 'Nether Minecraft'
mapa.players = [Jogador('*', 'Jamerson', mapa), Jogador('$', 'Alysson', mapa)]
listTerritories = []
countTerritory = 1
for i in range(3): 
    for g in range(14): 
        listTerritories.append(Territory(countTerritory, [i,g]))
        countTerritory += 1 
mapa.territories = listTerritories

def test_balanceamento():
    mapa.sortTerritories()
    players = mapa.getPlayers()
    countTerritoryPlayers = [0, 0]
    mapPlay = mapa.getMapa()
    for i in range(len(players)): 
        for g in range(3):
            for k in range(14):
                if(mapPlay[g][k] == players[i].id): 
                    countTerritoryPlayers[i] += 1 
    assert countTerritoryPlayers[0] == countTerritoryPlayers[1]
    