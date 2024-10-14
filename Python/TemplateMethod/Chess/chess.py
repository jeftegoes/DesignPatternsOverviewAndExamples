from game import Game


class Chess(Game):
    def __init__(self) -> None:
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    # Don't be necessary override
    # def run(self):
    #     return super().run()

    def start(self) -> None:
        print(f"Starting a game of chess with {self.number_of_players}")

    def have_winner(self) -> bool:
        return self.turn == self.max_turns

    def take_turn(self) -> None:
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    def winning_player(self) -> int:
        return self.current_player
