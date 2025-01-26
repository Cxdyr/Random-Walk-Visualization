# Random-Walk-Visualization

## Description
This project simulates a random walk visualization using `pygame`. It creates a grid of cells where a set of units move randomly, leaving a trail of white cells in their path. When two units collide, they disappear. New units are spawned at different positions as the simulation progresses.

## Features
- User-defined canvas size (between 100 and 800).
- User-defined number of initial white units (between 1 and the width/height of the canvas).
- Units move randomly in four directions (up, down, left, right).
- Collisions occur when two units land on the same grid cell.
- New white units are spawned as the units move.

## Requirements
- `pygame` library

To install the required libraries, run the following command:

```bash
pip install pygame
```

## How to Run Program
- Run git clone on this repository
- From terminal run py visualization.py
- Enter the desired size of the canvas
- Enter the desired amount of initial cells to spawn
- Watch as the visualization works
