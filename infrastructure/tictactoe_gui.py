import tkinter as tk
from tkinter import messagebox
from application.tictactoe_application import TicTacToeApplication
from ai.ai_player_service import AIPlayerService
from domain.player import Player
from typing import Optional

class TicTacToeGUI:
    """The GUI for the Tic Tac Toe game, handling user interaction and displaying game state."""
    # --- Constants for styling ---
    FONT_FAMILY: str = "Press Start 2P"
    BG_COLOR: str = "#222222"
    FG_COLOR: str = "#00FF00"
    BOARD_BG_COLOR: str = "#000000"
    BUTTON_BG_COLOR: str = "#000000"
    BUTTON_ACTIVE_BG_COLOR: str = "#333333"
    X_COLOR: str = "#FF0000"
    O_COLOR: str = "#0000FF"
    RESTART_BUTTON_BG: str = "#00FF00"
    RESTART_BUTTON_FG: str = "#222222"
    RESTART_BUTTON_ACTIVE_BG: str = "#00AA00"
    RESTART_BUTTON_ACTIVE_FG: str = "#FFFFFF"
    COMPUTER_MOVE_DELAY_MS: int = 500

    def __init__(self, master: tk.Tk):
        """Initializes the Tic Tac Toe GUI.

        Args:
            master: The Tkinter root window.
        """
        self.master = master
        self.app: TicTacToeApplication = TicTacToeApplication()
        self.ai_service: AIPlayerService = AIPlayerService()
        self._setup_window(master)
        self._create_widgets()
        self._update_status_display()
        self._check_initial_computer_move()

    def _setup_window(self, master: tk.Tk):
        """Configures the main Tkinter window properties."""
        master.title("Retro Tic Tac Toe")
        master.geometry("400x500")
        master.resizable(False, False)
        master.configure(bg=self.BG_COLOR)

    def _create_widgets(self):
        """Creates all the GUI widgets (labels, buttons, etc.)."""
        self._create_title_label()
        self._create_status_label()
        self._create_board_buttons()
        self._create_restart_button()

    def _create_title_label(self):
        """Creates the game title label."""
        self.title_label = tk.Label(self.master, text="Retro Tic Tac Toe", font=(self.FONT_FAMILY, 20), fg=self.FG_COLOR, bg=self.BG_COLOR)
        self.title_label.pack(pady=10)

    def _create_status_label(self):
        """Creates the label to display game status (e.g., current player's turn, win/draw)."""
        self.status_label = tk.Label(self.master, text="", font=(self.FONT_FAMILY, 12), fg=self.FG_COLOR, bg=self.BG_COLOR)
        self.status_label.pack(pady=10)

    def _create_board_buttons(self):
        """Creates the 3x3 grid of buttons for the Tic Tac Toe board."""
        self.board_frame = tk.Frame(self.master, bg=self.BOARD_BG_COLOR, bd=5, relief="sunken")
        self.board_frame.pack(pady=10)

        self.buttons: list[tk.Button] = []
        for i in range(self.app.game.board.BOARD_SIZE):
            button = tk.Button(self.board_frame, text="", font=(self.FONT_FAMILY, 30), width=4, height=2,
                               bg=self.BUTTON_BG_COLOR, fg=self.FG_COLOR, activebackground=self.BUTTON_ACTIVE_BG_COLOR, activeforeground=self.FG_COLOR,
                               command=lambda i=i: self._handle_button_click(i))
            button.grid(row=i // 3, column=i % 3, padx=2, pady=2)
            self.buttons.append(button)

    def _create_restart_button(self):
        """Creates the restart game button."""
        self.restart_button = tk.Button(self.master, text="Restart Game", font=(self.FONT_FAMILY, 12),
                                        bg=self.RESTART_BUTTON_BG, fg=self.RESTART_BUTTON_FG, activebackground=self.RESTART_BUTTON_ACTIVE_BG, activeforeground=self.RESTART_BUTTON_ACTIVE_FG,
                                        command=self._restart_game)
        self.restart_button.pack(pady=20)

    def _handle_button_click(self, index: int):
        """Handles a click event on a board cell button.

        Args:
            index: The index of the clicked cell.
        """
        if self.app.get_current_player() == self.app.get_human_player() and not self.app.is_game_over():
            if self.app.make_move(index):
                self._update_board_display()
                if not self.app.is_game_over():
                    self._update_status_display()
                    self.master.after(self.COMPUTER_MOVE_DELAY_MS, self._computer_turn)
                else:
                    self._show_game_result()

    def _computer_turn(self):
        """Manages the computer's turn, getting a move from the AI service and updating the game state."""
        if not self.app.is_game_over():
            move: Optional[int] = self.ai_service.get_best_move(self.app.game)
            if move is not None:
                self.app.make_move(move)
                self._update_board_display()
                if self.app.is_game_over():
                    self._show_game_result()
                else:
                    self._update_status_display()

    def _update_board_display(self):
        """Updates the text and color of the board buttons based on the current game state."""
        board_state: list[Optional[Player]] = self.app.get_board_state()
        for i, cell_value in enumerate(board_state):
            if cell_value is not None:
                self.buttons[i].config(text=cell_value.value, fg=self.X_COLOR if cell_value == Player.X else self.O_COLOR)
            else:
                self.buttons[i].config(text="", fg=self.FG_COLOR) # Reset color for empty cells

    def _update_status_display(self):
        """Updates the status label to show the current player's turn or game result."""
        if self.app.is_game_over():
            winner: Optional[Player] = self.app.get_winner()
            if winner:
                self.status_label.config(text=f"Player {winner.value} wins!")
            else:
                self.status_label.config(text="It's a Draw!")
        else:
            self.status_label.config(text=f"Player {self.app.get_current_player().value}'s turn")

    def _show_game_result(self):
        """Displays a messagebox with the game result (win or draw)."""
        winner: Optional[Player] = self.app.get_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner.value} wins!")
        else:
            messagebox.showinfo("Game Over", "It's a Draw!")

    def _restart_game(self):
        """Resets the game through the application layer and updates the GUI."""
        self.app.reset_game()
        self._update_board_display()
        self._update_status_display()
        self._check_initial_computer_move()

    def _check_initial_computer_move(self):
        """Checks if the computer is the starting player and initiates its first move if so."""
        if self.app.get_current_player() == self.app.get_computer_player():
            self.master.after(self.COMPUTER_MOVE_DELAY_MS, self._computer_turn)
