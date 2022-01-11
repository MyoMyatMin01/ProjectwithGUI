import pygame

pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

class Player():

    def __init__(self):

        self.walkRight = [pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                            'Changed size of Terrorists/1_terrorist_1_Walk_000.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_001.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_002.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_003.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_004.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_005.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_006.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_007.png')]

        self.walkLeft = [pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                           'Changed size of Terrorists/1_terrorist_1_Walk_000.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_001.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_002.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_003.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_004.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_005.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_006.png')
                    , pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/'
                                        'Changed size of Terrorists/1_terrorist_1_Walk_007.png')]

        self.bg = pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/Kill your crush background cartoon.jpg')
        self.char = pygame.image.load('C:/Users/ACER/Pictures/Pygame-Images/Game/standing.png')


        self.x = 50
        self.y= 300
        self.movement = 10
        self.width = 64
        self.height = 64
        self.left = False
        self.right = False
        self.walkCount = 0
        self.isJump = False
        self.jumpCount = 10
        self.win = pygame.display.set_mode((998, 454))
        self.standing = True

    def move_character_change_background(self):
        global walkCount
        self.win.blit(self.bg, (0, 0))

        if not(self.standing):
            if self.walkCount >= 8:
                self.walkCount = 0

            if self.left:
                self.win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                self.win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.left:
                self.win.blit(self.walkLeft[0], (self.x, self.y))
            else:
                self.win.blit(self.walkRight[0], (self.x, self.y))

        pygame.display.update()

    def input_from_user(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.movement
            self.left = True
            self.right = False
            self.standing = False

        elif keys[pygame.K_RIGHT]:
            self.x += self.movement
            self.right = True
            self.left = False
            self.standing = False

        else:
            self.standing = True

        if True:

            if keys[pygame.K_SPACE]:
                self.isJump = True
                self.right = False
                self.left = False

        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

man = Player()

while True:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    man.input_from_user()
    man.move_character_change_background()