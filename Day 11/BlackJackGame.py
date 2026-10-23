import random

# TO-DO: add a print of logo

#DECK OF CARDS
def newDeck():
    """
    returns new deck of cards (full)
    """
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'Ace'] * 4

#DRAW A CARD
def takeCard(deck):
    """
    contains full list of possible cards
    draws any card randomly
    :return: randomly drawn card
    """
    randomCard = random.choice(deck)
    deck.remove(randomCard)
    return randomCard

#COUNT SCORE
def scoreCount(hand):
    score = 0
    aceCount = 0
    for card in hand:
        if card == 'Ace':
            score += 11
            aceCount += 1
        else:
            score += card
    while score > 21 and aceCount > 0:
        score -= 10
        aceCount -= 1

    return score

#BLACKJACK ITSELF
def BlackJackGame():
    #print logo here

    #GET A DECK OF CARDS
    deck = newDeck() #if a player wants to play a new game, it will start over

    #FIRST TWO DRAWS OF CARDS
    #returns 2 lists
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(takeCard(deck))
        dealer_hand.append(takeCard(deck))

    while True:
        #no need for dealers score for now
        pScore = scoreCount(player_hand)
        print(f"Your hand: {player_hand}, current score: {pScore}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if pScore > 21:
            print("You went over 21, you lose!")
            return

        anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
        if anotherCard == 'y':
            #taking out another card
            player_hand.append(takeCard(deck))
        if anotherCard == 'n':
            break

        #DEALERS TURN
    dScore = scoreCount(dealer_hand)
    while dScore < 17:
        dealer_hand.append(takeCard(deck))
        dScore = scoreCount(dealer_hand)

        # FINAL COUNT
    if dScore > 21 and pScore > 21:
        print(f"Dealer's hand: {dealer_hand}, count: {dScore}")
        print("You lose!")
        print("==========================================================")
    elif dScore > pScore:
        print(f"Dealer's hand: {dealer_hand}, count: {dScore}")
        print("You lose!")
        print("==========================================================")
    elif dScore == pScore:
        print(f"Dealer's hand: {dealer_hand}, count: {dScore}")
        print("Draw!")
        print("==========================================================")
    else:
        print(f"Dealer's hand: {dealer_hand}, count: {dScore}")
        print("You win!")
        print("==========================================================")

wantToPlay = ""
while wantToPlay != 'n':
    wantToPlay = input("Do you want to play a game of 'BlackJack'? Type 'y' or 'n': ")
    if wantToPlay == 'y':
        BlackJackGame()