import tkinter as tk
from infrastructure.tictactoe_gui import TicTacToeGUI

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = TicTacToeGUI(root)
    root.mainloop()