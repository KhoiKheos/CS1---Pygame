"""
Pygame Template

    Import
    Initialize
    Create Window
    Initialize Clock for FPS

    Loop
        Get events
            if quit
                quit pygame
        Apply Logic
        Update Display/Window
        Set FPS

"""

# Import
import pygame
from pygame import mixer

# Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")

# Background Sound
mixer.music.load("../Resources/Sound Effect/Bgm.wav")
mixer.music.play(-1)

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    window.fill((255, 255, 255))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)
