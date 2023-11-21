import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #練習1：背景画像Surfaceの生成
    bg_img2 =  pg.transform.flip(bg_img, True, False) #演習2:背景画像を左右反転
    kk_img = pg.image.load("ex01/fig/3.png") #練習2:こうかとん画像Surfaceの生成
    kk_img = pg.transform.flip(kk_img, True, False) #練習2:こうかとんを左右反転
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 5, 1.0), pg.transform.rotozoom(kk_img, 10, 1.0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200 #練習6:動く背景画像
        screen.blit(bg_img, [-x, 0]) #練習4：背景画像の表示
        screen.blit(bg_img2, [1600-x, 0]) #練習6:動く背景画像
        screen.blit(bg_img, [3200-x, 0]) #演習2：連続な背景画像
        
        ten_times = int(tmr/10)
        if ten_times%2==1: screen.blit(kk_imgs[1], [300, 200])
        else: screen.blit(kk_imgs[ten_times%4], [300, 200]) #練習5:こうかとんはばたく
        
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()