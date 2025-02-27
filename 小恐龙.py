import pygame # 将pygame库导入到Python程序中
import time
import random
import threading
SCREENWIDTH = 800 # 窗体宽度
SCREENHEIGHT = 260 # 窗体高度
pygame.init()
window = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
window.fill((255,255,255))
pygame.display.set_caption('小恐龙')
clock = pygame.time.Clock()

font = pygame.font.Font("D:\\halloworld\\python\\pygame\\picture2\\字魂狂傲行书(商用需授权).ttf",30) # 创建一个字体对象
image_konglong = pygame.image.load('D:\\halloworld\\python\\pygame\\图片\\u=3409403884,1794930412&fm=253&fmt=auto&app=138&f=PNG.jpg') # 加载恐龙图片
imgae_ditu = pygame.image.load('D:\\halloworld\python\\pygame\\图片\\未标题-5.jpg')
image_xianrenzhang = pygame.image.load('D:\\halloworld\\python\\pygame\\图片\\仙人掌.jpg')
image_yunduo = pygame.image.load('D:\\halloworld\\python\\pygame\\图片\\云朵.jpg')
image_gameover = pygame.image.load('D:\\halloworld\\python\\pygame\\图片\\a3caae54704fd26c8227c51aca9fa7d248bd675f.jpg')
#image_niao = pygame.image.load('D:\\halloworld\\python\\pygame\\图片\\niao.jpg')
use_image_konglong = pygame.transform.scale(image_konglong,(42,42))
use_image_ditu = pygame.transform.scale(imgae_ditu,(1110,375)) 
use_image_xianrenzhang = pygame.transform.scale(image_xianrenzhang,(25,47))    
use_image_yunduo = pygame.transform.scale(image_yunduo,(37,26))
use_image_gameover = pygame.transform.scale(image_gameover,(350,200))
#use_image_niao = pygame.transform.scale(image_niao,(47,47))
music = pygame.mixer.Sound('D:\halloworld\python\pygame\music\Lulleaux、Kid Princess - Empty Love.mp3')
class Konglong:
    def __init__(self):
        self.x = 0
        self.y = 90
        
    def konglongxianshi(self):
        window.blit(use_image_konglong, (self.x, self.y))
        pygame.display.update()
    def suaxin(self):
        pygame.draw.rect(window,(255,255,255),(self.x,self.y,42,42))
        pygame.display.update()
    def move_up(self):
        if self.y <= 90 and self.y > 40: # 如果站在地上 
            self.y = self.y - 50 # 以5个像素值向上移动
        window.blit(use_image_konglong, (self.x, self.y))
        pygame.display.update()
        
    def move_down(self):
        if self.y <=40 :
            self.y = 90
        window.blit(use_image_konglong, (self.x, self.y))
        pygame.display.update()

yun_place_list = [555,481,564,565,532,478,255,547,775,400,500,600,700,254,845,674]

score = 0              
x_very = 8
yun_x = 300
#niao_x = 600
map_x = 0
xainrenzhangn_x = 400
xainrenzhangn_x2 = 700
K = pygame.key.get_pressed()
l = Konglong()

pygame.display.flip()

GREEN=(0,200,0)
RED=(200,0,0)
SHALLOW_GREEN=(0,255,0)
SHALLOW_RED=(255,0,0)

def jisuyouxi(GREEN,RED):
    pygame.draw.rect(window, GREEN,(200,180,120,40))
    pygame.draw.rect(window, RED,(500,180,120,40))
    text1 = font.render('重新开始',True,(0,0,0))
    text2 = font.render('退出游戏',True,(0,0,0))
    window.blit(text1,(200,180))
    window.blit(text2,(500,180))
    

def jump():
    l.suaxin()
    l.move_up()
    time.sleep(0.5)
    l.suaxin()
    l.move_down()  
t_count = 0
state=0
#def gameover():
music.play(-1)
while True:
    
    clock.tick(30)
    text = font.render("SCORE: " + str(score), True,(0, 0, 0)) # 创建一个文本对象

    if t_count == 0:
        score += 1
        if xainrenzhangn_x < -25:
            xainrenzhangn_x = xainrenzhangn_x2 + random.randint(200,300)
        if xainrenzhangn_x2 < -25:
                xainrenzhangn_x2 = xainrenzhangn_x + random.randint(200,300)        
        if yun_x < -15:
            for i in range(random.randint(0,len(yun_place_list)-1)):
                yun_x = yun_place_list[i]
        window.blit(use_image_ditu,(map_x,-110))
        window.blit(use_image_ditu,(map_x+1110,-110))
        window.blit(use_image_xianrenzhang,(xainrenzhangn_x,86))
        window.blit(use_image_xianrenzhang,(xainrenzhangn_x2,86))
        window.blit(text,(0,0))
        window.blit(use_image_yunduo,(yun_x,0)) 
        l.konglongxianshi()
        map_x -= x_very
        xainrenzhangn_x -= x_very
        xainrenzhangn_x2 -= x_very
        yun_x -= x_very
        x_very += 0.0025
        if map_x < -500:
            map_x = 0
        pygame.display.update()
    if  xainrenzhangn_x <= 35 and l.y == 90 and xainrenzhangn_x >= -25:
        music.stop()
        t_count = 1 
        if (state==0):
            window.blit(use_image_gameover,(225,30))
            jisuyouxi(GREEN,RED)
            pygame.display.update()
    if xainrenzhangn_x2 <= 35 and l.y == 90 and xainrenzhangn_x2 >= -25:
        t_count = 1
        music.stop()
        if(state==0):
            window.blit(use_image_gameover,(225,30))
            jisuyouxi(GREEN,RED)
            pygame.display.update()
        
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                t1 = threading.Thread(target=jump)
                t1.start()
            if event.key == pygame.K_DOWN:
                l.move_down()
                l.suaxin()
                
            if event.key == pygame.K_RETURN and t_count == 1:
                music.play(-1)
                t_count = 0
                score = 0              
                yun_x = 300
                x_very = 8
                map_x = 0
                xainrenzhangn_x = 400
                xainrenzhangn_x2 = 600
                state=0
            
        elif event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            if t_count == 1 and 200 <= x <= 320 and 180 <= y <= 220:
                jisuyouxi(GREEN=SHALLOW_GREEN,RED=RED)
                pygame.display.update()
                state=1
            elif t_count == 1 and 500 <= x <= 620 and 180 <= y <= 220:
                jisuyouxi(GREEN=GREEN,RED=SHALLOW_RED)
                pygame.display.update() 
                state=1
            else:
                state=0
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            x,y = event.pos
            if t_count == 1 and 200 <= x <= 320 and 180 <= y <= 220:
                music.play(-1)
                t_count = 0
                score = 0              
                yun_x = 300
                x_very = 10
                map_x = 0
                xainrenzhangn_x = 400
                xainrenzhangn_x2 = 600
                state=0
            if t_count == 1 and 500 <= x <= 620 and 180 <= y <= 220:
                pygame.quit()
                exit()
                
            
        #time.sleep(5)
        #t = threading.Thread(target=gameover())
        #t.start()
#纪念一下第一次做出来的小游戏，简单复刻高中的小恐龙        
            
       
            
              
               
           