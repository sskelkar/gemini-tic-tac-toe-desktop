from enum import Enum

class Player(Enum):
    """Represents the players in the Tic Tac Toe game."""
    X = "X"
    O = "O"

    @property
    def opponent(self) -> 'Player':
        """Returns the opposing player."""
        return Player.O if self.value == Player.X.value else Player.X
