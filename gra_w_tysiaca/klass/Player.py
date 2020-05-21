#from gra_w_tysiaca.klass.Tactics import *
#from gra_w_tysiaca.klass.Tactic_first import *


class Player:
    """Klasa definiuje gracza, przyjmuje tylko jeden argument, imię. """
    def __init__(self, name, chair):
        self.ID = int()
        self.name = name
        self.chair = chair
        self.tactic = False

    def __str__(self):
        return self.name

    def __repr__(self):
        """ Metoda magiczna, wyświetla nazwę podczas wywołania obiektu"""
        return self.name
     
    def build_tactic(self):
        self.tactic = Tactic_first(self.name)
        return self.tactic

def create_players(tupla):
    list_players = []
    for i in tupla:
        gracz = Player(i[1], i[2])
        list_players.append(gracz)
    return list_players
    

gracze_razem = ((1,'buczo',2,11),(2,'lasza',1,11),(4,'polmos',4,11),(5,'sebix',3,11))

def gracze_dict(gr):
    result_d = {}
    result_l = []
    for i in range(4):
        result_d[gr[i][2]] = gr[i][1]
    return result_d
