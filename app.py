#Lenar Troncoso
import sys, pygame

pygame.init()
size=800, 600
screen=pygame.display.set_mode(size)
pygame.display.set_caption("LenarBall")
width, height=800, 600
speed=[1, 1]
white=255, 255, 255
ball=pygame.image.load("ball.bmp")
ballrect=ball.get_rect()
bat=pygame.image.load("bat.bmp")
batrect=ball.get_rect()
batrect.move_ip(400, 500)

font = pygame.font.Font(None, 30)
fg = 0, 0, 0
bg = 255, 255, 255
cont=0

run=True
while run:
    pygame.time.delay(4)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: run=False
    #########
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        batrect=batrect.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        batrect = batrect.move(1, 0)
        ######
    if batrect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect=ballrect.move(speed)
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0:
        speed[1]=-speed[1]

    text="Score: "
    cont+=1
    ren = font.render(text+str(cont), 0, fg, bg)

    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(bat, batrect)
    screen.blit(ren, (10, 10))
    pygame.display.flip()
pygame.quit()
