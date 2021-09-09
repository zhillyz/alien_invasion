# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 01:41:25 2021

@author: zhill
"""
import pygame

class Character():
    """Creates character"""
    
    def __init__(self, screen):
        """Initialises the character."""
        self.screen = screen
        self.image = pygame.image.load('images/mario.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """Draw character."""
        self.screen.blit(self.image,self.rect)