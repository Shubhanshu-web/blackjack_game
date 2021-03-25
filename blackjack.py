import random
import colorama
import termcolor
from termcolor import colored
colorama.init()
#tuple
suits = ('Club','Diamond','Spade','Heart')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {
    'Two':2,
    'Three':3,
    'Four':4,
    'Five':5, 
    'Six':6,
    'Seven':7,
    'Eight':8,
    'Nine':9,
    'Ten':10,
    'Jack':10,
    'Queen':10,
    'King':10,
    'Ace':11
}

total_chips = 100

#making the card

def card(rank,suit):
    return rank + ' of ' + suit

print(card('Five','Spade'))

#making the deck
def deck_card():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(card(rank,suit))
    return deck

# print(deck_card())
# s = deck_card()
# random.shuffle(s)
# print(s)

def take_bet():
    while True:
       try:
            bet = int(input("How many chips would you like to bet?"))
       except ValueError:
           print("Invalid input. Please provide valid integer")
       else:
            if bet > total_chips:
                print("You don't have enough chips")
            else:
                break 
    return bet

# print(take_bet())

#show some
def showSome():
  print(colored("Player's card",'magenta'))
  for i in player_card:
     print(i,end=',')

  print()
  print()
  print(colored("Dealer's card",'magenta'))
  for i in dealer_card:
    if dealer_card.index(i) == 0:
        print("One card is hidden",end=",")
    else:
        print(i,end=',')

#count player score
def player_count_score():
    global player_score
    player_score = 0
    for i in player_card:
        player_score += values[i.split()[0]]
    if player_score > 21:
        values={'Ace':1}

#count dealer score
def dealer_count_score():
    global dealer_score
    dealer_score = 0
    for i in dealer_card:
        dealer_score += values[i.split()[0]]
    
# print(player_score)

#ask for hit stand
def hit_or_stand():
    global playing
    print(colored("Hit or stand?, press h or s",'magenta'))
    ask = input()
    if ask=='h':
        print("Player choose to hit")
        player_card.append(deck.pop())
        showSome()
    elif ask=='s':
        playing = False



#Game start

print(colored("Welcome to Black Jack",'blue'))
# print(help(termcolor))
bet = take_bet()

playing = True
deck = deck_card()
random.shuffle(deck)

#player' hand
player_card = []
player_score = 0
player_card.append(deck.pop())
player_card.append(deck.pop())


#dealer' hand
dealer_card = []
delaer_score = 0
dealer_card.append(deck.pop())
dealer_card.append(deck.pop())


#show ALL
def showAll():
   print(colored("Player's card",'cyan'))
   for i in player_card:
       print(i,end=',')
    
print()
print()
print(colored("Dealer's card",'cyan'))
for i in dealer_card:
    print(i,end=',')

showSome()

while playing:
    # player_count_score()
    # print(player_score)
    print(playing)
    if (player_score == 21):
        total_chips += bet
        print("Player hit the blackjack")
        break
    elif(player_score>21):
        print("Player burst")
        total_chips -= bet
        break
    elif(total_chips<1):
        print("You Lose the game! You Can go home")
        break
    else:     
        hit_or_stand()
        

print(player_card)
if player_score<21:
    #dealer's turn
    dealer_count_score()
    print(dealer_score)
    showAll()
    while True:
        dealer_count_score()
        if dealer_score<17:
            # print(deck)
            dealer_card.append(deck.pop())
        else:
            break
    showAll()
    if dealer_score == 21:
        total_chips -= bet
        print("Dealer wins")
    elif dealer_score > 21:
        total_chips += bet
        print("Dealer burst, Player wins")
    elif player_score > dealer_score:
        total_chips += bet
        print("Player wins")
    elif dealer_score>player_score:
        total_chips -= bet
        print("Dealer wins")
    else:
        print("Tie")
# print(delaer_score)
print(f"Your total chips is {total_chips} ")