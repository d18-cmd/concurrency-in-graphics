import time
import sys,pygame
from pygame import gfxdraw

start_time = time.time()
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0,0,0))
pygame.display.flip()
white = (255,255,255)
file1 = open("points2.txt","w")

def midPoint(X1,Y1,X2,Y2):  
    dx = X2 - X1  
    dy = Y2 - Y1  
    d = dy - (dx/2)  
    x = X1 
    y = Y1  
    print(x,",",y,"\n") 
    while (x < X2): 
        x=x+1
        if(d < 0): 
            d = d + dy   
        else: 
            d = d + (dy - dx)  
            y=y+1
        print(x,",",y,"\n")
        t = "x: "+str(x)+" y: "+str(y)+"\n"
        gfxdraw.pixel(screen,x,y,white)
        file1.write(t)
  
if __name__=='__main__': 
    X1 = 2
    Y1 = 2
    X2 = 590
    Y2 = 510
    midPoint(X1, Y1, X2, Y2) 
    pygame.display.flip()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("simple mp divion algorithm")
    while 1:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT: sys.exit()

    file1.close()
