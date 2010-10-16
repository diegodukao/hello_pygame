#! /usr/bin/env python

from pygame import sprite, time

class AnimatedSprite(sprite.Sprite):
    def __init__(self, position, frames, fps=10):
        sprite.Sprite.__init__(self)
        self.frames = frames
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        
        #Track the time the animation was created and the time between
        #updates. That way we can figure out when the image needs to be
        #changed
        self.current_frame = 0
        self.start = time.get_ticks()
        self.last_update = 0
        if fps == 0:
            fps = 1
        self.delay = 1000/fps
        
    def update(self):
        '''Update the frame of the animation. It will only occur if the
        time passed since the last update is longer than the delay 
        (1000/fps)'''
        t = time.get_ticks()
        
        if t - self.last_update > self.delay:
            self.change_frame()
            self.last_update = t
        
    def change_frame(self):
        if self.current_frame < (len(self.frames) - 1):
            self.current_frame += 1
        else:
            self.current_frame = 0
        
        self.image = self.frames[self.current_frame]
