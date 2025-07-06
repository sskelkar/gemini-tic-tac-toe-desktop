from typing import List, Optional, Tuple
from domain.player import Player

class Board:
    """Represents the Tic Tac Toe game board and its state."""
    WIN_CONDITIONS: List[Tuple[int, int, int]] = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    BOARD_SIZE: int = 9

    def __init__(self):
        """Initializes an empty Tic Tac Toe board."""
        self._cells: List[Optional[Player]] = [None] * self.BOARD_SIZE

    def get_cell(self, index: int) -> Optional[Player]:
        """Returns the player occupying the cell at the given index, or None if empty."""
        return self._cells[index]

    def is_empty(self, index: int) -> bool:
        """Checks if the cell at the given index is empty."""
        return self._cells[index] is None

    def place_mark(self, index: int, player: Player):
        """Places a player's mark on the board at the specified index.

        Args:
            index: The index of the cell (0-8).
            player: The Player (X or O) to place.

        Raises:
            ValueError: If the cell is already occupied.
        """
        if not self.is_empty(index):
            raise ValueError("Cell is already occupied")
        self._cells[index] = player

    def check_win(self, player: Player) -> bool:
        """Checks if the given player has won the game."""
        for condition in self.WIN_CONDITIONS:
            if all(self._cells[i] == player for i in condition):
                return True
        return False

    def is_full(self) -> bool:
        """Checks if the board is completely filled."""
        return all(cell is not None for cell in self._cells)

    def get_available_moves(self) -> List[int]:
        """Returns a list of indices of empty cells."""
        return [i for i, cell in enumerate(self._cells) if cell is None]

    def reset(self):
        """Resets the board to an empty state."""
        self._cells = [None] * self.BOARD_SIZE

    def get_state(self) -> List[Optional[Player]]:
        """Returns the current state of the board (list of cells)."""
        return self._cells

    def set_state(self, state: List[Optional[Player]]):
        """Sets the state of the board from a given list of cells.

        Args:
            state: A list representing the desired state of the board.

        Raises:
            ValueError: If the provided state list does not match the board size.
        """
        if len(state) != self.BOARD_SIZE:
            raise ValueError(f"Board state must have {self.BOARD_SIZE} cells.")
        self._cells = list(state)
