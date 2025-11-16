import random

# Global variables
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
player_hand = {}
computer_hand = {}
cont = True
def init():
    global player_hand, computer_hand, cont
    player_hand = {
        "hand": [],
        "sum": 0 
    }
    computer_hand = {
        "hand": [],
        "sum": 0
    }
    cont = True

def hand_com(round):
    global player_hand, computer_hand
    print(f"Your {round} hand: {player_hand['hand']}, Total: {player_hand['sum']}.")
    print(f"Opponent's {round} hand: {computer_hand['hand']}, Total: {computer_hand['sum']}")

def add_card(deck):
    deck["hand"].append(random.choice(cards))
    deck["sum"] = sum(deck["hand"])

def game():
    global player_hand, computer_hand, cont
    print(logo)

    for i in range(2):
        add_card(player_hand)
    add_card(computer_hand)

    hand_com("current")

    if player_hand["sum"] == 21:
        print("You win with Blackjack 😃")
        init()
        return


    # TODO - Ask to add more card to user
    while cont:
        more = input("Do you want 1 more card? Type 'y' for yes, 'n' for no: ").lower()
        if more == "y":
            add_card(player_hand)
            if player_hand["sum"] > 21:
                if 11 in player_hand["hand"]:
                    player_hand["hand"].remove(11)
                    player_hand["hand"].append(1)
                    player_hand["sum"] = sum(player_hand["hand"])
                    cont = True
                else:
                    cont = False
                if player_hand["sum"] > 21:
                    print(f"Your new hand: {player_hand['hand']}, Total: {player_hand['sum']}")
                    print("You went over. You lose 😭")
                    init()
                    return
            hand_com("current")
        elif more == "n":
            cont = False
        else:
            print("Invalid input, please use 'y' or 'n'. ")

    while computer_hand["sum"] < 17:
        add_card(computer_hand)

    # TODO - Player sum not more 21
    if computer_hand["sum"] > 21:
        hand_com("final")
        print("Opponent went over. You win. 😃")
    # TODO - Decide winner by compare
    elif computer_hand["sum"] > player_hand["sum"]:
        hand_com("final")
        print("You lose 😤")
    elif computer_hand["sum"] == player_hand["sum"]:
        hand_com("final")
        print("Draw 🙃")
    elif computer_hand["sum"] < player_hand["sum"]:
        hand_com("final")
        print("You win 😃")
    
    init()

def main():
    play = True
    while play:
        play = input("Do you want to play Blackjack? Type 'y' or 'n': ").lower()
        if play == "y":
            init()
            play = True
            game()
        elif play == "n":
            play = False
            print("The program exits. Thank you.")
        else:
            print("Wrong input. Try again.")

if __name__ == "__main__":
    main()