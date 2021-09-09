# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:45:31 2021

@author: zhill
"""

class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230,230,230)
        
        #Ship settings
        self.ship_speed_factor = 8
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3.5
        self.bullet_height = 15
        self.bullet_color = 226,88,34
        self.bullets_allowed = 5
        
        #Alien settings
        self.alien_speed_factor = 2.5
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        #How quickly the game speeds up
        self.speedup_scale = 1.1
        
        #Scoring
        self.alien_points = 50
        #How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

        
    def initialize_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50
        
        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
                
        self.alien_points = int(self.alien_points*self.score_scale)
        print(self.alien_points)