class Player:
    '''
    This is the player
    '''
     
    def __init__(self, chips = 0, lastBet=0):
        self.cards = []
        self.chips = chips
        self.lastBet = lastBet

    #Check if player has busted
    def checkBust(self):
        total = 0
        for aCard in self.cards:
            if aCard in ['J','Q','K']:
                total+=10
            elif aCard =='A':
                if (total+11) > 21:
                    total+=1
                else:
                    total+=11
            else:
                total+=aCard
        return total > 21, total
        
    #Bet moneys
    def bet(self):
        while True:
            try:
                betAmt = int(input("What's your bet? Minimum 5"))
                assert betAmt <= self.chips and betAmt >= 5
                self.chips-=betAmt
                print(f"Bet {betAmt} chips.\nAmount remaining: {self.chips}\n")
            except ValueError:
                print ("Invalid amount!")
                continue
            except:
                if betAmt > self.chips:
                    print ("Amount exceeds chip quantity!")
                elif betAmt < 5:
                    print ("Amount less than 5.")
                continue
            else:
                self.lastBet = betAmt*2
                break

    #Restart game, keep same chip count
    def newGame(self):
        self.cards=[]

    #Add more chips
    def addChips(self):
        while True:
            try:
                amount = int(input("How many do you want to add in?"))
            except TypeError:
                print ("Invalid amount!")
                continue
            else:
                self.chips+=amount
                print(f"You now have: {self.chips} chips\n")
                break

    def makeMove(self):
        while True:
            try:
                choice = input("Hit or stay?")
                assert choice in ('Hit','hit','stay','Stay')
            except:
                print('Not a valid option. Try again.')
                continue
            else:
                return choice
