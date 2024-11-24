#Imports
from People_Classes import Player, Dealer

#Declare variables
dealer = Dealer()
table = []  # Array of Player()s

#Declare functions
def gather_players():
#Used at the start of the program to fill the Player array (table)
    while True:
        try:
            user_input = int(input("How many players would you like to add? [int]: "))
            if user_input > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    for i in range(user_input):
        table.append(Player(i))

def end_round():
#A 'round' is one loop around the Player table
#at the end of a round, the game asks if the players want another round or if they want the winner to be revealed
    while True:
        match input("Finish game? 'Yes' or 'No': ").lower():
            case "yes":
                return True
            case "no":
                return False
            case _:
                print("Invalid input. Please type 'Yes' or 'No'.")

def check_win(table, dealer):
#Prints the name of all players with a hand greater than the dealers that are still alive (<=21)
    count_wins = 0
    for player in table:
        if player.get_hand().calculate() > dealer.get_hand().calculate() and player.get_alive() == True:
            print(f"{player.get_name()} beat the dealer!\n")
            count_wins += 1

    print(dealer)
    if count_wins == 0:
        print("\nThe dealer won.")

def print_table(turn=None):  # Default to None
#Prints the table while pointing to whose turn it is
    print()
    for player in table:
        if turn and player.get_player_number() == turn.get_player_number() and player.get_alive() == True:
            print(f"{player.get_hand()}\t<-----")
        elif player.get_alive() == True:
            print(f"{player.get_hand()}")
    print()

def table_length():
#Counts the number of players still alive
    return sum(1 for player in table if player.get_alive() == True)

#Main
game_done = False
print("Welcome to Blackjack")
while not game_done:
    # Reset the game state
    table.clear()
    dealer = Dealer()

    # Start
    gather_players()
    print("\nPlaying game:")

    # Play turns
    done = False
    while not done:
        for player in table:
            print_table(player)
            player.play_round()
            if table_length() == 0:
                done = True

        print_table()  # Final table display after all turns
        done = end_round()

    # Finish
    check_win(table, dealer)

    # Ask to play again
    while True:
        match input("Do you want to play again? 'Yes' or 'No': ").lower():
            case "yes":
                break
            case "no":
                game_done = True
                break
            case _:
                print("Invalid input. Please type 'Yes' or 'No'.")
