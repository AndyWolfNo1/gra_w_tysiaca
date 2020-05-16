from gra_w_tysiaca.klass.Table import *
from gra_w_tysiaca.klass.Card import *
from gra_w_tysiaca.klass.Player import *
from gra_w_tysiaca.klass.Deck import *
from gra_w_tysiaca.klass.Tactics import *
from random import shuffle

p1 = Player('Seba')
p2 = Player('Tomek')
p3 = Player('Marcin')
p4 = Player('Buczo')
players = [p1, p2, p3, p4]
table = Table(players)

def ready():
    table.start()
   

card1 = Card("K", 0)
card2 = Card("Q", 0)
card3 = Card("K", 3)
card4 = Card("Q", 3)
card5 = Card("A", 0)
card6 = Card("10", 0)
list_card = [card1, card2, card5, card6]
#table.start()

##def test(ie:int):
##    gracze = {p1.name : 0, p2.name : 0, p3.name : 0, p4.name : 0}
##    res = []
##    for i in range(ie):
##        table.start()
##        print('rozgrywka nr:', i+1)
##        table.players[i].tactic.sum_points()
##        table.players[i].tactic.take_musik()
##        #res2 = table.players[i].tactic.hand
##        #table.players[i].tactic.clear_hand()
##        #print(res)
##        #print(res2)
##        
##
##def test2(ie:int):
##    gracze = {p1.name : 0, p2.name : 0, p3.name : 0, p4.name : 0}
##    res = []
##    for i in range(ie):
##        for i in range(4):
##            table.players[i].tactic.sum_points()
##    print(table.players[0].tactic.master_t)
##    print(table.players[0].tactic.hand)
