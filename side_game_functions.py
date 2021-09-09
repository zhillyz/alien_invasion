# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 01:05:34 2021

@author: zhill
"""

import sys
import pygame
from side_bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False 
        
def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()    
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
     #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_colour)
    
    #Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
            
    #Make the most recently drawn screen visible.
    pygame.display.flip()
    
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    #Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    
def update_bullets(bullets, screen):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet positions.
    bullets.update()
    screen_rect = screen.get_rect()    
    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.right >= screen_rect.right:
            bullets.remove(bullet)
        