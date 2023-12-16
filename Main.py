import pygame
from Algorithms import *
from Spot import *
from Utility import *

WIDTH = 720
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Algorithms: Press \'D\' for DFS, \'B\' for BFS, \'A\' for Astar, \'K\' for Dijktra")

def main(win,width):
	ROWS = 40 #Change the grid dimension here
	grid = make_grid(ROWS,width)

	start = None
	end = None
	run = True
	started = False

	while(run):
		draw(win,grid,ROWS,width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			
			pos = pygame.mouse.get_pos()
			row,col = get_clicked_pos(pos,ROWS,width)
			spot = grid[row][col]

			if pygame.mouse.get_pressed()[0]:

				if not start and spot!=end:
					start = spot
					start.make_start()
				
				elif not end and spot!=start:
					end = spot
					end.make_end()
				
				elif spot != end and spot!=start:
					spot.make_barrier()


			elif pygame.mouse.get_pressed()[2]:
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS,width)
				
				if event.key == pygame.K_k and start and end:
					update_grid(grid)
					dijktra(lambda : draw(win,grid,ROWS,width), grid, start, end)
				
				if event.key == pygame.K_d and start and end:
					update_grid(grid)
					dfs(lambda : draw(win,grid,ROWS,width), grid, start, end)
				
				if event.key == pygame.K_b and start and end:
					update_grid(grid)
					bfs(lambda : draw(win,grid,ROWS,width), grid, start, end)
				
				if event.key == pygame.K_a and start and end:
					update_grid(grid)
					Astar(lambda : draw(win,grid,ROWS,width), grid, start, end)

	pygame.quit()

main(WIN,WIDTH)
