import pygame

from Code.drop import Drop
from Code.cooldown import Cooldown
from Code.basket import Basket
from Code.hud import Hud

class PlayState:
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        bg_img = pygame.image.load( 'Assets/Images/bg.png' ).convert_alpha()
        self.bg = pygame.Surface( ( bg_img.get_width(), bg_img.get_height() ) ).convert_alpha()
        self.bg.blit( bg_img, ( 0, 0 ) )
        self.bg = pygame.transform.scale( self.bg, ( 600, 800 ) )
        self.cooldown = Cooldown()
        self.changeTo = None
        self.point_effect = pygame.mixer.Sound( 'Assets/Sounds/point.mp3' )
        self.crash_effect = pygame.mixer.Sound( 'Assets/Sounds/crash.mp3' )
        self.point_play = False
        self.crash_play = False
    
    def enter( self ):
        self.drops = []
        self.dropcooldown = 3000
        self.basket = Basket()
        self.hud = Hud()
        self.changeTo = None
        self.hud.time = pygame.time.get_ticks()
        
        pygame.mouse.set_visible( False )
    
    def update( self, main ):
        self.cooldown.update()
        
        if not self.cooldown.run:
            self.drops.append( Drop() )
            self.cooldown.start( self.dropcooldown )
            if self.dropcooldown > 100:
                self.dropcooldown -= 1
        
        self.basket.update()
        
        if len( self.drops ):
            i = 0
            for drop in self.drops:
                drop.update()
                if drop.hitBasket( self.basket ):
                    self.hud.score += 1
                    self.point_play = True
                if drop.state == drop.states[ 'remove' ]:
                    self.drops.pop( i )
                    self.hud.hp -= 1
                    self.crash_play = True
                    if self.hud.hp == 0:
                        self.changeTo = 'over'
                        break
                if drop.state == drop.states[ 'point' ]:
                    self.drops.pop( i )
                i += 1
        
        self.hud.update()
        self.effects()

    def effects( self ):
        if self.point_play:
            self.point_effect.play( 0 )
            self.point_play = False
        if self.crash_play:
            self.crash_effect.play( 0 )
            self.crash_play = False

    def render( self ):
        self.surf.fill( '#222222' )
        self.surf.blit( self.bg, ( 0, 0 ) )
        
        if len( self.drops ):
            for drop in self.drops:
                drop.render()
                
        self.basket.render()
        
        self.hud.render()