#!/usr/bin/python

import random
import sys

def printBoard():
    print twoXline, "(6)"
    print threeXline, "(5)"
    print fourXline, "(4)"
    print fourXline, "(3)"
    print threeXline, "(2)"
    print twoXline, "(1)"

def adjustCards(X):
    global numFaces
    global numReg
    if X > 38 and numFaces < MAX_FACES:
        numFaces = numFaces + 1
    else:
        numReg = numReg + 1

def guessLine2():
    guess = sys.stdin.readline()
    X1 = random.randrange(0+numReg,53-numFaces)
    adjustCards(X1)
    X2 = random.randrange(0+numReg,53-numFaces)
    adjustCards(X2)
    if guess == 1 and X1 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()
    elif guess == 2 and X2 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()

def guessLine3():
    guess = sys.stdin.readline()
    X1 = random.randrange(0+numReg,53-numFaces)
    adjustCards(X1)
    X2 = random.randrange(0+numReg,53-numFaces)
    adjustCards(X2)
    X3 = random.randrange(0+numReg,53-numFaces)
    adjustCards(X3)
    if guess == 1 and X1 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()
    elif guess == 2 and X2 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()
    elif guess == 3 and X3 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()

def guessLine4():
    guess = sys.stdin.readline()
    X1 = random.randrange(0+numReg,53-numFaces)
    adjustCards(X1)
    X2 = random.randrange(0+numReg,53-numFaces)
    adjustCards(X2)
    X3 = random.randrange(0+numReg,53-numFaces)
    adjustCards(X3)
    X4 = random.randrange(0+numReg,53-numFaces)
    adjustCards(X4)
    if guess == 1 and X1 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()
    elif guess == 2 and X2 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()
    elif guess == 3 and X3 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()
    elif guess == 4 and X4 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()

MAX_FACES = 16
numFaces = 0
numReg = 0
twoXline = "   X X  "
threeXline =  "  X X X " 
fourXline = " X X X X"

#Ride the bus explanation
print "Ride The Bus"
print "Ride The Bus is a card game, with cards laid out as follows"
printBoard()
print "Each X represents a face down card."
print "Users pick a card, starting at row (1)."
print "If the card picked is not a face card,  the user advances to the next row."
print "If a face card (Jack, Queen, King, or Ace), is picked, the game is over"
print "The goal is to get to end of the six rows without drawing a face card."
print "To choose a card, type the number that appears below the card and press enter"

print "GAME START:"
print
print twoXline, "(1)"
print "   1 2"
print
print "Card Guess:"
guessLine2()
print
print threeXline, "(2)"
print "  1 2 3"
print
print "Card Guess:"
guessLine3()
print
print fourXline, "(3)"
print " 1 2 3 4"
print
print "Card Guess:"
guessLine4()
print
print fourXline, "(4)"
print " 1 2 3 4"
print
print "Card Guess:"
guessLine4()
print
print threeXline, "(5)"
print "  1 2 3"
print
print "Card Guess:"
guessLine3()
print
print twoXline, "(6)"
print "   1 2"
print
print "Card Guess:"
guessLine2()
