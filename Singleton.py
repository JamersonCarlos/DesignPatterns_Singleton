import random
#Singleton em Python
class Mapa(): 
    _instance = None

    def __init__(self):
        self.nomeMapa = None
        self.territories = None   
        self.mapaMatriz = None
        self.players = None    
    
    
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
        
    @classmethod
    def getMapa(self): 
        return self.mapaMatriz    
            
    @classmethod
    def getTerritories(self): 
        return self.territories 

    @classmethod
    def getPlayers(self): 
        return self.players
    
    def sortTerritories(self): 
        for i in range(len(self.players)):
            qtdTerritóriosPlayer = 0 
            while qtdTerritóriosPlayer < (42 / len(self.players)): 
                l = random.randint(0, 2)
                c = random.randint(0, 13)
                if(self.mapaMatriz[l][c] == '|'): 
                    self.mapaMatriz[l][c] = self.players[i].id
                    qtdTerritóriosPlayer += 1 
        return 'Territórios sorteados para cada jogador'
            
    def testMapa(self):

        teste = True 
        for i in range(len(self.mapaMatriz)): 
            for c in range(len(self.mapaMatriz[0])): 
               if(self.mapaMatriz[i][c] == '|'): 
                   teste = False
        if teste: 
            return 'Mapa ok!'
        else: 
            return 'Mapa com territórios vazios' 
    
        