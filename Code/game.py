import pygame, sys, random

from Code.beginState import BeginState
from Code.playState import PlayState
from Code.overState import OverState

class Game:
    def __init__( self ):
        
        pygame.init()
        self.surf = pygame.display.set_mode( ( 600, 800 ) )
        pygame.display.set_caption( 'Złap bomki' )
        icon = pygame.image.load( 'Assets/Images/bombka{}.png'.format( random.randint( 1, 3 ) ) ).convert_alpha()
        pygame.display.set_icon( icon )
        self.run = True
        self.time = pygame.time.Clock()
        pygame.mixer.music.load( 'Assets/Sounds/music.mp3' )
        pygame.mixer.music.play( -1 )
        
        self.states = {
            'begin' : BeginState(),
            'play' : PlayState(),
            'over' : OverState()
        }
        
        self.state = self.states[ 'begin' ]
        self.state.enter()
        
        self.mouseDown = False
        
        self.loop()
    
    def loop( self ):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseDown = True
                
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouseDown = False
                    
                
            self.update()
            self.render()
            self.time.tick( 60 )
        
        pygame.quit()
        sys.exit()
    
    def update( self ):
        self.state.update( self )
        if self.state.changeTo:
            self.changeState( self.state.changeTo )
    
    def render( self ):
        
        self.state.render()
        
        pygame.display.update()
        
    def changeState( self, state ):
        self.state = self.states[ state ]
        self.state.enter()