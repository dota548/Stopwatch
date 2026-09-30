## Stopwatch – Pygame Project
This project is a simple foundation for a stopwatch application built using Python and Pygame. Right now, it opens a window, sets up the basic event loop, and prepares the structure you’ll expand over time.

# Current Features
Initializes Pygame

Creates a window titled “stopwatch”

Fills the screen with a white background

Runs a stable game loop at 60 FPS

Handles the window close event

This is the essential skeleton needed before adding stopwatch logic, buttons, text rendering, or timing features.

# Code Overview
Main Components
pygame.init()  
Sets up Pygame modules.

pygame.display.set_mode((400, 200))  
Creates a 400×200 window.

screen.fill(white)  
Fills the background with white.

clock.tick(60)  
Limits the loop to 60 frames per second.

Event Loop  
Listens for the QUIT event so the window closes properly.

# Planned Improvements
You mentioned you’ll improve this project day by day. Here are natural next steps you can work toward:

1. Displaying Time
Render text showing elapsed time

Use pygame.time.get_ticks() or Python’s time module

2. Start / Stop / Reset Controls
Keyboard controls (e.g., SPACE to start/stop, R to reset)

Later: clickable buttons

3. UI Improvements
Add fonts

Add colors

Add layout for stopwatch numbers

4. Advanced Features (future)
Lap times

Save session history

Animated transitions

Custom themes

# How to Run
Make sure you have Python and Pygame installed:

pip install pygame
Then run:

python main.py

# License
This project is open for personal learning and experimentation. Feel free to modify and expand it however you like.
