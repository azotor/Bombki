import pygame

class Cooldown:
    def __init__( self ):
        self.run = False
        self.begin = 0
        self.end = 0
    
    def update( self ):
        if self.run:
            self.begin = pygame.time.get_ticks()
            if self.begin >= self.end:
                self.stop()
    
    def start( self, time ):
        self.begin = pygame.time.get_ticks()
        self.end = self.begin + time
        self.run = True
    
    def stop( self ):
        self.begin = 0
        self.end = 0
        self.run = False