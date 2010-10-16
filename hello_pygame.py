#! /usr/bin/env python

import pygame
from animated_sprite import AnimatedSprite
from world import World

class Game:
    def __init__(self, size):
        pygame.init()
        pygame.key.set_repeat(200, 5)
        
        self.screen = pygame.display.set_mode(size)
        
        guy_image = pygame.image.load("data/images/guy_idle.png")
        guy_image = guy_image.convert()
        self.guy = AnimatedSprite([0, 0], guy_image, 10)
        
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
            
            self.guy.update(self.screen)
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

if __name__ == "__main__":
    game = Game((640,480))
    game.main_loop()
