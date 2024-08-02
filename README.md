# Python Tetris  

## Description  

This project is an implementation of the classic Tetris game in Python using the Tkinter library for the graphical interface. The game includes the basic functions of Tetris, such as falling tetrominoes, shape controls, line deletion, score calculation, difficulty levels, and the ability to restart the game.  

## Features  

### Main Functions  

- **Falling Shapes (Tetrominoes)**: Shapes fall from the top to the bottom of the play area.  

### Shape Controls:  

- Rotate Shape (up arrow key)  
- Move Shape Left (left arrow key)  
- Move Shape Right (right arrow key)  
- Speed Up Shape Drop (down arrow key)  
- Instant Drop Shape (space bar)  

- **Line Formation and Deletion**: When a horizontal line is filled with blocks, it disappears, and the blocks above it drop down one line.  
- **Points and Levels**: The player earns points for each removed line. The difficulty level increases with the number of points or lines deleted, speeding up the fall of the shapes.  
- **Game Over**: The game ends when the shapes fill the play area to the top.  
- **Restart Game**: A button is available to restart the game.  

### Additional Functions  

- **Hold Shape**: Ability to temporarily hold one shape and use it later.  
- **Next Shape Preview**: Shows which shape will appear next, helping the player plan their moves.  

## Installation and Running  

To run this project, you will need Python 3 and the Tkinter library, which usually comes with the standard Python library.  

1. Clone the repository or download the project files.  
2. Navigate to the project directory.  

   ```bash  
   git clone <URL of your repository>  
   cd <main.py>
