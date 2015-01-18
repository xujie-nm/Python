# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "New deal!"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card_list = []	# create Hand object

    def __str__(self):
        str1 = "Hand has "
        for card in self.card_list:
            str1 += str(card) + " "
        return str1
        # return a string representation of a hand

    def add_card(self, card):
        self.card_list.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        has_Ace = False
        hand_value = 0
        for card in self.card_list:
            if card.get_rank() == 'A':
                has_Ace = True
            hand_value += VALUES[card.get_rank()]
        if has_Ace:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
        else:
            return hand_value
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for card in self.card_list:
            card.draw(canvas, pos)
            pos[0] += 100
        # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_card = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_card.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_card)    # use random.shuffle()

    def deal_card(self):
        return self.deck_card.pop()	# deal a card object from the deck
    
    def __str__(self):
        cards = "the deck contain "
        for card in self.deck_card:
            cards = cards + str(card) + " "
            
        return cards
        # return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, deck1
    deck1 = Deck()
    deck1.shuffle()
    
    dealer = Hand()
    player = Hand()
    
    dealer.add_card(deck1.deal_card())
    player.add_card(deck1.deal_card())
    dealer.add_card(deck1.deal_card())
    player.add_card(deck1.deal_card())
    # your code goes here
    
    in_play = True

def hit():
    global outcome, in_play, dealer, player, deck1
    
    if in_play:
        if dealer.get_value() < 17:
            dealer.add_card(deck1.deal_card())
            player.add_card(deck1.deal_card())
        else:
            player.add_card(deck1.deal_card())
        
        if player.get_value() > 21:
            outcome = "You gonna bust!!!!"
            in_play = False
    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, dealer, player, deck1, score
    while dealer.get_value() < 17:
        dealer.add_card(deck1.deal_card())
        
    if dealer.get_value() < 21 and player.get_value() < 21:
        if dealer.get_value() < player.get_value():
            score += 1
            outcome = "You win!! new deal?"
        else:
            outcome = "You lose!! new deal?"
            score -= 1
    elif dealer.get_value() > 21 and player.get_value() < 21:
        score += 1
        outcome = "You win!! new deal?"
    else:
        score -= 1
        outcome = "You lose!! new deal?"
        
    in_play = False
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', (50, 110), 70, 'Black')
    canvas.draw_text(outcome, (100, 150), 20, 'Blue')
    canvas.draw_text( "score " + str(score), (450, 50), 30, 'White')
    canvas.draw_text('Dealer:', (70, 250), 30, 'Red')
    canvas.draw_text('Player:', (70, 550), 30, 'Red')
    
    dealer_pos = [100, 300]
    player_pos = [100, 400]
    if not in_play:
        dealer.draw(canvas, dealer_pos)
        player.draw(canvas, player_pos)
    else:
        dealer.draw(canvas, dealer_pos)
        card_back_loc = (CARD_CENTER[0], CARD_CENTER[1])
        canvas.draw_image(card_back, card_back_loc, CARD_BACK_SIZE, [133, 350], CARD_BACK_SIZE)
        player.draw(canvas, player_pos)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric