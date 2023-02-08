from abc import ABC


class Game(ABC):
    def __init__(self, number_of_players) -> None:
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self):
        self.start()
        while not self.have_winner():
            self.take_turn()
        print(f"Player {self.winning_player()} wins")

    def start(self) -> None:
        pass

    def have_winner(self) -> bool:
        pass

    def take_turn(self) -> None:
        pass

    def winning_player(self) -> int:
        pass
