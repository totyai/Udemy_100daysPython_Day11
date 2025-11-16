import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo =  """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      '------'                           |__/           
"""

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
player_hand = {
    "hand": [],
    "sum": 0 
}
computer_hand = {
    "hand": [],
    "sum": 0
}

player_hand["hand"].append(random.choice(cards))
player_hand["hand"].append(random.choice(cards))
computer_hand["hand"].append(random.choice(cards))
player_hand["sum"] = sum(player_hand["hand"])
computer_hand["sum"] = sum(computer_hand["hand"])

# TODO - Ask to add more card to user

# TODO - Decide winner by compare

# TODO - Lose if hand is more then 21

# TODO - User communications

# TODO - 

print(player_hand, computer_hand)