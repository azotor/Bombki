import pygame, random

from Code.cooldown import Cooldown

class Drop:
    
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        self.size = ( 65, 69 )
        self.pos = pygame.math.Vector2( random.randint( self.size[ 0 ], self.surf.get_width() - self.size[ 0 ] ), -self.size[ 1 ] )
        self.dir = pygame.math.Vector2( 0, random.uniform( 1.0, 3.0 ) )
        self.states = {
            'drop' : 0,
            'broken' : 1,
            'remove' : 2,
            'point' : 3
        }
        self.state = self.states[ 'drop' ]
        self.brokenCooldown = Cooldown()
        
        sprite_img = pygame.image.load( 'Assets/Images/bombka{}.png'.format( random.randint( 1, 3 ) ) ).convert_alpha()
        self.sprite = pygame.Surface( ( sprite_img.get_width(), sprite_img.get_height() ) )
        self.sprite.fill( '#000000' )
        self.sprite.blit( sprite_img, ( 0, 0 ) )
        self.sprite = pygame.transform.scale( self.sprite, self.size )
        self.sprite.set_colorkey( '#000000' )
        
        self.broken = []
        part_width = self.sprite.get_width() // 2
        part_height = self.sprite.get_height() // 2
        for i in range( 4 ):
            sprite = pygame.Surface( ( part_width, part_height ) ).convert_alpha()
            sprite.fill( '#000000' )
            part_x = i // 2 * part_width
            part_y = i % 2 * part_height
            sprite.blit( self.sprite, ( 0, 0 ), ( part_x, part_y, part_width, part_height ) )
            sprite.set_colorkey( '#000000' )
            pos = pygame.math.Vector2( part_x, part_y )
            dir = pygame.math.Vector2( random.uniform( -3, 3 ), random.uniform( -3, 3 ) )
            self.broken.append( { 'sprite' : sprite, 'pos' : pos, 'dir' : dir } )
    
    def update( self ):
        if self.state == self.states[ 'drop' ]:
            self.pos += self.dir
            if self.hitTheFloor():
                self.state = self.states[ 'broken' ]
                self.brokenCooldown.start( 200 )
                pos = pygame.math.Vector2( self.pos[ 0 ], self.pos[ 1 ] )
                for part in self.broken:
                    part[ 'pos' ] += pos
        elif self.state == self.states[ 'broken' ]:
            for part in self.broken:
                part[ 'pos' ] += part[ 'dir' ]
            self.brokenCooldown.update()
            if not self.brokenCooldown.run:
              self.state = self.states[ 'remove' ]  
        
    def render( self ):
        if self.state == self.states[ 'drop' ]:
            self.surf.blit( self.sprite, self.pos )
        elif self.state == self.states[ 'broken' ]:
            for part in self.broken:
                self.surf.blit( part[ 'sprite' ], part[ 'pos' ] )
        
    def hitTheFloor( self ):
        if self.pos[ 1 ] >= self.surf.get_height() - 90:
            return True
        return False

    def hitBasket( self, basket ):
        if self.state == self.states[ 'drop' ]:
            if(
                self.pos[ 0 ] + self.sprite.get_width() >= basket.pos[ 0 ] - basket.sprite.get_width() / 2 and
                self.pos[ 0 ] <= basket.pos[ 0 ] + basket.sprite.get_width() / 2 and
                self.pos[ 1 ] + self.sprite.get_height() >= basket.pos[ 1 ]
            ):
                self.state = self.states[ 'point' ]
                return True
        return False