#Imports
from abc import ABC, abstractmethod
from Hand_Classes import Hand

#Classes
class Person(ABC):
    @abstractmethod
    def hit(self):
        pass

    @abstractmethod
    def stand(self):
        pass

    @abstractmethod
    def set_hand(self):
        pass

    @abstractmethod
    def get_hand(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

class Dealer(Person):
    def __init__(self):
        self.hand = Hand()
    
    def hit(self):
        self.hand.add(self)

    def stand(self):
        pass

    def set_hand(self):
        for card in self.hand:
            card.check_rank()
            if card.get_value() == 1:
                card.set_value(11)

    def get_hand(self):
        return self.hand

    def get_type(self):
        return "Dealer"

    def __str__(self):
        return str(self.hand)

class Player(Person):
    def __init__(self, player_number):
        self.hand = Hand()
        self.player_number = player_number
        self.name = f"Player {self.player_number + 1}"
        self.alive = True
        self.set_hand()

    def play_round(self):
        while True:
            user_input = input("What would you like to do?\n'Hit' or 'Stand': ").lower()
            match user_input:
                case "hit":
                    self.hit()
                    if self.hand.calculate() > 21:
                        print(f"\nGAME OVER for {self.name}\n")
                        self.alive = False
                    return "Hit"
                case "stand":
                    self.stand()
                    return "Stand"
                case _:
                    print("Invalid input. Must be 'Hit' or 'Stand'.")

    def hit(self):
        self.hand.add(self)

    def stand(self):
        pass

    def set_hand(self):
        for card in self.hand:
            card.check_rank()
        for card in self.hand:
            card.check_ace(self)

    def get_hand(self):
        return self.hand

    def get_alive(self):
        return self.alive

    def get_type(self):
        return "Player"

    def __str__(self):
        return str(self.hand)
