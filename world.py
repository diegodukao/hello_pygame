#! /usr/bin/env python

import pygame

class World(pygame.sprite.Sprite):
    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = position
    
    def move(self, key):
        x_move = 0
        y_move = 0
        distance = 1
        
        if key == pygame.K_DOWN:
            y_move += distance
        elif key == pygame.K_UP:
            y_move -= distance
        elif key == pygame.K_RIGHT:
            x_move += distance
        elif key == pygame.K_LEFT:
            x_move -= distance
        
        self.rect.move_ip(x_move, y_move)
