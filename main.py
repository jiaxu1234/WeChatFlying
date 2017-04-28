#coding:utf-8
import pygame
import sys
import traceback
from random import *
from pygame.locals import *
import  myplane
import enemy
import bullet
#==============初始化=================
pygame.init()
pygame.mixer.init()     #声音控制对象初始化
background_size = width,height = 480,650
screen = pygame.display.set_mode(background_size)
pygame.display.set_caption("Aircraft War-JX")
background = pygame.image.load("image/background.png")
#============加载各种音频文件=============
pygame.mixer.music.load("sound/game_music.wav")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
big_enemy_flying_sound = pygame.mixer.Sound("sound/big_spaceship_flying.wav")
big_enemy_flying_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.2)
me_down_sound = pygame.mixer.Sound("sound/game_over.wav")
me_down_sound.set_volume(0.2)
button_down_sound = pygame.mixer.Sound("sound/button.wav")
button_down_sound.set_volume(0.2)
level_up_sound = pygame.mixer.Sound("sound/achievement.wav")
level_up_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_double_laser.wav")
get_bullet_sound.set_volume(0.2)

def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1 = enemy.SmallEnemy(background_size)
        group1.add(e1)
        group2.add(e1)
def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(background_size)
        group1.add(e2)
        group2.add(e2)
def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(background_size)
        group1.add(e3)
        group2.add(e3)

#===================实例化敌方飞机========
enemies = pygame.sprite.Group()#生成敌方飞机组
small_enemies = pygame.sprite.Group()#敌方小型飞机组
add_small_enemies(small_enemies, enemies,1)#生成若干敌方小型飞机
mid_enemies = pygame.sprite.Group()#敌方中型飞机组
add_mid_enemies(mid_enemies, enemies,1)
big_enemies = pygame.sprite.Group()
add_big_enemies(big_enemies, enemies,1)

def main():
    import enemy
    score = 0
    pygame.mixer.music.play(-1)
    running = True
    me = myplane.MyPlane(background_size)  # 生成我方飞机
    clock = pygame.time.Clock()  # 设置频率
    switch_image = False  # 控制飞机切换标志位
    delay = 60

    # ====================飞机损毁图像索引====================
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    #============子弹精灵索引，生成普通子弹====================
    bullet1 = []
    bullet1_index = 0
    bullet1_num = 6   #定义子弹实例化个数
    for i in range(bullet1_num):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

#==============定义颜色
    color_black = (0,0,0)
    color_green = (0,255,0)
    color_red = (255,0,0)
    color_white = (255,255,255)

    #============显示分数===============
    score_font = pygame.font.SysFont("arial",48)

    while running:
        #====绘制分数==========
        score_text = score_font.render("Score : %s" % str(score), True, color_white)
        screen.blit(score_text, (10, 5))

        screen.blit(background,(0,0))

        clock.tick(60)  # 设置帧数为60

        if not delay % 3:
            switch_image = not switch_image
        if switch_image:
            screen.blit(me.image1,me.rect)     #绘制我方飞机的两种不同形式
        else:
            screen.blit(me.image2,me.rect)

        # 显示子弹
        if not (delay % 10):  # 每十帧发射一颗移动的子弹
            bullet_sound.play()
            bullets = bullet1
            bullets[bullet1_index].reset(me.rect.midtop)
            bullet1_index = (bullet1_index + 1) % bullet1_num

        # 子弹与敌机的碰撞检测
        for b in bullets:
            if b.active:
                b.move()
                screen.blit(b.image, b.rect)
                enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                for e in enemies_hit:
                    if e in mid_enemies or e in big_enemies:
                        e.energy -= 1
                        e.hit = True
                        if e.energy == 0:
                            e.active = False
                    else:
                        e.active = False  # 小型飞机坠毁

        for each in small_enemies:
            each.move()
            screen.blit(each.image,each.rect)

        for each in mid_enemies:
            if each.active:
                each.move()
                if not each.hit:
                    screen.blit(each.image, each.rect)
                else:
                    screen.blit(each.image_hit, each.rect)
                    each.hit = False
    # ==============绘制血槽======================================

                pygame.draw.line(screen, color_black, (each.rect.left, each.rect.top - 5),(each.rect.right, each.rect.top - 5), 2)
                energy_remain = each.energy / enemy.MidEnemy.energy
                if energy_remain > 0.2:
                    energy_color = color_green
                else:
                    energy_color = color_red
                pygame.draw.line(screen, energy_color, (each.rect.left, each.rect.top - 5),(each.rect.left + each.rect.width * energy_remain, each.rect.top - 5), 2)
            else:  # 意为已经撞了
                pass
        for each in big_enemies:
            if each.active:
                each.move()
                if not each.hit:
                    if switch_image:
                        screen.blit(each.image1, each.rect)  ##################坑
                    else:
                        screen.blit(each.image2, each.rect)
                else:
                    screen.blit(each.image_hit,each.rect)
                    each.hit = False
    #==============绘制血槽======================================

                pygame.draw.line(screen,color_black,(each.rect.left,each.rect.bottom - 10),(each.rect.right,each.rect.bottom - 10),2)
                energy_remain = each.energy/enemy.BigEnemy.energy
                if energy_remain > 0.2:
                    energy_color = color_green
                else:
                    energy_color = color_red
                pygame.draw.line(screen,energy_color,(each.rect.left,each.rect.bottom - 10),(each.rect.left + each.rect.width * energy_remain,each.rect.bottom - 10),2)
                if each.rect.bottom == -50:
                    big_enemy_flying_sound.play(-1)
            else:  #意为已经撞了
                pass

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.move_right()

        enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
        if enemies_down:  # 如果碰撞检测返回的列表非空，则说明已发生碰撞,若此时我方飞机处于无敌状态
            me.active = False
            for e in enemies_down:
                e.active = False  # 敌机损毁

        #我方飞机坠毁特效
        if me.active:  # 绘制我方飞机的两种不同的形式#
            pass
        else:
            me_down_sound.play()
            if not (delay % 3):
                screen.blit(me.destroy_images[me_destroy_index], me.rect)
                me_destroy_index = (me_destroy_index + 1) % 4
                if me_destroy_index == 0:
                    me.reset()



        #敌方小飞机坠毁特效
        for each in small_enemies:
            if each.active:
                pass
            else:
                if e1_destroy_index == 0:
                    enemy1_down_sound.play()
                if not (delay % 3):
                    screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                    e1_destroy_index = (e1_destroy_index + 1) % 4
                    if e1_destroy_index == 0:
                        score += 500
                        each.reset()

        #敌方中型飞机坠毁特效
        for each in mid_enemies:
            if each.active:
                pass
            else:
                if e2_destroy_index == 0:
                    enemy2_down_sound.play()
                    if not(delay % 3):
                        screen.blit(each.destroy_images[e2_destroy_index],each.rect)
                        e2_destroy_index = (e2_destroy_index + 1)%4
                        if e2_destroy_index == 0:
                            score += 1000
                            each.reset()
        # 敌方大型飞机坠毁特效
        for each in big_enemies:
            if each.active:
                 pass
            else:
                if e3_destroy_index == 0:
                    enemy3_down_sound.play()
                    if not (delay % 3):
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            score  += 3000
                            each.reset()





        pygame.display.flip()             #Update the full display Surface to the screen
        '''Python采用了一种双缓冲的屏幕刷新机制，
        即先通过blit（）函数将一个图片（统称为surface对象）绘制在内存中，
        最后统一用pygame.dis        play.flip()
        函数将绘制好的surface对象一次全部刷新到屏幕上。'''

        for event in pygame.event.get():     #相应用户偶然操作
            if event.type == QUIT:        #相应用户点击关闭按钮，退出程序
                pygame.quit()
                sys.exit()

        if delay == 0:   #延时
            delay = 60
        delay -=1

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()        #point
