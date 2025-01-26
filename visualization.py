import pygame
import random
import time


pygame.init()

print("Welcome to random walk visualization - Cody Rabie")
input_wh = int(input("What size do you want the canvas to be? (int value): "))  # Getting user selected size, between 100 and 800 ofr pygame display
while input_wh>800 or input_wh<100:
    input_wh = int(input("Size must be less than 800 and over 100, try again: "))


cell_am = int(input("How many cells would you like to spawn for this visualization: ")) # Cell amount starting at one and maxing at the width/height of canvas (so user doesn't spawn too many)
while cell_am>input_wh or cell_am<1:
    cell_am = int(input("Cell amount cannot be more than the width of the canvas or less than 1, try again: "))


# Canvas dimensions and setup
WIDTH, HEIGHT = input_wh, input_wh
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Walk Visualization")

# Colors, potentially allow user to choose these in the future
white = (255, 255, 255)
black = (0, 0, 0)

# Grid properties
UNIT_SIZE = 3  # Each unit is 3x3
NUM_UNITS = cell_am  # Number of white units to start with

# Directions for movement: up, down, left, right, randomly chose in the Unit class
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (dx, dy)

# Initialize units list
units = []

# Check if unit is within boundary
def in_bounds(x, y):
    return 0 <= x < WIDTH // UNIT_SIZE and 0 <= y < HEIGHT // UNIT_SIZE

# Unit class 
class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = white
        self.direction = random.choice(DIRECTIONS)   

    def move(self):
        direction = self.direction
        new_x = self.x + direction[0]
        new_y = self.y + direction[1]

        if in_bounds(new_x, new_y):
            self.x, self.y = new_x, new_y

    def render(self):
        pygame.draw.rect(canvas, self.color, (self.x * UNIT_SIZE, self.y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE))

# Function to initialize the white units randomly, ensuring no overlap
def initialize_units():
    positions = set()

    while len(units) < NUM_UNITS:
        x = random.randint(0, WIDTH // UNIT_SIZE - 1)
        y = random.randint(0, HEIGHT // UNIT_SIZE - 1)

        if (x, y) not in positions:
            units.append(Unit(x, y))  # Create a new Unit object
            positions.add((x, y))

# Function to check for tile collisions and spawning of new white tiles
def check_for_collisions_and_spawn():
    new_white_tiles = []  # List to store newly created white tiles
    positions = {}  # Dictionary to track tile positions and handle collisions
    to_remove = set()  # Set to track units to remove after processing

    for unit in units:
        # Move each unit and check if a new white tile should be spawned
        unit.move()

        # Track position of the unit in a dictionary (coordinates as the key)
        position = (unit.x, unit.y)
        if position not in positions:
            positions[position] = unit
        else:
            # If two units occupy the same position, they "collide" and disappear
            existing_unit = positions[position]
            if existing_unit.color == white and unit.color == white:
                to_remove.add(unit)  
                to_remove.add(existing_unit)  
                continue  

        # If the unit hasn't collided with another, spawn a new white tile
        new_white_tiles.append(Unit(unit.x, unit.y))  # Create a new white tile at the same position

    # Remove all the marked units (those that collided)
    for unit in to_remove:
        if unit in units:
            units.remove(unit)

    # Add all the newly created white tiles to the units list
    units.extend(new_white_tiles)

# Function to render units
def render_units():
    canvas.fill(black)  # Fill background with black

    for unit in units:
        unit.render()  # Render each unit

    pygame.display.flip()



running = True
initialize_units()  # Initialize the white units

# Main loop
while running:
    start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    check_for_collisions_and_spawn()  # Check for collisions and spawn new white tiles

    render_units()  # Render updated canvas

    elapsed_time = time.time() - start_time
    if elapsed_time < 1: 
        time.sleep(1 - elapsed_time)

pygame.quit()
