import pygame
pygame.init()

win_width, win_height = 960, 696

win = pygame.display.set_mode((win_width, win_height))
bg1 = pygame.image.load("Assets/Bgs/BG1.jpg")

class Player():
    def __init__(self, image, x, y, speed):
        self.image = pygame.transform.scale(pygame.image.load(image), (92, 121))
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.speed = speed
        self.right = False
        self.left = False
        self.idle_state = True
        self.jump_state = False
        self.jump_count = 20
        self.animation_count = 0
    
    def reset(self):
        if self.left:
            win.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
        elif self.right:
            win.blit(self.image, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.left = True
            self.right = False
            self.idle_state = False
        elif keys[pygame.K_d]:
            self.x += self.speed
            self.right = True
            self.left = False
            self.idle_state = False
        else:
            self.right = False
            self.left = False
            self.idle_state = True
        
        if not self.jump_state:
            if keys[pygame.K_SPACE]:
                self.jump_state = True
        else:
            if self.jump_count >= -20:
                if self.jump_count < 0:
                    self.y += self.jump_count ** 2 / 7
                else:
                    self.y -= self.jump_count ** 2 / 7
                self.jump_count -= 1
            else:
                self.jump_state = False
                self.jump_count = 20
        

class Magician(Player):
    def __init__(self, image, x, y, speed):
        super().__init__(image, x, y, speed)

        self.idle = [
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Idle/Idle_1.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Idle/Idle_2.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Idle/Idle_3.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Idle/Idle_4.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Idle/Idle_5.png"), (92, 121))
        ]
        self.run_right = [
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Right/Run_1.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Right/Run_2.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Right/Run_3.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Right/Run_4.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Right/Run_5.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Right/Run_6.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Right/Run_7.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Right/Run_8.png"), (92, 121))
        ]
        self.run_left = [
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Left/Run_1.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Left/Run_2.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Left/Run_3.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Left/Run_4.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Left/Run_5.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Left/Run_6.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Left/Run_7.png"), (92, 121)),
            pygame.transform.scale(pygame.image.load("Assets/Player/Magician/Run/Left/Run_8.png"), (92, 121))
        ]

player = Magician("Assets/Player/Magician/Idle/Idle_1.png", win_width // 2, win_height - 160, 6)

clock = pygame.time.Clock()
FPS = 120

def draw_win():
    win.blit(bg1, (-480, 0))

    if player.animation_count + 1 >= 120:
        player.animation_count = 0

    if player.left:
        win.blit(player.run_left[player.animation_count // 15], (player.x, player.y))
        player.animation_count += 1
    elif player.right:
        win.blit(player.run_right[player.animation_count // 15], (player.x, player.y))
        player.animation_count += 1
    elif player.idle_state or player.jump_state:
        win.blit(player.idle[player.animation_count // 24], (player.x, player.y))
        player.animation_count += 1
    

    pygame.display.update()
    clock.tick(FPS)

game = True

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.reset()
    player.move()
    
    draw_win()

    pygame.display.update()
    clock.tick(FPS)

quit()