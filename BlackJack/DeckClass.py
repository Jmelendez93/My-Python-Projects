from random import shuffle
class DeckofCards:
    '''
    This is the deck of cards class
    '''
    
    def __init__(self, cards = ([i for i in range(2,11)]+['A','J','Q','K'])*4):
        self.cards = cards

    def shuffleDeck(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop() #use list.append

    def initDeal(self):
        return[self.cards.pop(),self.cards.pop()] #use list.extend
