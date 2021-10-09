from random import shuffle


def rules(action):
    
    input("please enter '--resume' to resume the game")


def createDeck():
    Deck = []

    faceCards = ["A","J","K","Q"]

    for i in range(4): #4 different suits
        for card in range(2,11):
            Deck.append(str(card))
        for card in faceCards:
            Deck.append(card)
    shuffle(Deck)
    return Deck

cardDeck = createDeck()

Name = input("Hello,Please enter your name")




while(True):
    correctGuesses = 0
    wrongGuesses = 0
    invalidInputs = 0

    if len(cardDeck) < 10:
        print("Less than 10 cards remaining in the deck")
        print("To re-Shuffle, and resume: enter 'R'")
        print("Press any other key to exit")
        whatToDo = input().upper
        if whatToDo == "R":
            cardDeck = createDeck()
            continue
        else:
            break
    if correctGuesses == 10:
        print("Yay, you made 10 correct guesses, YOU WIN!!")
        replay = input("Play again? (Y/N:)").upper()
        if replay == "Y":
            continue
        elif replay == "N":
            break
        else:
            print("Invalid input")
            break

    elif wrongGuesses == 10:
        print("oops, you made 10 Incorrect guesses, YOU LOSE :(")
        replay = input("Play again? (Y/N:)").upper()
        if replay == "Y":
            continue
        elif replay == "N":
            break
        else:
            print("Invalid input")
            break
    elif invalidInputs == 5:
        print("oops, you made too many invalid inputs, YOU LOSE :(")
        replay = input("Play again? (Y/N:)").upper()
        if replay == "Y":
            continue
        elif replay == "N":
            break
        else:
            print("Invalid input")
            break

    fCardsDict = {"A": 1, "J": 11, "Q": 12, "K": 13,}

    playerCard = cardDeck.pop()
    print("here's your card:", playerCard)

    nextCard = cardDeck.pop()
    action = input("H/L:").upper()

    if action == "--HELP":
        rules(action)
    if action == "H":
        if nextCard > playerCard:
            print("Yay!, You got that correct.")
            print("The next card was",nextCard)
            correctGuesses += 1
        elif nextCard < playerCard:
            print("Oops!, You got that wrong")
            print("The next card was",nextCard)
            wrongGuesses += 1

    elif action == "L":
        if nextCard < playerCard:
            print("Yay!, You got that correct.")
            print("The next card was:",nextCard)
            correctGuesses += 1
        elif nextCard > playerCard:
            print("Oops!, You got that wrong")
            print("The next card was:",nextCard)
            wrongGuesses += 1

    elif action == "--EXIT":
        break

    else:
        print("Invalid input, Please try Again")
        invalidInputs += 1
        continue