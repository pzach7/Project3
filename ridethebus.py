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

#Adjust the current number of face cards and non-face cards in the deck
def adjustCards(X):
    global numFaces
    global numReg
    if X > 38 and numFaces < MAX_FACES:
        numFaces = numFaces + 1
    else:
        numReg = numReg + 1

#Takes in user input, and checks if the card they drew was a face card
#If so, end the game, otherwise, advance to the next row

#For 2 cards in a row
def guessLine2():
    guess = int(input("Enter a number: "))
    X1 = random.randint(0+numReg,53-numFaces)
    adjustCards(X1)
    X2 = random.randint(0+numReg,53-numFaces)
    adjustCards(X2)
    if guess == 1 and X1 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()
    elif guess == 2 and X2 > 38:
        print "You picked a face card, better luck next time"
        sys.exit()
    else:
        print "You advanced to the next row!"

#For 3 cards in a row
def guessLine3():
    guess = int(input("Enter a number: "))
    X1 = random.randint(0+numReg,53-numFaces)
    adjustCards(X1)
    X2 = random.randint(0+numReg,53-numFaces)
    adjustCards(X2)
    X3 = random.randint(0+numReg,53-numFaces)
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
    else:
        print "You advanced to the next row!" 
 
#For 4 cards in a row
def guessLine4():
    guess = int(input("Enter a number: "))
    X1 = random.randint(0+numReg,53-numFaces)
    adjustCards(X1)
    X2 = random.randint(0+numReg,53-numFaces)
    adjustCards(X2)
    X3 = random.randint(0+numReg,53-numFaces)
    adjustCards(X3)
    X4 = random.randint(0+numReg,53-numFaces)
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
    else:
        print "You advanced to the next row!" 
       
MAX_FACES = 16 #Maximum number of face cards in a deck
numFaces = 0 #Current number of faces in a deck
numReg = 0 #Maximum number of non-face cards
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

#Main body for the game
print "GAME START:"
print

#First line
print twoXline, "(1)"
print "   1 2"
print
guessLine2()
print

#Second line
print threeXline, "(2)"
print "  1 2 3"
print
guessLine3()
print

#Thirt line
print fourXline, "(3)"
print " 1 2 3 4"
print
guessLine4()
print

#Fourth line
print fourXline, "(4)"
print " 1 2 3 4"
print
guessLine4()
print

#Fifth line
print threeXline, "(5)"
print "  1 2 3"
print
guessLine3()
print

#Sixth line
print twoXline, "(6)"
print "   1 2"
print
guessLine2()

#user won
print "You won!!!!1!!!"
