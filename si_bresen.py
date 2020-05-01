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

def midPoint(x1,y1,x2,y2):  
    m_new = 2 * (y2 - y1)  
    slope_error_new = m_new - (x2 - x1) 
  
    y=y1 
    for x in range(x1,x2+1):  
      
        print(x ,y )  
  
        # Add slope to increment angle formed  
        slope_error_new =slope_error_new + m_new  
  
        # Slope error reached limit, time to  
        # increment y and update slope error.  
        if (slope_error_new >= 0):  
            y=y+1
            slope_error_new =slope_error_new - 2 * (x2 - x1)
      

        # Plot intermediate points  
        # putpixel(x,y) is used to print pixel  
        # of line in graphics  
        print(x,",",y,"\n")
        t = "x: "+str(x)+" y: "+str(y)+"\n"
        gfxdraw.pixel(screen,x,y,white)
        file1.write(t)
      
  
# Driver program  
  
if __name__=='__main__': 
    	X1 = 2
    	Y1 = 2
    	X2 = 590
    	Y2 = 510
    	midPoint(X1, Y1, X2, Y2) 
    	pygame.display.flip()
    
    	print("--- %s seconds ---" % (time.time() - start_time))
    	while 1:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT: sys.exit()

    	file1.close()
