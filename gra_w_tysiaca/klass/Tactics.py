

class Tactic:
    """ Klasa definiuje taktykę gracza"""
    def __init__(self, name):
        self.player_name = name
        self.ID = int()
        self.colors = {'trefl': 0, 'pik': 0, 'kier': 0, 'karo': 0}
        self.cards = []
        self.licit = False
        self.hand = []
        self.master = self.colors
        self.master_t = self.colors
        self.sum_cards = int()
        self.point_t = self.colors
        self.point_sum = []
        self.trumf = False
        self.show_handd = False

    def get_cards(self, cards:list):
        """ Metoda  pobierająca listę kart, przypisuje otrzymane karty do self.cards"""
        for i in cards:
            self.cards.append(i)

    def show_hand(self):
        debug_list = list()
        for i in self.hand:
            if len(i) == 0:
                print('puste')
            else:
                for j in i:
                    debug_list.append(j)
        self.show_handd = debug_list

    def clear_hand(self):
        self.cards = []
        self.hand = []
        self.licit = False
        self.master = self.colors
        self.master_t = self.colors
        self.sum_cards = int()
        self.trumf = False
        self.point_t = self.colors
        self.point_sum = []

    def sum_points(self):
        for i in self.master.keys():
            pt = int(self.master[i])
            if pt == 70:
                self.master_t[i] += self.cards[0].val_suits[i]
        for i in self.hand:
            for j in i:
                self.point_t[j.color] += j.value

    def count_cards(self):
        """ Metoda sortująca karty, sumowania punktów {self.sum_cards},
            sprawdza karty "Q" i "K" z tego samego koloru {self.master}"""
        def sort(cards:list):
            color = ['A', 'K', 'Q', 'J', '10', '9']
            bufor = []
            for i in color:
                for j in range(len(cards)):
                    if i == cards[j].name:
                        bufor.append(cards[j])
            return bufor

        if len(self.cards) > 0:
            trefl = []
            pik = []
            kier = []
            karo = []
            self.hand = []
            for i in self.cards:
                if i.color == 'trefl':
                    trefl.append(i)
                elif i.color == 'pik':
                    pik.append(i)
                elif i.color == 'kier':
                    kier.append(i)
                else:
                    karo.append(i)
            alls = [sort(trefl), sort(pik), sort(kier), sort(karo)]
            for i in alls:
                self.hand.append(i)
            self.sum_cards = 0
            for i in alls:
                for j in i:
                    if j.name == "K":
                        self.master[j.color] += 40
                    elif j.name == "Q":
                        self.master[j.color] += 30
            for i in self.cards:
                self.sum_cards += i.value
            self.show_hand()
                    
        else:
            return "Brak kart na ręce"

    def play(self, stan:list):
        if stan < 0:
            self.card_in_table = stan[0]
            self.trumf = stan[1]
            self.licit = stan[2]
            ID_u_g = stan[3]
        if stan == 0:
            res = self.take_musik()
            return res

    def take_musik(self):
        res = []
        for i in range(3):
            res.append(self.cards[i])
        for i in range(3):
            self.cards.pop(0)
        return res
