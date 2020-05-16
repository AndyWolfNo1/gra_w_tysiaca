

class Card:
    """ Klasa definiuje kartę do gry, przyjmuje 2 argumenty. Pierwszy
        argument to nazwa karty ['9', 10', 'J', 'Q', 'K', 'A'].
        Drugi argument to liczba od 0-3 która definouje kolor karty.
        Kolory kart ['trefl', 'pik', 'kier', 'karo']"""
    
    names = {'9':0, '10':10, 'J':2, 'Q':3, 'K':4, 'A':11}
    

    def __init__(self, name, color):
        """Konstruktor klasy, definiuje wartość danej karty oraz kolor. """
        self.name = name
        self.value = self.names[name]
        self.colors = ['trefl', 'pik',
                        'kier', 'karo']
        self.color = self.colors[color]
        self.val_suits = {'trefl' : 100, 'pik': 80,
                            'kier': 60, 'karo': 40}

    def __lt__(self, other):
        """ Metoda magiczna, definiuje możliwość porównywania < obiektów karty"""
        if self.value < other.value:
            return True
        return False
        
    def __gt__(self, other):
        """ Metoda magiczna, definiuje możliwość porównywania > obiektów karty"""
        if self.value > other.value:
            return True
        return False

    def __repr__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania obiektu"""
        return self.name+' '+self.color

    def __str__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania obiektu w obiekcie print()"""
        return "Nazwa:  {}\nKolor:  {}\nWartoś: {}".format(self.name,
                                                           self.color, self.value)

    def __eq__(self, other):
        """ Metoda magiczna, sprawdza równość wartości obiektów"""
        if self.value == other.value:
            return True
        return False

    def __add__(self, other):
        """ Metoda magiczna, dodaje dwa obiekty"""
        return self.value + other.value

    def __sub__(self, other):
        """ Metoda magiczna, odejmuje dwa obiekty"""
        return self.value - other.value





