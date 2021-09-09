# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 01:24:25 2021

@author: zhill
"""

import pygame
import sys
from character import Character

def run_game():
    """Run the game."""
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Blue Sky")
    bg_colour = (0,0,230)
    
    character = Character(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    character.rect.centerx += 2
                elif event.key == pygame.K_LEFT:
                    character.rect.centerx -= 2
        
        screen.fill(bg_colour)
        character.blitme()
        pygame.display.flip()
        
run_game()