## card_deck module

`python3 -m pip install card_deck`

#### Example Code
```python
from card_deck import *

# Create a "card deck" object
d = Deck()

#Shuffle the deck
d.shuffle()

#Deal 5 cards to 2 players
hands = d.deal(2, 5)

p1hand = hands[0] # assigns the first five card hand to a player
p2hand = hands[1] # assigns the second five card hand to a player
pond = d          # remaining cards in the pile
```

#### Object Classes and their Methods
https://card-deck.readthedocs.io/en/latest/autodoc.html#module-model

```
d object
<class 'card_deck.model.Deck'>




p1hand object
<class 'card_deck.model.Pile'>

append(card) method of card_deck.model.Pile instance
    Append the card to the Pile

clear() method of card_deck.model.Pile instance
    Empty the contents of the Pile

count(card) method of card_deck.model.Pile instance
    Count the number of instances of a card in the Pile

empty() method of card_deck.model.Pile instance
    Return whether the pile is empty

extend(other) method of card_deck.model.Pile instance
    Extend the pile contents by another pile

insert(card, position=None) method of card_deck.model.Pile instance
    Place a card into the pile, by default to the top, or at a specified
    position in the pile

peek(position=-1) method of card_deck.model.Pile instance
    Peek at the value of a card in the pile, by default the top card, or
    at a specified position in the pile

pop() method of card_deck.model.Pile instance
    Pop a card off the top of the pile

remove(card) method of card_deck.model.Pile instance
    Remove a card from the Pile

reverse() method of card_deck.model.Pile instance
    Reverse the order of the Pile

shuffle() method of card_deck.model.Pile instance
    Randomly shuffle the order of the cards in the pile

size() method of card_deck.model.Pile instance
    Return the number of cards in the pile

sort() method of card_deck.model.Pile instance
    Sort the pile of cards in the total ordering of the cards




p1hand[0]
<class 'card_deck.model.Card'>
# specific card from a hand or deck

get_from_typeable_name(typeable_name)
    Return the Card object specified by the typeable name. If the name
    does not reference a valid card, return None
    
    The first character of this string represents the face, as either the
    first letter of the face name if it is a picture card, or the number
    of the face if it is not. The second character of this string reprsents
    the suit, as the first letter of the suit name.
    For example, the ace of hearts would be 'AH', whereas the five of clubs
    would be '5C'

get_face_from_typeable_name(typeable_name)
    Return the Face enum specified by the typeable name

get_typeable_name() method of card_deck.model.Card instance
    Get the typeable name of the card, i.e. a unique string to describe
    a card's value
```


### GO FISH introductory code

```python
#!/usr/bin/env python3
""" TO DO: how to group cards by face values into "books"- groups of
four matching cards- and tallying how many books a player has to
determine the winner """

from card_deck import *

from card_deck import *

# Create a "card deck" object
d = Deck()

#Shuffle the deck
d.shuffle()

#Deal 5 cards to 2 players
hands = d.deal(2, 5)

p1hand = hands[0] # assigns the first five card hand to a player
p2hand = hands[1] # assigns the second five card hand to a player
pond = d          # remaining cards in the pile

while True:
    guess= input(">")
    # for testing purposes, we'll let player 2 ask for as many cards as they want
    # until we type "stop"
    if guess == "stop":
        break
    found= False

    # loop over all card objects in p1hand to check if they have the card(s) we asked for
    for card in p1hand:
        # return the card as a string so its easier to check
        cardvalue= card.get_typeable_name()

        # we will check if the value of "guess" (for example, "2","K","A", etc.) 
        # is in the name of the "cardvalue" variable (for example, "2D","KC")
        # NOTE: "2D" is two of diamonds, "KC" is king of clubs, etc.

        if guess in cardvalue:
            print(card)         # announce what card is a match (printing card and not cardvalue shows the lil card emoji)
            found= True         # set a boolean as a flag that a match was made
            p2hand.append(card) # add that matching card to player 2's hand
            p1hand.remove(card) # remove that card from player 1's hand
                                # all of this will repeat over all other cards in player 1's hand

    # if found == False (no matches)
    if not found:
        # announce that the other player can pound sand
        print("Go fish, sucka!")

        # grab a card from the "pond" variable
        new_card= pond.pop()   # this grabs the first card in the deck

        # add that new card to player 2's hand
        p2hand.append(new_card)

# debug output displaying all cards in both players' hands and in the remaining deck
print("Player 1's hand:", p1hand)
print("Player 2's hand:", p2hand)
print("Remaining deck:", pond)
```
