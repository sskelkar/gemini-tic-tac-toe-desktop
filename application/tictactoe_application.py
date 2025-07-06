from typing import List, Optional
from domain.game import Game
from domain.player import Player

class TicTacToeApplication:
    """The Application layer orchestrates the domain objects to fulfill use cases."""
    def __init__(self):
        """Initializes the TicTacToeApplication with a new game instance."""
        self.game: Game = Game()

    def make_move(self, index: int) -> bool:
        """Attempts to make a move in the game.

        Args:
            index: The index of the cell where the move is to be made.

        Returns:
            True if the move was successful, False otherwise.
        """
        return self.game.make_move(index)

    def get_board_state(self) -> List[Optional[Player]]:
        """Returns the current state of the game board."""
        return self.game.get_board_state()

    def get_current_player(self) -> Player:
        """Returns the player whose turn it is."""
        return self.game.get_current_player()

    def is_game_over(self) -> bool:
        """Checks if the game has ended."""
        return self.game.is_game_over()

    def get_winner(self) -> Optional[Player]:
        """Returns the winning player if the game is over and there's a winner, otherwise None."""
        return self.game.get_winner()

    def reset_game(self):
        """Resets the game to its initial state."""
        self.game.reset_game()

    def get_available_moves(self) -> List[int]:
        """Returns a list of available moves (empty cell indices) on the board."""
        return self.game.get_available_moves()

    def get_human_player(self) -> Player:
        """Returns the player designated as the human player (X)."""
        return Player.X

    def get_computer_player(self) -> Player:
        """Returns the player designated as the computer player (O)."""
        return Player.O
