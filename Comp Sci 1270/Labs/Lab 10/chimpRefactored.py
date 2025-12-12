#!/usr/bin/env python
"""pygame.examples.chimp

This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation,
follow along in the tutorial.
"""

# Import Modules
import os
import pygame



class Entity(pygame.sprite.Sprite):

    def __init__(self, name, colorkey=None, scale=1, data_dir = ""):
        super().__init__()
        self.name = name
        self.colorkey = colorkey
        self.scale = scale
        self.data_dir = data_dir
        fullname = os.path.join(self.data_dir, self.name)
        self.image = pygame.image.load(fullname)
        self.image = self.image.convert()


        if colorkey is not None:
            if colorkey == -1:
                colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey, pygame.RLEACCEL)
        
        self.image = pygame.transform.scale_by(self.image, scale)
        self.rect = self.image.get_rect()






# functions to create our resources



def load_sound(name, data_dir):
    class NoneSound:
        def play(self):
            pass

    



    if not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
   
    try:
        sound = pygame.mixer.Sound(fullname)
    except FileNotFoundError:
        sound = "Sound not found"
    
    return sound


# classes for our game objects
class Fist(Entity):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(one, name, colorkey, scale, dir):
        super().__init__(name, colorkey, scale, dir)  # call Sprite initializer
        
        
        one.fist_offset = (-235, -80)
        one.punching = False

    def update(one):
        """move the fist based on the mouse position"""
        pos = pygame.mouse.get_pos()
        one.rect.topleft = pos
        one.rect.move_ip(one.fist_offset)
        if one.punching:
            one.rect.move_ip(15, 25)

    def punch(one, target):
        """returns true if the fist collides with the target"""
        if not one.punching:
            one.punching = True
            hitbox = one.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(one):
        """called to pull the fist back"""
        one.punching = False


class Chimp(Entity):
    """moves a monkey critter across the screen. it can spin the
    monkey when it is punched."""

    def __init__(me, name, colorkey, scale, dir):
        super().__init__(name, colorkey, scale, dir)
        
    
        screen = pygame.display.get_surface()
        me.area = screen.get_rect()
        me.rect.topleft = 10, 90
        me.move = 18
        me.dizzy = False

    def update(me):
        """walk or spin, depending on the monkeys state"""
        if me.dizzy:
            me._spin()
        else:
            me._walk()

    def _walk(me):
        """move the monkey across the screen, and turn at the ends"""
        newpos = me.rect.move((me.move, 0))
        if not me.area.contains(newpos):
            if me.rect.left < me.area.left or me.rect.right > me.area.right:
                me.move = -me.move
                newpos = me.rect.move((me.move, 0))
                me.image = pygame.transform.flip(me.image, True, False)
        me.rect = newpos

    def _spin(me):
        """spin the monkey image"""
        center = me.rect.center
        me.dizzy = me.dizzy + 12
        if me.dizzy >= 360:
            me.dizzy = False
            me.image = me.original
        else:
            rotate = pygame.transform.rotate
            me.image = rotate(me.original, me.dizzy)
        me.rect = me.image.get_rect(center=center)

    def punched(me):
        """this will cause the monkey to start spinning"""
        if not me.dizzy:
            me.dizzy = True
            me.original = me.image


def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in
    a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((1280, 480), pygame.SCALED)
    pygame.display.set_caption("Monkey Fever")
    pygame.mouse.set_visible(False)


    
    if not pygame.font:
        print("Warning, fonts disabled")
    if not pygame.mixer:
        print("Warning, sound disabled")

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")

    print(main_dir, data_dir)


    # Create The Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put Text On The Background, Centered
    font = pygame.Font(None, 64)
    text = font.render("Pummel The Chimp, And Win $$$", True, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
    background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    whiff_sound = load_sound("whiff.wav", data_dir)
    punch_sound = load_sound("punch.wav", data_dir)
    chimp = Chimp("chimp.png", -1, 4, data_dir)
    fist = Fist("fist.png", -1, 1, data_dir)
    all_sprites = pygame.sprite.Group(chimp, fist)
    clock = pygame.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                going = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()  # punch
                    chimp.punched()
                else:
                    whiff_sound.play()  # miss
            elif event.type == pygame.MOUSEBUTTONUP:
                fist.unpunch()

        all_sprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()