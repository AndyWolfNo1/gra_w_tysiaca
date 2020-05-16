from gra_w_tysiaca.klass.Tactics import *
from gra_w_tysiaca.klass.Tactic_first import *


class Player:
    """Klasa definiuje gracza, przyjmuje tylko jeden argument, imię. """
    def __init__(self, name):
        self.ID = int()
        self.name = name
        self.tactic = False

    def __str__(self):
        return self.name

    def __repr__(self):
        """ Metoda magiczna, wyświetla nazwę podczas wywołania obiektu"""
        return self.name
     
    def build_tactic(self):
        self.tactic = Tactic_first(self.name)
        return self.tactic
