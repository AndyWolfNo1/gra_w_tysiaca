from random import shuffle
from gra_w_tysiaca.klass.Deck import *
from gra_w_tysiaca.klass.Card import *
from gra_w_tysiaca.klass.Player import *

class Table:
    """ Klasa definiująca stół. Stół tworzy talię kart, pobiera graczy {list},
        rozdaje karty, tworzy licytację, komunikacja z taktyką gracza.""" 
    def __init__(self, players:list):
        self.players = players
        self.cards = Deck()
        #self.auction = int()
        self.auction = [120, self.players[0]] # do wykasowania
        self.movement = ''
        self.trumf = ''
        self.musik = []

    def __str__(self):
        """ Metoda magiczna, wyświetla graczy w obiekcie print()"""
        return "Stół do gry:\n Gracze: {}".format(self.players)

    def __repr__(self):
        """ Metoda magiczna, wyświetla informacje o graczach"""
        return "Stół: {}".format(self.players)

    def expand(self):
        """ Metoda rozdaje karty graczom oraz 4 szt do self.musik."""
        for i in range(4):
            self.players[i].ID = i
        for i in self.players:
            tact = i.build_tactic()
            tact.clear_hand()
        cards = self.cards.take()
        shuffle(cards)
        self.get_music(cards[::6])
        list_list = [[cards[1], cards[2], cards[10], cards[11], cards[20]],
                     [cards[3], cards[4], cards[13], cards[14], cards[21]],
                     [cards[5], cards[7], cards[15], cards[16], cards[22]],
                     [cards[8], cards[9], cards[17], cards[19], cards[23]], ]
        for i in range(4):
            self.players[i].tactic.get_cards(list_list[i])
            self.players[i].tactic.sum_points()

    def get_music(self, card):
        """ Metoda pozwala dodac kartę graczowi."""
        self.musik.append(card)

    def reset_musik(self):
        """ Metoda czyszczenia danych"""
        self.musik = []

    def take_musik(self, stan:list):
        cards = stan[0]
        ID = int(stan[1])
        if ID == 0:
            self.players[1].tactic.get_cards([cards[0]])
            self.players[2].tactic.get_cards([cards[1]])
            self.players[3].tactic.get_cards([cards[2]])
        elif ID == 1:
            self.players[2].tactic.get_cards([cards[0]])
            self.players[3].tactic.get_cards([cards[1]])
            self.players[0].tactic.get_cards([cards[2]])
        elif ID == 2:
            self.players[3].tactic.get_cards([cards[0]])
            self.players[0].tactic.get_cards([cards[1]])
            self.players[1].tactic.get_cards([cards[2]])
        elif ID == 3:
            self.players[0].tactic.get_cards([cards[0]])
            self.players[1].tactic.get_cards([cards[1]])
            self.players[2].tactic.get_cards([cards[2]])

    def auct(self):
        """ Metoda wywołująca licytację graczy"""
        def dec(var):
            res = var%10
            return var - res
        players = self.players
        best = int()
        bp = None
        a = []
        while len(a)<3:
            for i in range(4):
                if players[i].licit == False:
                    res = input('Licytuje {}:\n'.format(players[i].name))
                    try:
                        res = int(res)
                        res = dec(res)
                        if res < best:
                            print('Za mało!')
                        elif res == best:
                            print('Za mało!')
                            players[i].licit = False
                        if res > best:
                            best = res
                            players[i].licit = best
                            bp = players[i]
                            print('Najlepsza', best)
                    except:
                        if res == 'p':
                            players[i].licit = 'p'
                            a.append('p')
                            if len(a)==4:
                                print('Gra zakończona')
                                a = []
                                for e in range(4):
                                    players[e].licit = False
                            elif len(a)==3:
                                best = input('{} daje swoją wartość:\n'.format(players[i+1].name))
                                bests = [best, players[i+1]]
                                self.auction = bests
                                return
                                                  
                elif players[i].licit != 'p' :
                        res = input('Aktualna wartość: {}\nLicytuje {}, {}:\n'.format(best, players[i].name, players[i].licit))
                        try:
                            res = int(res)
                            res = dec(res)
                            if res < best:
                                print('Za mało!')
                            elif res == best:
                                print('Tyle już ktoś dał')
                            elif res > best:
                                best = res
                                players[i].licit = res
                                bp = players[i]
                        except:
                            if res == 'p':
                                players[i].licit = 'p'
                                a.append('p')
                if len(a)==3:
                    best = [best, bp]
                    self.auction = best
                     
    def reset_hands(self):
        for i in range(4):
            self.players[i].tactic.count_cards()

    def clear_hands(self):
        for i in range(4):
            self.players[i].tactic.clear_hand()

    def clear(self):
        self.auction = [120, self.players[0]] # do wykasowania
        self.movement = ''
        self.trumf = ''
        self.musik = []
        self.clear_hands()

    def start(self):
        """ Metoda wywołująca start rozgrywki. Do skończenia!!!"""
        self.expand()
        #self.auct()
        # self.auction[1].tactic.get_cards(self.musik[0])
        # res = self.auction[1].tactic.play(0)
        # res = [res, self.auction[1].ID]
        # self.take_musik(res)
        self.reset_hands()
        

