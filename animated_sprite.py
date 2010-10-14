#! /usr/bin/env python

from pygame import sprite

class AnimatedSprite(sprite.Sprite):
    def __init__(self, position, frames, fps=10):
        sprite.Sprite.__init__(self)
        self.image = frames[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = position
