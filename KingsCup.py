import random, sys

print('*************************************************************************************')
print('Welcome to King\'s Cup, also known as the Ring of Fire')
print('')
print('Players will take turns picking cards until all 4 Kings are drawn.')
print('When the last King appears, the person who picked it up must finish the King\'s Cup!')
print('*************************************************************************************')

numCards = 52
numKings = 4
curDeck = list(range(1, 53))
random.shuffle(curDeck)

while numCards > 1 and numKings > 1:
    print('*************************************************************************************')
    print('')
    print('There are currently: %s Kings and %s Cards left in the deck' % (numKings, numCards))
    print('')
    print('Choose your next action (q to Quit vs. any other key to Continue)')
    print('')
    print('*************************************************************************************')
    playerAction = input()
    if playerAction == 'q':
        sys.exit() # Quit the program
    
    print('You chose to pick up a random card ...')

    # TODO: What is that random card?
    cardPicked = curDeck[0]
    cardAction = cardPicked % 13
    print('')
    print('You have drawn: ')
    #TODO: Define card actions and subtract from total number of cards in deck
    if cardAction == 0:
        if numKings > 2:
            print('King: Make a rule or cancel a previous rule. Pour a shot of any beverage into the King\'s Cup!')
            curDeck.pop(0)
            numCards = numCards -1
            numKings = numKings -1
        else:
            print('I\'m so sorry ... You have drawn the Last King. Finish the King\'s Cup (with your mates)!')
            sys.exit()
    elif cardAction == 1:
        print('Ace: Waterfall - Don\'t stop drinking until the person to the left of you finishes!')
        print('Whoever drew the card will start.')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 2:
        print('Two: means YOU drink!')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 3:
        print('Three: is ME!')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 4:
        print('Four: touch the FLOOR! Last person to place both hands on the floor drinks.')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 5:
        print('Five: congratulations GUYS drink.')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 6:
        print('Six: Congratulations CHICKS drink.')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 7:
        print('Seven: touch HEAVEN! Last person to place both hands in the air drinks.')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 8:
        print('Eight: pick a MATE. Choose a drinking buddy for the rest of the game.')
        print('The "mate" will also drink whenever the person who picked up the Eight drinks.')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 9:
        print('Nine: RHYME - Choose a word to rhyme with and go left. There\'s a penality if you lose!')
        curDeck.pop(0)
        numCards = numCards -1
    elif cardAction == 10:
        print('Ten: Categories - Pick a category and the person who cannot think of something related ')
        print('to that word must take a penalty.')
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

print('Congratulations, you have finished the game!')
print('Everyone take a shot!')
