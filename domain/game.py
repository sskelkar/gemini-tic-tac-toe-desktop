import random
from typing import Optional
from domain.board import Board
from domain.player import Player

class Game:
    """Manages the overall Tic Tac Toe game flow, players, turns, and win/draw conditions."""
    def __init__(self):
        """Initializes a new game with an empty board and a randomly chosen starting player."""
        self.board: Board = Board()
        self.current_player: Player = random.choice([Player.X, Player.O])
        self.game_over: bool = False
        self.winner: Optional[Player] = None

    def make_move(self, index: int) -> bool:
        """Attempts to make a move on the board for the current player.

        Args:
            index: The index of the cell where the move is to be made.

        Returns:
            True if the move was successful, False otherwise (e.g., game over, cell occupied).
        """
        if self.game_over or not self.board.is_empty(index):
            return False

        self.board.place_mark(index, self.current_player)
        
        if self.board.check_win(self.current_player):
            self.winner = self.current_player
            self.game_over = True
        elif self.board.is_full():
            self.game_over = True
        else:
            self._switch_player()
        return True

    def _switch_player(self):
        """Switches the current player to the opponent."""
        self.current_player = self.current_player.opponent

    def reset_game(self):
        """Resets the game to its initial state, clearing the board and choosing a new starting player."""
        self.board.reset()
        self.current_player = random.choice([Player.X, Player.O])
        self.game_over = False
        self.winner = None

    def get_board_state(self) -> list[Optional[Player]]:
        """Returns the current state of the game board."""
        return self.board.get_state()

    def get_current_player(self) -> Player:
        """Returns the player whose turn it is."""
        return self.current_player

    def is_game_over(self) -> bool:
        """Checks if the game has ended (either by win or draw)."""
        return self.game_over

    def get_winner(self) -> Optional[Player]:
        """Returns the winning player if the game is over and there's a winner, otherwise None."""
        return self.winner

    def get_available_moves(self) -> list[int]:
        """Returns a list of available moves (empty cell indices) on the board."""
        return self.board.get_available_moves()