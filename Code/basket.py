import pygame

class Basket:
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        self.pos = pygame.math.Vector2( ( self.surf.get_width() / 2, self.surf.get_height() - 110 ) )
        
        sprite_img = pygame.image.load( 'Assets/Images/koszyk.png' ).convert_alpha()
        self.sprite = pygame.Surface( ( sprite_img.get_width(), sprite_img.get_height() ) )
        self.sprite.fill( '#000000' )
        self.sprite.blit( sprite_img, ( 0, 0 ) )
        self.sprite = pygame.transform.scale( self.sprite, ( 110, 60 ) )
        self.sprite.set_colorkey( '#000000' )
    
    def update( self ):
        self.pos[ 0 ] = pygame.mouse.get_pos()[ 0 ]
    
    def render( self ):
        self.surf.blit( self.sprite, self.pos - ( 55, 0 ) )