from enum import Enum, auto
from dataclasses import dataclass



class Classe(Enum):
    MAGO = auto()
    GUERREIRO = auto()
    ARQUEIRO = auto()
    TANQUE = auto()


@dataclass
class Jogador:
    classe:Classe
    nivel: int
    vida: int
    xp: int

def CirarPersonagem():
    classe = input("Digite a classe desejada:\n1 - Arqueiro\n2 - Mago\n3 - Guerreiro\n4 - Tanque")
    if classe == 1:
        jogador =  Jogador(Classe.ARQUEIRO, 0, 80, 0)
    if classe == 2:
        jogador = Jogador(Classe.MAGO, 0, 60, 0)
    if classe == 3:
        jogador = Jogador(Classe.GUERREIRO, 0, 90, 0)
    if classe == 4:
        jogador = Jogador(Classe.TANQUE, 0, 100, 0)

    return jogador

def ExpdoPersonagem(jogador:Jogador):
    jogador.xp += 5
    if jogador.xp >= 10:
        jogador.xp = 0
        jogador.nivel += 1
        
    return jogador


    
