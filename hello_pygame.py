#! /usr/bin/env python

import pygame
import math
from animated_sprite import AnimatedSprite, Animation
from world import World

class Game:
    def __init__(self, size):
        pygame.init()
        pygame.key.set_repeat(200, 5)
        
        self.screen = pygame.display.set_mode(size)
        
        guy_image = pygame.image.load("data/images/guy.png")
        guy_image = guy_image.convert()
        self.guy = AnimatedSprite([0, 0], guy_image, 3, 4, 10)
        self.guy_idle = self.guy.create_animation([0, 1, 2, 3, 3, 2, 1, 0])
        self.guy_waving = self.guy.create_animation([7, 8, 9, 10, 11, 11, 10, 9, 8, 7])
        
        self.guy.set_animation(self.guy_idle)
        
        world_image = pygame.image.load("data/images/world.png")
        world_image = world_image.convert()
        self.world = World([200, 200], world_image)
        
        self.running = True
        
    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.key_handler(event.key)
            
            if distance(self.guy, self.world) < 140:
                if self.guy.animation != self.guy_waving:
                    self.guy.set_animation(self.guy_waving)
            else:
                if self.guy.animation != self.guy_idle:
                    self.guy.set_animation(self.guy_idle)
            
            self.guy.update()
            self.screen.blit(self.world.image, self.world.rect)
            self.screen.blit(self.guy.image, self.guy.rect)
            pygame.display.flip()

    def key_handler(self, key):
        if (key == pygame.K_DOWN
        or key == pygame.K_UP
        or key == pygame.K_LEFT
        or key == pygame.K_RIGHT):
            self.world.move(key)
            self.screen.fill((0, 0, 0))

def distance(object1, object2):
    x1 = object1.rect.centerx
    y1 = object1.rect.centery
    
    x2 = object2.rect.centerx
    y2 = object2.rect.centery
    
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

if __name__ == "__main__":
    game = Game((640,480))
    game.main_loop()
