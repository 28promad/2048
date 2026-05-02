# 2048 Game

## Overview
This is a Python implementation of the popular 2048 game. The objective of the game is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. The game ends when there are no valid moves left.

## Features
- **Dynamic Board Generation**: The game initializes with a 4x4 grid and generates two tiles with the number 2 at random positions.
- **Tile Movement and Merging**: Tiles can be moved in four directions (up, down, left, right). Tiles with the same number merge into one tile with their sum.
- **Game Over Detection**: The game ends when no valid moves are possible.
- **Random Tile Generation**: After each move, a new tile with the number 2 is added to a random unoccupied position.

## How to Play
1. Run the game by executing the `main.py` file.
2. Use the following keys to control the game:
   - `w`: Move tiles up
   - `a`: Move tiles left
   - `s`: Move tiles down
   - `d`: Move tiles right
   - `q`: Quit the game
3. Combine tiles with the same number to achieve the highest score possible.

## Code Structure
- **`main.py`**: Contains the game logic, including board initialization, tile movement, merging, and game loop.
- **Key Functions**:
  - `reset_board()`: Initializes the game board.
  - `add_two(board)`: Adds a new tile with the number 2 to a random unoccupied position.
  - `move(direction, board)`: Handles tile movement and merging based on the input direction.
  - `print_board(board)`: Displays the current state of the game board.

## Requirements
- Python 3.6 or higher

## Running the Game
1. Ensure Python is installed on your system.
2. Navigate to the `2048` directory.
3. Run the game using the command:
   ```bash
   python main.py
   ```

## Future Improvements
- Add a scoring system to track the player's progress.
- Implement a graphical user interface (GUI) for better user experience.
- Add support for undoing moves.

Enjoy playing 2048!