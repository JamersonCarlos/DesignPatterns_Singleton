import pytest
from app.jogador import Jogador
from app.singleton import Mapa

mapa = Mapa.instance


#Testando se dois objetos diferentes estão acessando a mesma instancia de classe 
@pytest.fixture()
def player1(): 
    return Jogador('*', 'Jamerson', mapa)

@pytest.fixture()
def player2(): 
    return Jogador('$', 'Alysson', mapa)

def test_sameMap(player1, player2): 
    assert player1.mapa == player2.mapa

