
# card 2 attributes
# rank    2-10 J K Q A
# suit    H C S D

import random

def card_generator():
    #generate a number between 1 and 13 to correspond to rank
    card_num = (random.randint(1,13))
    #randomply pair that number with a suit option
    suit = ['H', 'C', 'S', 'D']
    random_suit = random.randint(0,3)
    card_suit = suit[random_suit]
    #return number-suit combination
    return [card_num, card_suit]

print(card_generator())

def number_of_cards_generator(N):
    #how many times we will run the loop
    counter = N
    #store generated cards in list
    hand_of_cards = []
    while counter > 0:
        new_card = card_generator()
        hand_of_cards.append(new_card)
        counter -= 1
    #return full hand of cards back
    return hand_of_cards

# cards = [card_generator() for i in range(1, 5)]
        
# test by generating 5 cards
print(number_of_cards_generator(5))

# flush [[5, 'S'], [9, 'S'], [10, 'S'], [13, 'S'], [6, 'S']]
# not flush [[5, 'S'], [9, 'D'], [10, 'S'], [13, 'S'], [6, 'S']]

test_of_flush = [[5, 'S'], [9, 'S'], [10, 'S'], [13, 'S'], [6, 'S']]
test_not_flush = [[5, 'S'], [9, 'D'], [10, 'S'], [13, 'S'], [6, 'S']]

# is(has)_flush for functions that return boolean
def check_flush(list_of_cards):
    #get all suits in the list of lists
    suits_in_hand = []
    for elem in list_of_cards:
        suit = elem[1]
        suits_in_hand.append(suit)
    # suits_in_hand = [elem[1] for elem in list_of_cards]

    #set it
    suits_in_hand_unique = set(suits_in_hand)
    # if len(suits_in_hand_unique) == 1:
    #     return True
    # #otherwise: return False
    # else:
    #     return False
    return len(suits_in_hand_unique) == 1

print(check_flush(test_of_flush))
print(check_flush(test_not_flush))

def main():
  # call all functions here
  pass