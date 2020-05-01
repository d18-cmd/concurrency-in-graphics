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
def print_square1(X1,Y1,X2, Y2):  
	dx = X2 - X1 
	dy = Y2 - Y1 
	d = dy - (dx/2) 
	x = X1 
	y = Y1 
	while (x < X2): 
		x=x+1
		if(d < 0): 
			d = d + dy 
		else: 
			d = d + (dy - dx) 
			y=y+1
		print(x,y)
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
		print(x1,y1)
		t1 = threading.Thread(target=print_square1, args=(x1,y1,x2,y2,)) 
		t2 = threading.Thread(target=print_square1, args=(x2,y2,x3,y3,))
		t1.start() 
		t2.start()	 
		t1.join() 
		t2.join()		
		print("Done!") 
		pygame.display.flip()		
		print("--- %s seconds ---" % (time.time() - start_time))
		print("threading mp divion algorithm")
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
		file1.close()
