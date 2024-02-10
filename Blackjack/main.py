import random


def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit':suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = 0
    db = 0
    for card in hand:
        if card['rank'] == 'A':
            db = 1
            score +=11
        elif card['rank'] in ['K','Q','J']:
            score += 10
        else:
            score += int(card['rank'])
    
    while db > 0 and score > 21:
        score -= 10
        db -=1
    
    return score

def display_hand(hand):
    for card in hand:
        print("   " + card['rank'] + " of " + card['suit'])

def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print("\nYour cards:")
        display_hand(player_hand)
        print("Your score: " + str(player_score))

        print("\nDealer's first card")
        print("   " + dealer_hand[0]['rank'] + " of " + dealer_hand[0]['suit'])

        if player_score == 21:
            print("Blackjack! You win.\n")
            break
        if player_score > 21:
            print("Bust! You lost.\n")
            break
        
        action = input("\nType 'hit' to get another card, 'stand' to stop ").lower()
        
        if action == "hit":
            player_hand.append(deck.pop())
        elif action == "stand":
            while dealer_score < 17:
                dealer_hand.append(deck.pop())
                dealer_score = calculate_score(dealer_hand)

            print("\nYour final hand:")
            display_hand(player_hand)
            print("Your final score: " + str(player_score))
            print("\nDealer's final hand:")
            display_hand(dealer_hand)
            print("Dealer's final score: " + str(dealer_score))

            if dealer_score > 21:
                print("Dealer bust! You win.\n")
            elif dealer_score > player_score:
                print("Dealer wins!\n")
            elif dealer_score < player_score:
                print("You win!\n")
            else:
                print("It's a draw\n")
            
            break
        else:
            print("Invalid input.")
    play_again = input("Do you want to play again? (Y/N)").lower()
    if play_again == "y":
        play_blackjack()
    elif play_again == "n":
        print("Goodbye!")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    play_blackjack()
                

