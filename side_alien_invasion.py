# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:21:21 2021

@author: zhill
"""

import pygame
from pygame.sprite import Group
from settings import Settings
from side_ship import Ship
import side_game_functions as gf

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #Make a ship.
    ship = Ship(screen,ai_settings)
    
    #Make a group to store bullets in.
    bullets = Group()
    
    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets,screen)
        gf.update_screen(ai_settings, screen, ship, bullets)
        print(len(bullets))
        
run_game()
