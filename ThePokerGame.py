# import the random number generator
# this is needed to shuffle the cards into a random order

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank, suit):
    # each Card object consists of two attributes: a rank
    #    and a suit
    self.rank = rank
    self.suit = suit
    
  def __str__ (self):
    # print J, Q, K, A instead of 11, 12, 13, 14
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  # you'll find the following methods to be useful:  they 
  #    allow you to compare Card objects

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)


class Deck (object):

  def __init__ (self):
    # self.deck is the actual deck of cards
    # create it by looping through all SUITS and RANKS
    #    and appending them to a list
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    # the shuffle method in the random package reorders
    #    the contents of a list into random order
    random.shuffle (self.deck)

  def deal (self):
    # if the deck is empty, fail:  otherwise pop one
    #    card off and return it
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)
      
class Poker (object):
  #
  # when you create an object of class Poker, you
  #    create a deck, shuffle it, and deal cards
  #    out to the players.
  #
  def __init__ (self, numHands):
    self.deck = Deck()              # create a deck
    self.deck.shuffle()             # shuffle it
    self.hands = []
    numCards_in_Hand = 5

    for i in range (numHands):
      # deal out 5-card hands to numHands players
      # you'd actually get shot if you dealt this
      #    way in a real poker game (5 cards to
      #    the first player, 5 to the next, etc.)
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal())
      self.hands.append (hand)

  def play (self):
    result = []

    for i in range (len(self.hands)):
      # the method "sorted" returns a sorted list without
      #   altering the original list.  reverse = True
      #   makes it sort in decreasing order
      sortedHand = sorted (self.hands[i], reverse = True)
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + ' '
      print ('Hand ' + str(i + 1) + ': ' + hand)
    for i in range (len(self.hands)):
      sortedHand = sorted (self.hands[i], reverse = True)
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + ' '
      if self.is_royal(sortedHand) != False:
         result.append(self.is_royal(sortedHand))
         print ('Hand ' + str(i + 1) + ': ' + "Royal Flush")
      elif self.is_straight_flush(sortedHand) != False:
        result.append(self.is_straight_flush(sortedHand))
        print ('Hand ' + str(i + 1) + ': ' + "Straight Flush")
      elif self.is_four(sortedHand) != False:
         result.append(self.is_four(sortedHand))
         print ('Hand ' + str(i + 1) + ': ' + "Four of a Kind")
      elif self.is_full(sortedHand) != False:
         result.append(self.is_full(sortedHand))
         print ('Hand ' + str(i + 1) + ': ' + "Full House")
      elif self.is_flush(sortedHand) != False:
         result.append(self.is_flush(sortedHand))
         print ('Hand ' + str(i + 1) + ': ' + "Flush")
      elif self.is_straight(sortedHand) != False:
         result.append(self.is_straigh(sortedHand))
         print ('Hand ' + str(i + 1) + ': ' + "Straight")
      elif self.is_three(sortedHand) != False:
         result.append(self.is_three(sortedHand))
         print ('Hand ' + str(i + 1) + ': ' + "Three of a Kind")
      elif self.is_two(sortedHand) != False:
         result.append(self.is_two(sortedHand))
         print ('Hand ' + str(i + 1) + ': ' + "Two Pairs")
      elif self.is_one(sortedHand) != False:
         result.append(self.is_one(sortedHand))
         print ('Hand ' + str(i + 1) + ': ' + "One Pair")
      else:
         result.append(self.is_high(sortedHand))
         print ('Hand ' + str(i + 1) + ': ' + "High Card")
    winner = 0
    winningpoints = 0
    tiecounter = 0
    for i in range(len(result)):
      if result[i] > winningpoints:
        winningpoints = result[i]
        winner = i
      elif result[i] == winningpoints:
        tiecounter += 1
    if tiecounter == 0:
      print ("Hand" + " " + str(winner + 1) + " " + "wins.")
    else:
       for i in range(tiecounter):
         winner = result.index(winningpoints)
         print("Hand" + " " + str(winner + 1) + " " + "ties.")
         result.remove(winningpoints)
      
  def is_royal (self, hand):
    c1 = hand[0].rank
    c2 = hand[1].rank
    c3 = hand[2].rank
    c4 = hand[3].rank
    c5 = hand[4].rank  
    total = 10 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5

    counter = 0
    if hand[0].rank == 14 and hand[1].rank == 13 and  hand[2].rank == 12 and  hand[3].rank == 11 and  hand[4].rank == 10:
      counter += 1
    if  hand[0].suit == hand[1].suit ==  hand[2].suit ==  hand[3].suit ==  hand[4].suit:
      counter += 1
    if counter == 2:
      return(total)
    else:
      return(False)
  def is_straight_flush (self, hand):
    c1 = hand[0].rank
    c2 = hand[1].rank
    c3 = hand[2].rank
    c4 = hand[3].rank
    c5 = hand[4].rank 
    total = 9 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
    counter = 0
    if hand[0].rank == hand[1].rank + 1 and hand[1].rank ==  hand[2].rank + 1 and  hand[2].rank == hand[3].rank +1 and hand[3].rank == hand[4].rank + 1:
      counter += 1
    if  hand[0].suit == hand[1].suit ==  hand[2].suit ==  hand[3].suit ==  hand[4].suit:
      counter += 1
    if counter == 2:
      return(total)
    else:
      return(0)

  def is_four (self, hand):
    if hand[0] == hand[1] and hand[1] == hand[2] and hand[2] == hand[3]:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank 
      total = 8 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    elif hand[1] == hand[2] and hand[2] == hand[3] and hand[3] == hand[4]:
      c1 = hand[1].rank
      c2 = hand[2].rank
      c3 = hand[3].rank
      c4 = hand[4].rank
      c5 = hand[0].rank 
      total = 8 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    else:
      return(0)

  def is_full (self, hand):
    
    if hand[0] == hand[1] and hand[1] == hand[2] and hand[3].rank == hand[4].rank:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank 
      total = 7 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    elif hand[0] == hand[1] and hand[2] == hand[3] and hand[3] == hand[4]:
      c1 = hand[2].rank
      c2 = hand[3].rank
      c3 = hand[4].rank
      c4 = hand[1].rank
      c5 = hand[0].rank 
      total = 7 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    else:
      return(0)
      

  def is_flush (self, hand):
    c1 = hand[0].rank
    c2 = hand[1].rank
    c3 = hand[2].rank
    c4 = hand[3].rank
    c5 = hand[4].rank 
    total = 6 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
    if  hand[0].suit == hand[1].suit ==  hand[2].suit ==  hand[3].suit ==  hand[4].suit:
      return(total)
    else:
      return(0)

  def is_straight (self, hand):
    c1 = hand[0].rank
    c2 = hand[1].rank
    c3 = hand[2].rank
    c4 = hand[3].rank
    c5 = hand[4].rank 
    total = 5 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
    if hand[0].rank == hand[1].rank + 1 and hand[1].rank ==  hand[2].rank + 1 and  hand[2].rank == hand[3].rank +1 and hand[3].rank == hand[4].rank + 1:
      return(5)
    else:
      return(0)

  def is_three (self, hand):
    if hand[0].rank == hand[1].rank and hand[1].rank ==  hand[2].rank:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank 
      total = 4 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    elif hand[1].rank == hand[2].rank and hand[2].rank ==  hand[3].rank:
      c1 = hand[1].rank
      c2 = hand[2].rank
      c3 = hand[3].rank
      if hand[0].rank > hand[4].rank:
        c4 = hand[0].rank
        c5 = hand[4].rank
      else:
        c4 = hand[4].rank
        c5 = hand[0].rank
      total = 4 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    elif hand[2].rank == hand[3].rank and hand[3].rank ==  hand[4].rank:
      c1 = hand[2].rank
      c2 = hand[3].rank
      c3 = hand[4].rank
      if hand[0].rank > hand[1].rank:
        c4 = hand[0].rank
        c5 = hand[1].rank
      else:
        c4 = hand[1].rank
        c5 = hand[0].rank
      total = 4 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    else:
      return(0)

  def is_two (self, hand):
    if hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      total = 3 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    elif hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank:
      c1 = hand[1].rank
      c2 = hand[2].rank
      c3 = hand[3].rank
      c4 = hand[4].rank
      c5 = hand[0].rank
      total = 3 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    elif hand[0].rank == hand[1].rank and hand[3].rank == hand[4].rank:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[3].rank
      c4 = hand[4].rank
      c5 = hand[2].rank
      total = 3 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    else:
      return(0)
  def is_one (self, hand):
    if hand[0].rank == hand[1].rank:
      c1 = hand[0].rank
      c2 = hand[1].rank
      c3 = hand[2].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      total = 2 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    elif hand[1].rank == hand[2].rank:
      c1 = hand[1].rank
      c2 = hand[2].rank
      c3 = hand[0].rank
      c4 = hand[3].rank
      c5 = hand[4].rank
      total = 2 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    elif hand[2].rank == hand[3].rank:
      c1 = hand[2].rank
      c2 = hand[3].rank
      c3 = hand[0].rank
      c4 = hand[1].rank
      c5 = hand[4].rank
      total = 2 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    elif hand[3].rank == hand[4].rank:
      c1 = hand[3].rank
      c2 = hand[4].rank
      c3 = hand[0].rank
      c4 = hand[1].rank
      c5 = hand[2].rank
      total = 2 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
      return(total)
    else:
      return(0)

  def is_high (self, hand):
    c1 = hand[0].rank
    c2 = hand[1].rank
    c3 = hand[2].rank
    c4 = hand[3].rank
    c5 = hand[4].rank
    total = 1 * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
    return(total)


def main():

  numHands = int (input ('Enter number of hands to play: '))

  # need at least 2 players but no more than 6
  while (numHands < 2 or numHands > 6):
    numHands = int (input ('Enter number of hands to play: '))

  # create a Poker object:  create a deck, shuffle it, and
  # deal out the cards
  game = Poker (numHands)

  # play the game
  game.play()

main()
