# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:17:31 2021

@author: zhill
"""

import pygame
import sys

def run_game():
    """Displays the events of each key press."""
    pygame.init()
    
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Key presses.")
    bg_colour = (230,230,230)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
            elif event.type == pygame.KEYDOWN:
                keys = print(event)
        screen.fill(bg_colour)
        pygame.display.flip()
        
run_game()