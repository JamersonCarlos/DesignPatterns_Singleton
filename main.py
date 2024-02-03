import requests, json
from Singleton import Mapa

namePlayers = []
qtdPlayers = 0

print('------ Bem vindo ao Jogo ------')
print('História: Atualizar Mapa')
print('Max Jogadores = 3')
while True: 
    try: 
        qtdPlayers = int(input('Digite a quantidade de jogadores: '))
        break
    except ValueError: 
        print('Por favor, digite um numero inteiro válido')

for i in range(qtdPlayers): 
    namePlayers.append(input(f'Digite o nome do jogador {i}: '))

response = requests.post('http://127.0.0.1:5000/setPlayers', data=json.dumps({'players': namePlayers}), headers={'Content-Type': 'application/json'})
print(json.loads(response.text)['mensagem'])
response = requests.get('http://127.0.0.1:5000/setTerritories')
print(json.loads(response.text)['mensagem'])
response = requests.get('http://127.0.0.1:5000/sortTerritories')
print(json.loads(response.text)['mensagem'])
response = requests.get('http://127.0.0.1:5000/testeMapa')
print(json.loads(response.text)['mensagem'])