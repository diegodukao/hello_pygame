#! /usr/bin/env python

from pygame import sprite, time

class AnimatedSprite(sprite.Sprite):
    def __init__(self, position, image_frames, fps=10):
        sprite.Sprite.__init__(self)
        self.frames = self.get_frames(image_frames, 1, 4)
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
        
    def get_frames(self, image, lines, columns):
        image_width, image_height = image.get_size()
        
        frames = []
        frame_width = image_width / columns
        for i in xrange(columns):
            x = i * frame_width
            y = 0
            frames.append(image.subsurface((x, y, frame_width, image_height)))
        
        return frames
        
    
    def update(self, screen):
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
