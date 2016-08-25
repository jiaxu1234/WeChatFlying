#coding:utf-8
import pygame
import random
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,background_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy1.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width,self.height = background_size[0],background_size[1]
        self.speed = 2
        self.active = True

        self.rect.left,self.rect.top = (random.randint(0,self.width - self.rect.width),#定义敌机出现位置
                                        random.randint(-5 * self.rect.height, -5)#保证敌机不会再程序开始就出现
                                        )     #？？？为什么是-5*self.rect.height

        self.destroy_images = []  # 加载飞机损毁图片
        self.destroy_images.extend([pygame.image.load("image/enemy1_down1.png"),
                                    pygame.image.load("image/enemy1_down2.png"),
                                    pygame.image.load("image/enemy1_down3.png"),
                                    pygame.image.load("image/enemy1_down4.png")])

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width),  # 定义敌机出现位置
                                         random.randint(-5 * self.rect.height, -5)  # 保证敌机不会再程序开始就出现
                                         )

class MidEnemy(pygame.sprite.Sprite):
    energy = 5
    def __init__(self,background_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy2.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width,self.height = background_size[0],background_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width),  # 定义敌机出现位置
                                         random.randint(-10 * self.rect.height, -self.rect.height)  # 保证敌机不会再程序开始就出现
                                         )

        self.destroy_images = []  # 加载飞机损毁图片
        self.destroy_images.extend([pygame.image.load("image/enemy2_down1.png"),
                                    pygame.image.load("image/enemy2_down2.png"),
                                    pygame.image.load("image/enemy2_down3.png"),
                                    pygame.image.load("image/enemy2_down4.png")])

        self.energy = MidEnemy.energy
        self.image_hit = pygame.image.load("image/enemy2_hit.png")
        self.hit = False


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        energy = 5
        self.active = True
        self.hit = False
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width),  # 定义敌机出现位置
                                         random.randint(-10 * self.rect.height, -self.rect.height)  # 保证敌机不会再程序开始就出现
                                         )

class BigEnemy(pygame.sprite.Sprite):
    energy = 15
    def __init__(self,background_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("image/enemy3_n1.png")
        self.image2= pygame.image.load("image/enemy3_n2.png")
        self.rect = self.image1.get_rect()
        self.mask = pygame.mask.from_surface(self.image1)
        self.mask = pygame.mask.from_surface(self.image2)
        self.width, self.height = background_size[0], background_size[1]
        self.speed = 0.5
        self.active = True

        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width),  # 定义敌机出现位置
                                         random.randint(-15 * self.rect.height, -5 * self.rect.height)  # 保证敌机不会再程序开始就出现
                                         )

        self.destroy_images = []  # 加载飞机损毁图片
        self.destroy_images.extend([pygame.image.load("image/enemy3_down1.png"),
                                    pygame.image.load("image/enemy3_down2.png"),
                                    pygame.image.load("image/enemy3_down3.png"),
                                    pygame.image.load("image/enemy3_down4.png"),
                                    pygame.image.load("image/enemy3_down5.png"),
                                    pygame.image.load("image/enemy3_down6.png")])

        self.energy = BigEnemy.energy
        self.image_hit = pygame.image.load("image/enemy3_hit.png")
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.hit = False
        self.rect.left, self.rect.top = (random.randint(0, self.width - self.rect.width),  # 定义敌机出现位置
                                         random.randint(-15 * self.rect.height, -5 * self.rect.height)  # 保证敌机不会再程序开始就出现
                                         )
