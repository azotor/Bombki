import pygame, random

class OverState:
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        self.font_title = pygame.font.SysFont( "ArialBlack", 38 )
        self.font_tap = pygame.font.SysFont( "Arial", 24 )
        self.changeTo = None
        self.score = 0
    
    def enter( self ):
        self.changeTo = None
        self.icon = pygame.image.load( 'Assets/Images/bombka{}.png'.format( random.randint( 1, 3 ) ) ).convert_alpha()
        self.icon_rect = self.icon.get_rect( center = ( self.surf.get_width() / 2, self.surf.get_height() / 2 ) )
        
        pygame.mouse.set_visible( True )
    
    def update( self, main ):
        self.score = main.states[ 'play' ].hud.score
        if main.mouseDown == True:
            self.changeTo = 'play'
    
    def render( self ):
        self.surf.fill( '#222222' )
        
        self.surf.blit( self.icon, self.icon_rect )
        
        bg = pygame.Surface( ( self.surf.get_width(), 100 ), pygame.DOUBLEBUF ).convert_alpha()
        bg.fill( ( 0, 0, 0, 100 ) )
        self.surf.blit( bg, ( 0, self.surf.get_height() / 2 - 30 ) )
        
        title = self.font_title.render( "Złapane bombki {}".format( self.score ), False, ( 255, 255, 255 ) )
        title_rect = title.get_rect( center = ( self.surf.get_width() / 2, self.surf.get_height() / 2 ) )
        tap = self.font_tap.render( "Kliknij aby zacząć!", False, ( 255, 255, 255 ) )
        tap_rect = tap.get_rect( center = ( self.surf.get_width() / 2, self.surf.get_height() / 2 + 40 ) )
        self.surf.blit( title, title_rect )
        self.surf.blit( tap, tap_rect )