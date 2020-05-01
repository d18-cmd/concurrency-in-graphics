# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import time
import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0,0,0))
pygame.display.flip()

white = (255,255,255)

start_time = time.time()

file1 = open("points1.txt","w") 

def print_square1(x1,y1,x2, y2): 
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

if __name__ == "__main__": 
		x1 = 2
		y1 = 2
		x3 = 590
		y3 = 510
		x2=(x1+x3)/2
		y2=(y1+y3)/2
#		file1.write(str(x2)+" "+str(y2)+"\n")
		# creating thread 
		print(x1,y1)
		 
		t1 = threading.Thread(target=print_square1, args=(x1,y1,x2,y2,)) 
		t2 = threading.Thread(target=print_square1, args=(x2,y2,x3,y3,))
		# starting thread 1 
		
		t1.start() 
		t2.start()
		# starting thread 2 
		 

		# wait until thread 1 is completely executed 
		
		# wait until thread 2 is completely executed 
		 
		t1.join() 
		t2.join()		
		# both threads completely executed 
		print("Done!") 


		pygame.display.flip()
		
		print("--- %s seconds ---" % (time.time() - start_time))
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
		file1.close()
