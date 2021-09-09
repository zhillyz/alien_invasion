# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:21:21 2021

@author: zhill
"""

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_image = pygame.image.load('images/background.jpg').convert()
    
    #Make the Play button
    play_button = Button(ai_settings, screen, 'Play')
    
    #Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    #Make a ship.
    ship = Ship(screen,ai_settings)
    
    #Make a group to store bullets and aliens in.
    bullets = Group()
    aliens = Group()
    
    #Create fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, 
                        ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button, bg_image)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship,
                              aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship,
                             aliens, bullets, play_button, bg_image)
        
run_game()
input('')