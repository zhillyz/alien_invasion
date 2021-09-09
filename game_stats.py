# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 23:39:13 2021

@author: zhill
"""
import json

class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #start alien invasion in an inactive state.
        self.game_active = False
        
        #High score should never be reset.
        try:
            with open('highscore.json') as f_obj:
                self.high_score = json.load(f_obj)
        except FileNotFoundError:
            self.high_score = 0
        
    def reset_stats(self):
        """Initializes statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1