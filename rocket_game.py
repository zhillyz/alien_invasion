# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:52:21 2021

@author: zhill
"""

import pygame
from settings import Settings
from rocket import Rocket
import rocket_game_functions as gf

def run_game():
    """Runs rocket ship game."""
    #starts pygame and the screen where the game will run
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Rocket game")
    
    #creates rocket
    rocket = Rocket(screen,ai_settings)
    
    #Start the main loop for the game.
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings, screen, rocket)
        
run_game()