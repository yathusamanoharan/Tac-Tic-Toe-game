import random



def display_board(board):
    clear_output()  
    
    print('    |      |    ')
    print(' ' + board[7] + '  |  ' + board[8] + '   |   ' + board[9])
    print('    |      |')
    print('-----------------')
    print('    |      |  ')
    print(' ' + board[4] + '  |  ' + board[5] + '   |   ' + board[6])
    print('    |      |')
    print('-----------------')
    print('    |      |  ')
    print(' ' + board[1] + '  |  ' + board[2] + '   |   ' + board[3])
    print('    |      |')
    
'''
 function on a test version of the board list, and make adjusments as necessary

'''


test_board = ['a', 'x','o', 'x','o', 'x','o', 'x','o', 'x']
display_board(test_board)

'''
function that can take in a player input and assign their markers as 'x' or 'o'. 
Think about using while loops ti continually ask until you ger acorrect answer.
'''

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be x or o?').upper()
        
    if marker == 'x':
        return ('x', 'o')
    else:
        return ('0', 'x')


'''
function to make sure it returns the desired output
'''

player_input()

'''
 function that takes in the board list object, a marker ('X', 'O') and a disered position (number 1-9) and 
 assigns it to the board
'''

def place_marker(board, marker, position):
    board[position] = marker

'''
function using test parameters and display the modified board
'''

place_marker(test_board, '$',8)
display_board(test_board)

'''
function that takes in a board and checks to see if someone has won

'''


def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

'''win_check function against our test_board - it should return True'''

win_check(test_board, 'x')



def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

'''
function that returns a boolean indicating whether a space on the board is freely available
'''

def space_check(board, position):
    return board[position] == ' '

'''function that checks if the board is full and returns a boolean avalue.True if full, False otherwise'''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

'''function that asks for a player's next position (as a number 1-9) and
then uses the function from step 6 to check if its a free position. If its, then return the position for later use
'''

def player_choice(board, player):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(player + 'Choose your next position: (1-9)'))
        
    return position

'''function that asks the player if they want to play again and returns a boolean True if they do want to play again.'''

def replay():
    return input('Do you want to play again? Enter Yes or No ').lower().startswith('y')


def game_logic():
        
    print('Welcome to Tic Tac Toe!')

    while True:
        theBoard = [' '] * 10
        print(theBoard)
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + 'will go first.')
        
        play_game = input('Are you ready to play? Enter Yes or No.')
        
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False
            
        while game_on:
            if turn == 'Player 1':
                
                display_board(theBoard)
                position = player_choice(theBoard, 'Player-1')
                place_marker(theBoard, player1_marker,position)
                
                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False
                
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                        
                    else:
                        turn = 'Player 2'
                        
            else:

                display_board(theBoard)
                position = player_choice(theBoard, 'Player-2')
                place_marker(theBoard, player2_marker,position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False

                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break

                    else:
                        turn = 'Player 1'

        if not replay():
            break

game_logic()