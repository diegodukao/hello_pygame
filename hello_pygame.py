#! /usr/bin/env python

import pygame
from animated_sprite import AnimatedSprite

world_image = pygame.image.load("data/images/world.png")
world_rect = world_image.get_rect()
world_rect.topleft = [200, 200]
screen = pygame.display.set_mode((640, 480))

def game():
    pygame.init()
    
    guy_frames = []
    guy_image = pygame.image.load("data/images/guy_idle1.png")
    guy_frames.append(guy_image)
    guy_image = pygame.image.load("data/images/guy_idle2.png")
    guy_frames.append(guy_image)
    
    guy = AnimatedSprite([0, 0], guy_frames, 10)
    
    #guy_image = pygame.image.load("data/images/guy.png")
    #guy_rect = guy_image.get_rect()

    

    pygame.key.set_repeat(200, 5)
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_handler(event.key)
        
        #screen.blit(guy_image, guy_rect)
        screen.blit(world_image, world_rect)
        screen.blit(guy.image, guy.rect)
        pygame.display.flip()

def key_handler(key):
    if (key == pygame.K_DOWN or
       key == pygame.K_UP or
       key == pygame.K_LEFT or
       key == pygame.K_RIGHT):
        snake_move(key)
        
def snake_move(key):
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
    
    world_rect.move_ip(x_move, y_move)
    screen.fill((0, 0, 0))

if __name__ == "__main__":
    game()
