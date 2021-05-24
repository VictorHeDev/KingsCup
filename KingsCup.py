import random, sys

print('Welcome to King\'s Cup, also known as the Ring of Fire')
numCards = 52
numKings = 4
# TODO: 52 cards in a deck and shuffle function
curDeck = list(range(1, 53))
random.shuffle(curDeck)

# TODO: While the main (while) loop for the game
while numCards > 1 and numKings > 1:
    print('There are currently: %s Kings and %s Cards left in the deck' % (numKings, numCards))
    #TODO: Obtain player input
    print('Choose your next action (q to Quit vs. any other key to Continue)')
    playerAction = input()
    if playerAction == 'q':
        sys.exit() # Quit the program
    
    print('You chose to pick up a random card ...')

    # TODO: What is that random card?
    cardPicked = curDeck[0]
    cardAction = cardPicked % 13
    print('You have drawn: ')
    #TODO: Define card actions and subtract from total number of cards in deck
    if cardAction == 0:
        if numKings > 2:
            print('King: Make a rule or cancel a previous rule. Pour a shot of any beverage into the King\'s Cup!')
            curDeck.pop(0)
            numCards = numCards -1
            numKings = numKings -1
        else:
            print('So sorry ... You have drawn the Last King. Finish the King\'s Cup!')
            sys.exit()
    elif cardAction == 1:
        print('Ace: Waterfall - Don\'t stop drinking until the person to the left of you finishes!')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 2:
        print('Two: means you drink!')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 3:
        print('Three: is me!')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 4:
        print('Four: touch the floor! Last one to place both hands on the floor drinks.')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 5:
        print('Five: is guys')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 6:
        print('Six: is chicks')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 7:
        print('Seven: Heaven! Last one to place both hands in the air drinks.')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 8:
        print('Eight: is Mate. Choose a drinking buddy for the rest of the game.')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 9:
        print('Nine: Rhyme - Choose a word to rhyme with and go left. There\'s a penality if you lose!')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 10:
        print('Ten: Categories')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 11:
        print('Jack: "Never have I ever ..."')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 12:
        print('Queen: Question Master - There\'s a penaltiy if you respond to the QM!')
        curDeck.pop(0)
        numCards = numCards -1

# TODO: Zero cards left
print('Congratulations, you have finished the game! Everyone take a shot!')