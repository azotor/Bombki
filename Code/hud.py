import pygame

class Hud:
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        self.font = pygame.font.SysFont( "ArialBlack", 24 )
        self.score = 0
        self.time = 0
        self.hp = 3
        
    def update( self ):
        pass#self.time = pygame.time.get_ticks()
    
    def render( self ):
        surf_score = pygame.Surface( ( 250, 50 ), pygame.DOUBLEBUF ).convert_alpha()
        surf_score.fill( ( 0, 0, 0, 100 ) )
        text = self.font.render( "Punkty: {}".format( self.score ), False, ( 255, 255, 255 ) )
        surf_score.blit( text, ( 10, 5 ) )
        self.surf.blit( surf_score, ( 10, 10 ) )
        
        surf_time = pygame.Surface( ( 250, 50 ), pygame.DOUBLEBUF ).convert_alpha()
        surf_time.fill( ( 0, 0, 0, 100 ) )
        text = self.font.render( "Czas: {}".format( ( pygame.time.get_ticks() - self.time ) // 1000 ), False, ( 255, 255, 255 ) )
        surf_time.blit( text, ( 10, 5 ) )
        self.surf.blit( surf_time, ( self.surf.get_width() - 260, 10 ) )
        
        surf_time = pygame.Surface( ( 50, 50 ), pygame.DOUBLEBUF ).convert_alpha()
        surf_time.fill( ( 0, 0, 0, 100 ) )
        text = self.font.render( str( self.hp ), False, ( 255, 255, 255 ) )
        rect = text.get_rect()
        rect.centerx = 25
        rect.centery = 25
        surf_time.blit( text, rect )
        self.surf.blit( surf_time, ( self.surf.get_width() / 2 - 25, 10 ) )