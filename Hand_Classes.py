#Imports
import random

#Classes
class Card:
    #Constructor
    def __init__(self):
        self.value = random.randint(1, 13)

    #Methods
    def check_rank(self):
        if self.value > 10:
            self.value = 10
        
    def check_ace(self, person):
        if person.get_type() == "Player" and self.value == 1:
        #if the person is a player and the card is a 1
        #ask the player
            done = False
            while not done:
                print(person.get_hand())
                user_input = input(f"Player {person.get_name()} got an ace! Would you like for it to be a 1 or 11?: ")
                match user_input:
                    case "1":
                        done = True
                        self.set_value(1)
                    case "11":
                        done = True
                        self.set_value(11)
                    case _:
                        print("Invalid. Must be 1 or 11: ")
        elif person.get_type() == "Dealer" and self.value == 1:
            self.value = 11

    #Utility
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Hand:
    #Constructor
    def __init__(self):
        self.cards = [Card(), Card()]

    #Methods
    def calculate(self):
        return sum(card.get_value() for card in self)

    def add(self, person):
        card = Card()
        card.check_rank()
        card.check_ace(person)
        self.cards.append(card)

    #Utility
    def __iter__(self):
        return iter(self.cards)
    
    def __str__(self):
        return " ".join(str(card) for card in self.cards)
