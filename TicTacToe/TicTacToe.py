from Board import gameboard
def ticTacToe():
    play = 'yes'
    while play in ('Yes','yes','y','Y'):
        #initialize board and values
        winner = 'None'
        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        location = 100000
        print('Welcome to Tic Tac Toe!')
        turncount = 0;

        #Select role
        player1=input('Player1: Do you want to be X or O?')
        if player1 in ('X','x'):
            player2 = 'O'
        elif player1 in ('O','o'):
            player2 = 'X'
        else:
            print('Enter a valid choice!')
        while player1 not in ('X','x','O','o'):     #Must be X or O
            player1=input('Player1: Do you want to be X or O?')
        print('Player 1 will go first.')
        currentMove = player1           #Player 1 goes first
        
        while winner == 'None':
            #win conditions
            def wincondition():
                for i in range (1,8,3):
                    if len(set(board[i:i+3]))==1 and board[i]!=' ':
                       return board[i]
                for i in range (1,4):
                    if len(set(board[i:i+7:3]))==1 and board[i]!=' ':
                        return board[i]
                if board[1]==board[5] and board[5]==board[9] and board[1]!=' ':
                    return board[1]
                if board[3]==board[5] and board[5]==board[7] and board[3]!=' ':
                    return board[3]
                return 'None'
            
            #in the event of a draw
            if winner == 'None' and turncount==9:
                 winner = 'Tie'
                 continue
                
            #Player moves
            if currentMove==player1:
                location = int(input("Player 1's move!(Choose 1-9)"))
                while location not in range(1,10) or board[location]!=' ':
                    location = int(input("Not valid spot, choose unoccupied 1-9"))
                board[location] = player1
                print('\n'*100)
                gameboard(board)
                winner=wincondition()
                currentMove=player2
                turncount+=1
                continue
            if currentMove==player2:
                location = int(input("Player 2's move!(Choose 1-9)"))
                while location not in range(1,10) or board[location]!=' ':
                    location = int(input("Not valid spot, choose unoccupied 1-9"))
                board[location] = player2
                print('\n'*100)
                gameboard(board)
                winner=wincondition()
                currentMove=player1
                turncount+=1
                continue             

        #Post-game
        if winner==player1:
            print(f'Player 1 ({player1}) wins!')
        elif winner==player2:
            print(f'Player 2 ({player2}) wins!')
        else:
            print('Tie game!')
        play = input('Do you want to keep playing? Yes or no?')
        while play not in ('Yes','yes','y','Y','No','no','N','n'):
            play = input('Not a valid response. Do you want to keep playing? Yes or no?')
