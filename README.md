# Conway's Game of Life
An interactive simulation and visualizer of John Conway's Game of Life created using Python's pygame library. 

## Introduction
The Game of Life is a zero-player game developed by John Conway in 1970. It is played on an infinite grid of square cells and relies on the principles of cellular-automaton; at each moment in time, a cell can change state depending on the states of it's neighboring cells. 

GIF

## Conway's Rules
The game is played on an infinite grid of square cells where these cells can be initialized as "alive" or "dead". The evolution of these cell patterns is only determined by it's initial state, and is dependent of a set of defined rules:
- **Birth:** a cell that is dead at time $t$ will be alive at time $t+1$ if three of it's neighbours were alive at time $t$.
- **Death:** a cell alive at time $t$ dies at time $t+1$ if it has less than two live neighbors or if it has more than three live neighbors. 
- **Survival:** a cell survives from $t$ to $t+1$ if only two or three of it's neighbors were alive at time $t$. 

These three simple rules allow the game board to evolve based on the board's initial state. This allows us to create patterns or "life-forms" on the board. 

## Results
### How to Play
- `Left click` on a cell in the grid to highlight it, initializing it to alive. You can also hold `left click` and drag your mouse cursor to highlight multiple grids quickly.
- Press the `space bar` to run the game and see the pattern evolve. 
- Press `return` to clear the board.

https://user-images.githubusercontent.com/80748482/184883921-f4dd2b20-f25a-499d-afb9-2a9ab8993286.mp4

## Files
- **life.py** - Project file
- **packages.txt** - Python packages needed to run this project

## References
- Gymrek, M., 2010. _Conway's Game of Life_.
- Martin, R., 2017. Conway’s Game of Life in python. [Blog] _Medium_, Available at: <https://medium.com/@martin.robertandrew/conways-game-of-life-in-python-2900a6dcdc97> [Accessed 29 May 2022].
- Neural Nine, 2022. _Conway's Game of Life in Python_. [video] Available at: <https://www.youtube.com/watch?v=cRWg2SWuXtM> [Accessed 26 May 2022].
- Roberts, S., 2020. The Lasting Lessons of John Conway’s Game of Life. _The New York Times_, [online] Available at: <https://www.nytimes.com/2020/12/28/science/math-conway-game-of-life.html> [Accessed 29 May 2022].
