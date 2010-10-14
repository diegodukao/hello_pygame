#! /usr/bin/env python

import pygame
from animated_sprite import AnimatedSprite

class Game:
    def __init__(self, size):
        pygame.init()
        pygame.key.set_repeat(200, 5)
        
        self.screen = pygame.display.set_mode(size)
        
        guy_frames = []
        guy_image = pygame.image.load("data/images/guy_idle1.png")
        guy_frames.append(guy_image)
        guy_image = pygame.image.load("data/images/guy_idle2.png")
        guy_frames.append(guy_image)
        
        self.guy = AnimatedSprite([0, 0], guy_frames, 10)
        
        self.world_image = pygame.image.load("data/images/world.png")
        self.world_rect = self.world_image.get_rect()
        self.world_rect.topleft = [200, 200]
        
        self.running = True
        
    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.key_handler(event.key)
            
            self.screen.blit(self.world_image, self.world_rect)
            self.screen.blit(self.guy.image, self.guy.rect)
            pygame.display.flip()

    def key_handler(self, key):
        if (key == pygame.K_DOWN or
           key == pygame.K_UP or
           key == pygame.K_LEFT or
           key == pygame.K_RIGHT):
            self.snake_move(key)
        
    def snake_move(self, key):
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
        
        self.world_rect.move_ip(x_move, y_move)
        self.screen.fill((0, 0, 0))

if __name__ == "__main__":
    game = Game((640,480))
    game.main_loop()
