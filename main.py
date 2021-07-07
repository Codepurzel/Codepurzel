#Setting parameters
from replit import clear
from art import logo
import random

#Function to pick random cards from the deck
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Calculating the score & checking for Black Jack
def calculate_score(cards):
  if sum(cards) == 21 in cards and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Checking on who won
def compare(player_score, dealer_score):
  if player_score == dealer_score:
    return "You both have the same points. It's a Draw!"
  elif dealer_score == 0:
    return "Dealer has scored a Black Jack! You lose!"
  elif player_score == 0:
    return "Congratulations, you scored a BlackJack and won the game!"
  elif player_score > 21:
    return "You're above 21 and lose to the dealer!"
  elif dealer_score > 21:
    return "The dealer is above 21. You win!"
  elif player_score > dealer_score:
    return "You scored higher than the dealer. You win!"
  else:
    return "The dealer has got better cards and wins the game! Better luck next time!"

#Function for the whole game
def play_game():
  print(logo)
  player_cards = []
  dealer_cards = []
  game_over = False
  
  #Dealing two cards to player and dealer
  for _ in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

  #While loop allowing the player to get another card
  while not game_over:

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"\nYour current hand shows: {player_cards}, giving you a total of: {player_score}!")

    #Checking on who won
    if player_score == 0 or dealer_score == 0 or player_score > 21:
      game_over = True
    else:
      another_card = input("\nType 'y' to get another card or type 'n' to pass: ")
      if another_card == "y":
        player_cards.append(deal_card())
      else:
        game_over = True

  #While loop to keep the dealer playing
  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

  print(f"\nYour hand is: {player_cards}, giving you a total of {player_score} vs. the dealer's hand: {dealer_cards} sitting on a score of {dealer_score}\n")
  print(compare(player_score, dealer_score))

while input("\nWant to play BlackJack? Type 'y' for Yes and 'n' for No: ") == "y":
  clear()
  play_game()











  

