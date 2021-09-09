# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 21:44:38 2021

@author: zhill
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Create an instance of an alien."""
    
    def __init__(self, ai_settings, screen):
        """Initialises alien attributes."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #load alien image and get its rect
        self.image = pygame.image.load('images/ufo2.png').convert_alpha()
        # sizex = 100
        # sizey = 60
        # self.image = pygame.transform.scale(self.orig_image, (sizex,sizey))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each new alien at the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact position.
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
        
    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * 
                       self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
        