#coding:utf-8
import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self,background_size):
        pygame.sprite.Sprite.__init__(self)          #关于self与_init_的用法 ?

        self.image1=pygame.image.load("image/hero1.png")    #加载飞机图片1
        self.rect = self.image1.get_rect()         #得到当前我方飞机位置
        self.width,self.height = background_size[0],background_size[1]    #本地化背景图片的尺寸
        self.rect.left,self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        #定义飞机初始化位置，底部预留60像素
        self.speed = 10  # 设置飞机移动速度
        self.image1 = pygame.image.load("image/hero1.png")
        self.image2 = pygame.image.load("image/hero2.png")
        self.mask = pygame.mask.from_surface(self.image1)
        self.mask = pygame.mask.from_surface(self.image2)
        self.active = True

        #加载撞毁画面
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("image/hero_blowup_n1.png"),
                                    pygame.image.load("image/hero_blowup_n2.png"),
                                    pygame.image.load("image/hero_blowup_n3.png"),
                                    pygame.image.load("image/hero_blowup_n4.png"),])

    def move_up(self):
        if self.rect.top > 0:       #?飞机尚未飞出背景边缘位置
            self.rect.top -= self.speed
        else:                        #如果飞出去，，及时纠正背景边缘位置
            self.rect.top = 0

    def move_down(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def move_right(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        self.active = True