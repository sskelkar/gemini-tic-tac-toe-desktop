# Retro Tic Tac Toe Desktop Game

This is a simple Tic Tac Toe desktop game built with Python, featuring a retro-themed user interface and an AI opponent.

## Tech Stack

*   **Python**: The core programming language.
*   **Tkinter**: Python's standard GUI (Graphical User Interface) library, used for creating the desktop application.

## Architecture

The project is structured following Domain-Driven Design (DDD) principles to ensure a clear separation of concerns and maintainability:

*   **`domain/`**: Contains the core business logic of the game, including `Board` (game grid and state), `Player` (player definitions), and `Game` (overall game flow, rules, and state management).
*   **`application/`**: Houses the `TicTacToeApplication` class, which acts as an orchestrator between the UI and the domain logic. It defines the application's use cases.
*   **`ai/`**: Contains the `AIPlayerService`, responsible for the computer opponent's move-making logic.
*   **`infrastructure/`**: Includes `TicTacToeGUI`, which implements the Tkinter-based graphical user interface, handling user interactions and displaying the game state.

## How it was Created

This project was interactively developed using a Gemini-powered CLI agent. The agent assisted in:

1.  **Project Setup**: Initializing the project structure.
2.  **Core Implementation**: Writing the initial game logic and GUI.
3.  **Feature Addition**: Integrating the AI opponent.
4.  **Refactoring**: Restructuring the codebase into a Domain-Driven Design architecture for improved readability and maintainability.
5.  **Version Control**: Managing Git commits and pushes to GitHub.

## How to Run

To run this game, ensure you have Python 3 installed on your system. Then, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/sskelkar/gemini-tic-tac-toe-desktop.git
    ```
2.  **Navigate to the project directory**:
    ```bash
    cd gemini-tic-tac-toe-desktop
    ```
3.  **Run the game**:
    ```bash
    python3 main.py
    ```

The game window should appear, and you can start playing against the AI opponent.