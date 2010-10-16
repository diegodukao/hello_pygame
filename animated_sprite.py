#! /usr/bin/env python

from pygame import sprite

class AnimatedSprite(sprite.Sprite):
    def __init__(self, position, frames, fps=10):
        sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.frames = frames
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        
    def update(self):
        if self.current_frame < (len(self.frames) - 1):
            self.current_frame += 1
        else:
            self.current_frame = 0
        
        self.image = self.frames[self.current_frame]
