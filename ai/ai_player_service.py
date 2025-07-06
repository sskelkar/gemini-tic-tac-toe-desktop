import random
from typing import List, Optional
from domain.board import Board
from domain.player import Player
from domain.game import Game

class AIPlayerService:
    """Provides AI logic for the computer player to determine the best move."""
    def __init__(self):
        """Initializes the AIPlayerService."""
        pass

    def get_best_move(self, game: Game) -> Optional[int]:
        """Determines the best move for the AI player based on the current game state.

        The AI prioritizes:
        1. Winning moves.
        2. Blocking opponent's winning moves.
        3. Taking the center cell.
        4. Taking corner cells.
        5. Taking side cells.
        6. A random available move (fallback).

        Args:
            game: The current Game instance.

        Returns:
            The index of the best move (0-8), or None if no moves are available.
        """
        board_state: List[Optional[Player]] = game.get_board_state()
        computer_player: Player = game.get_current_player()
        human_player: Player = computer_player.opponent
        available_moves: List[int] = game.get_available_moves()

        # 1. Check if computer can win
        for move in available_moves:
            temp_board = Board()
            temp_board.set_state(board_state)
            temp_board.place_mark(move, computer_player)
            if temp_board.check_win(computer_player):
                return move

        # 2. Check if human can win and block
        for move in available_moves:
            temp_board = Board()
            temp_board.set_state(board_state)
            temp_board.place_mark(move, human_player)
            if temp_board.check_win(human_player):
                return move

        # 3. Take center if available
        if 4 in available_moves:
            return 4

        # 4. Take a corner if available
        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for move in corners:
            if move in available_moves:
                return move

        # 5. Take a side if available
        sides = [1, 3, 5, 7]
        random.shuffle(sides)
        for move in sides:
            if move in available_moves:
                return move
        
        # Fallback: make a random move (should not be reached in normal play if available_moves is not empty)
        if available_moves:
            return random.choice(available_moves)
        return None
