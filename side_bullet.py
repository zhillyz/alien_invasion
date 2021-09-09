# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:31:29 2021

@author: zhill
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet at ship's current position."""
        super().__init__()
        self.screen = screen
        
        #create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_height,
                                ai_settings.bullet_width)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right
        
        #store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """Move the bullet up the screen."""
        #Update the decimal position of the bullet.
        self.x += self.speed_factor
        #Update the rect position
        self.rect.x = self.x
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)