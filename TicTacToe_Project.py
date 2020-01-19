from IPython.display import clear_output #this function can clear the output so we don't have clutter
import time #using time.sleep in the code so we don't have issues with input sequence display in jypiter
from random import randint #used to randomly assign first player 

board = [[' ', ' ', ' '], 
         [' ', ' ', ' '], 
         [' ', ' ', ' ']]

player_turn = 'x' #using this to store player turn
entered_keys = [] #using this to check which keys are entered. we append the entered keys to the list


def clear_board ():
    global board #defining board as global, so we can change it inside the function
    global entered_keys #same for keys
    
    
    board = [[' ', ' ', ' '], 
         [' ', ' ', ' '], 
         [' ', ' ', ' ']]
    entered_keys = [] #clearing keys as well

def display_board(board):
    
    clear_output() #from IPython.display import clear_output, clears screen before displaying the modified board
    board_print = "{}|{}|{} \n-----\n{}|{}|{}\n-----\n{}|{}|{}".format(board[0][0], board[0][1],board[0][2],
                                                                       board[1][0], board[1][1],board[1][2],
                                                                       board[2][0], board[2][1],board[2][2])
    print(board_print)

def player_input():

    while True:
        try:
            player_choice = int(input(f'Player {player_turn.upper()}, choose where to place {player_turn.upper()} (1-9): ')) #converting input to INT
            if player_choice not in range(1,10): #user entered a number thats not between 1-9
                print("That's not a valid option, choose a NUMBER between 1 and 9.")
                continue
            elif player_choice in entered_keys: #user entered a key that was already entered
                print("That field is already taken, please choose an empty field.")
            else:           
                break #no issues with input, breaking out of while loop
        except: ##if there is an exception in converting the string to INT, In other words, user entered a letter
            print("That's not a valid option, choose a NUMBER between 1 and 9.")

    entered_keys.append(player_choice) 
    return player_choice

def winning_check (board): ### CHECK IF A PLAYER IS WINNING
    entered_keys.sort() #sorting list so we can check if it is the end of the game
    #check 1) horizontally 2) vertically 3) across (8 possible combinations), returing false will break out of the main loop and the game will end
    if board[0][0] == board[0][1] == board[0][2] == 'x' or board[1][0] == board[1][1] == board[1][2] == 'x' or  board[2][0] == board[2][1] == board[2][2] == 'x':
        print("X wins the game. Game over")
        return False
    elif board[0][0] == board[1][0] == board[2][0] == 'x' or board[0][1] == board[1][1] == board[2][1] == 'x' or  board[0][2] == board[1][2] == board[2][2] == 'x':
        print("X wins the game. Game over")
        return False
    elif board[0][0] == board [1][1] == board [2][2] == 'x' or board [2][0]==board[1][1]==board[0][2] =='x':
        print("X wins the game. Game over")
        return False
    elif board[0][0] == board[0][1] == board[0][2] == 'o' or board[1][0] == board[1][1] == board[1][2] == 'o' or  board[2][0] == board[2][1] == board[2][2] == 'o':
        print("O wins the game. Game over")
        return False
    elif board[0][0] == board[1][0] == board[2][0] == 'o' or board[0][1] == board[1][1] == board[2][1] == 'o' or  board[0][2] == board[1][2] == board[2][2] == 'o':
        print("O wins the game. Game over")
        return False
    elif board[0][0] == board [1][1] == board [2][2] == 'o' or board [2][0]==board[1][1]==board[0][2] =='o':
        print("O wins the game. Game over")
        return False
    #check if all spots are filled
    elif entered_keys == list(range(1,10)): #entered keys list already sorted above. Alternatively can use >= 9 as well, instead of creating a new list
        print("It's a DRAW. Nobody wins the game. Game over")
        return False
    return True ##returnign true to continue while loop

def change_player_turn(): #### CHANGE PLAYER TURN FUNCTION####, checks which player's turn is currently, and switches to the other one
    global player_turn
    if player_turn == 'x':
        player_turn = 'o'
    else:
        player_turn = 'x'

def board_update(player_input): #### UPDATE BOARD FUCNTION#### Updates board with the date entered from the player input function
    
    if player_input == 1:
        board[2][0] = player_turn
    elif player_input == 2:
        board[2][1] = player_turn
    elif player_input == 3:
        board[2][2] = player_turn
    elif player_input == 4:
        board[1][0] = player_turn
    elif player_input == 5:
        board[1][1] = player_turn
    elif player_input == 6:
        board[1][2] = player_turn
    elif player_input == 7:
        board[0][0] = player_turn
    elif player_input == 8:
        board[0][1] = player_turn
    elif player_input == 9:
        board[0][2] = player_turn
        
def random_first_player(): ###randomly assigning first player
    global player_turn 
        
    if randint(0,1) == 0:
        player_turn = 'x' 
    else:
        player_turn ='o'

def start_game(): #starts game
    
    random_first_player() #randomly choose first player
    
    clear_board () #clear board and output in case another game was played before
    #clear_output()
    
    display_board(board)
    
    print(f"It's time to begin a new game. Player {player_turn.upper()} goes first")

    

    while winning_check(board): ###IF no winner, func returns TRUE, if there;s a winner it will return False and we will leave the loop
        

        board_update(player_input()) #take input and update board
        display_board(board)
        change_player_turn()
       
def yes_no_game():
    
    multiple_games_text = ''
    
    while True:
        yes_no = input(f'Would you like to play a{multiple_games_text} game of Tic Tac Toe? Choose Y or N: ')
        if yes_no.lower() == 'y':
            start_game()
            multiple_games_text = 'nother' ##little trick, if playing multiple texts, this will change the printed question
            
        elif yes_no.lower() == 'n':
            clear_output()
            print("Closing the game")
            break
        else:
            print("Please write 'y' or 'n'. ")
            