#todo: import choice function from random module
from random import choice
#todo: ask user do they want to play a game of blackjack? and control based on answers. while loop
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if play_game == "y":
#todo: Create a deal_card() function that uses the List below to return a random card.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #ace will count as 11 until we go over 21
    return choice(cards)

#todo: Create a function called calculate_score() that takes a List of cards as input
# and returns the sum of all the cards in the List as the score. Google the sum() function to help you do this.
def calculate_score():
    user_total_score = sum(user_cards)
    computer_total_score = sum(computer_cards)
    return user_total_score, computer_total_score

print(calculate_score())

# print(deal_card())

#todo: deal 2 cards for user, 1 card for dealer and show boths scores
#store cards in lists for both user and dealer
user_cards = []
computer_cards = []

#deal random cards for both user and comp and store into each list using append
# user_card = deal_card()
# print(user_card)
user_card = user_cards.append(deal_card())
computer_card = computer_cards.append(deal_card())
print(user_card, computer_card)


#todo: ask do they want another card or not? if yes, deal another card to user, none for dealer.
# if no, deal all cards to dealer, while <17 he needs to get more cards.

#todo: compare scores and say who won


#todo:Deal both user and computer a starting hand of 2 random card values.

#todo:Detect when computer or user has a blackjack. (Ace + 10 value card).

#todo:If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).

#todo:Calculate the user's and computer's scores based on their card values.

#todo:If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.

#todo:Reveal computer's first card to the user.

#todo:Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.

#todo:Ask the user if they want to get another card.

#todo:Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.

#todo:Compare user and computer scores and see if it's a win, loss, or draw.

#todo:Print out the player's and computer's final hand and their scores at the end of the game.

#todo:After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start. recursive function?