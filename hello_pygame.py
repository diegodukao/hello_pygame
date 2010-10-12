#! /usr/bin/env python

import pygame

screen = pygame.display.set_mode((640, 480))
running = True

#guy_image = pygame.image.load("data/images/guy.png")
#guy_rect = guy_image.get_rect()

world_image = pygame.image.load("data/images/world.png")
world_rect = world_image.get_rect()
world_rect.topleft = [200, 200]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #screen.blit(guy_image, guy_rect)
    screen.blit(world_image, world_rect)
    pygame.display.flip()
