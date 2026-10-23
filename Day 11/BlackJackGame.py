import random

# TO-DO: add a print of logo

#DRAW A CARD
listOfCards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'Ace'] * 4
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
    for card in hand:
        if card == 'Ace':
            score += 11
            # list['Ace']=11
            if score > 21:
                score-=10
                # list['Ace'] = 1
        else:
            score += card
    return score

#BLACKJACK ITSELF
def BlackJackGame():
    #print logo here

    #first two draws of cards
    #return 2 lists
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(takeCard(listOfCards))
        dealer_hand.append(takeCard(listOfCards))

    #tell how many Aces have been drawn
    # aceCount = 0
    # isAce = False #will use this in every count check
    # for card in player_hand+dealer_hand:
    #     if card == 'Ace':
    #         isAce = True
    #         aceCount += 1

    while True:
        pScore = scoreCount(player_hand)
        dScore = scoreCount(dealer_hand)
        print(f"Your hand: {player_hand}, current score: {pScore}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        while True:
            if pScore > 21:
                print("You lose!")
                return
            anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
            if anotherCard == 'y':
                #taking out another card
                player_hand.append(takeCard(listOfCards))
                pScore = scoreCount(player_hand)
            if anotherCard == 'n':
                break

        #FINAL COUNT
        while dScore < 17:
            dealer_hand.append(takeCard(listOfCards))
            dScore = scoreCount(dealer_hand)
        if dScore > pScore:
            print("You lose!")
            print(f"Dealer's hand: {dealer_hand}, count: {dScore}")
            return
        elif dScore == pScore:
            print("Draw!")
            print(f"Dealer's hand: {dealer_hand}, count: {dScore}")
            return
        else:
            print("You win!")
            print(f"Dealer's hand: {dealer_hand}, count: {dScore}")
            return

wantToPlay = ""
while wantToPlay != 'y' and wantToPlay != 'n':
    wantToPlay = input("Do you want to play a game of 'BlackJack'? Type 'y' or 'n': ")

if wantToPlay == 'y':
    BlackJackGame()