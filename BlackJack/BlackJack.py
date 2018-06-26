from Player import Player
from DeckClass import DeckofCards
def blackJack():
    '''
    Blackjack by Joseph M
    '''
    print("Welcome to BlackJack")
    play = 'yes'
    player = Player()
    dealer = Player()
    
    player.chips=int(input("How many chips do you have?"))
    
    while play in ('Yes','yes','y','Y'):

        #initiaize the game
        print("\nStarting the game.")
        deck = DeckofCards()
        deck.shuffleDeck()
        print("Deck has been shuffled. Dealing cards")
        player.cards.extend(deck.initDeal())
        dealer.cards.extend(deck.initDeal())
        print("Cards have been dealt.")
        print("Your cards:")
        print (" + ".join([str(x) for x in player.cards]))
        print("Dealer cards:")
        print(f"{dealer.cards[0]} + (?)")
        player.bet()

        #game loop
        while not player.checkBust()[0] and not dealer.checkBust()[0]:
            choice = player.makeMove()
            dealerTotal = dealer.checkBust()[1]
            if choice in ('stay','Stay'):
                print("You stayed. Your cards:")
                print (" + ".join([str(x) for x in player.cards]))
                playerTotal = player.checkBust()[1]
                print (f"Your total: {playerTotal}")
            else:
                player.cards.append(deck.draw())
                print("You hit. Your cards:")
                print (" + ".join([str(x) for x in player.cards]))
                playerTotal = player.checkBust()[1]
                print (f"Your total: {playerTotal}")
                continue
            while dealer.checkBust()[1] <=17:
                dealer.cards.append(deck.draw())
                dealerTotal = dealer.checkBust()[1]
            print("-"*50) #Formatting
            break
                
        #win conditions
        if dealer.checkBust()[0]:
            print(f"Dealer BUST! Dealer total: {dealerTotal}")
            player.chips+=player.lastBet
            print(f"You now have: {player.chips} chips")
        elif player.checkBust()[0]:
            print("BUST. Your total: {playerTotal}.")
        elif dealerTotal > playerTotal:
            print(f"Dealer wins. {dealerTotal} > {playerTotal}")
        elif dealerTotal < playerTotal:
            print(f"You win! {playerTotal} > {dealerTotal}")
            player.chips+=player.lastBet
            print(f"You now have: {player.chips} chips")
        else:
            print(f"Same total. Dealer wins.")
        
        #Postgame        
        play = input('\nDo you want to keep playing? Yes or no?')
        while True:
            try:
                assert play in ('Yes','yes','y','Y','No','no','N','n')
            except AssertionError:
                play = input('Not a valid response. Do you want to keep playing? Yes or no?')
                continue
            else:
                if play in ('Yes','yes','y','Y'):
                    addChoice = input("Great, another round! Do you want to add in chips?")
                    if addChoice in ('Yes','yes','y','Y'):
                        player.addChips()
                    elif addChoice not in('No','no','n','N'):
                        print("Not a valid answer.")                        
                player.newGame()
                dealer.newGame()
                break
            
