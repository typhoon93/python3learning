import random
from IPython.display import clear_output #this function can clear the output so we don't have clutter, workds in jupiter notebook

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card: 
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    
    def __init__(self):
        self.deck = [] #start with an empy list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    def __str__(self): # returns a string of all cards, use with print for good formating
        sequentialDeck = ""
        for card in self.deck:
            sequentialDeck += f'{str(card)}\n'
        return sequentialDeck
    def __len__(self): # returns how many cards we have in the deck
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
    
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.adjusted_for_aces = False #indicator if we have used adjust_for_ace once 
    
    def  add_card(self, card):
        #card passed in from Deck.deal()
        self.cards.append(card)
        if card.rank == 'Ace':
                self.aces +=1
                if self.aces>1:
                    self.value +=1 #if we have more than once ace in deck, 
                                    #only the first will be counted as 11,
                                     #each subsequent one if counted as 1
                else:
                    self.value +=values[card.rank]
        else:
            self.value +=values[card.rank]
        

    def adjust_for_ace(self):
        if self.value > 21 and self.aces > 0 and self.adjusted_for_aces == False:
                self.value = self.value - 10 
                self.adjusted_for_aces = True #indicating that we have now already ajusted
                                                # for aces, and we won't do it again
class Chips:  

    def __init__(self, total=100):
        self.total =  total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
        self.bet = 0
    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0
def take_bet(available_funds): #will pass in total Chips class
    print(f'Avaible Funds: {available_funds}\n')
    while True:
        try:
            bet_amount = int(input("Please input the amount you would like to bet: "))
            if bet_amount > available_funds: #checking if they have the funds
                print("You do not have enough funds.")
            else:
                break
        except: #in NAN
            print('Error! Please enter an amount in numbers.')
    return bet_amount #returning bet amount        

def hit(deck,hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()
    print(f'\n{card} was drawn...\n')


def hit_or_stand(deck,hand): #hit or stand for player
    global playing
    while True:
        playerChoice = input('Please input 1 for HIT and 2 for STAND: ')
        if playerChoice == '1':
            hit(deck,hand)
            print(f'Your current score is: {hand.value}\n')
            if hand.value>21:
                break
        elif playerChoice == '2':
            playing = False
            break
        else:
            print("You have entered an invalid choice, please only enter 1 or 2.")
    
def show_some(player,dealer): #showing cards
    container = "Your cards are: | "
    for card in player.cards:
        container +=f'{str(card)} | ' 

    print(container)
    print(f'Your current score is: {player.value}\n')
    container = "The dealer's cards are: | "
    
    container +=str(f'Hidden | {dealer.cards[1]} |\n')

    print(container)
        
def show_all(player,dealer):

    container = "Your cards are: | "
    for card in player.cards:
        container +=f'{str(card)} | ' 

    print(f'{container} \nValue: {player.value}\n')
    container = "The dealer's cards are: | "

    for card in dealer.cards:
            container +=f'{str(card)} | ' 
    print(f'{container} \nValue: {dealer.value}\n')

def player_busts(chips): # end game scenarious        
    
    chips.lose_bet()
    print( "The player has busted. The dealer wins.")
        
def player_wins(chips):
    
    chips.win_bet()
    print("The player has won. The dealer loses.")
        
def dealer_busts(chips):

    chips.win_bet()
    print("The dealer has busted. The player wins.")
           
def dealer_wins(chips): #end game scenarious
    
    chips.lose_bet()
    print("The dealer has won. The player loses.")
    
def push(chips):
    
    chips.bet = 0
    print("There's a push. Nobody loses.")
        
      

# Set up the Player's chips (outside of while loop)
playerChips = Chips()

while True:
    # Print an opening statement
    print("Welcome to the game of BlackJack. The game now begins")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    deck.shuffle()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    player_hand.adjust_for_ace()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.adjust_for_ace()
   
    
    
    # Prompt the Player for their bet
    if playerChips.total != 0:
        playerChips.bet = take_bet(playerChips.total)
    else:
        print('You do not have any funds so you are playing in fun mode. Your games will not win any amount. Please deposit to play with real money\n')

    
    
    
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        
        clear_output()
        show_some(player_hand,dealer_hand)
            
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(playerChips)
            break
        

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        print("It's the dealer's turn to draw now: \n")
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if player_hand.value > dealer_hand.value:
            player_wins(playerChips)
            break
        elif dealer_hand.value > 21:
            dealer_busts(playerChips)
            break
        elif dealer_hand.value > player_hand.value:
            dealer_wins(playerChips)
            break
        elif dealer_hand.value == player_hand.value:
            push(playerChips)
            break
    

    
    # Inform Player of their chips total 
    print(f'Your current balance is: {playerChips.total}')

    # Ask to play again #break
    continue_game = input("Please confirm if you would like to continue playing. Y for YES and and any other key for NO ")
    if continue_game.upper() == 'Y':
        clear_output()
        playing = True
        continue    
    else:
        break
    

   