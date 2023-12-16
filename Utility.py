import pygame
from Spot import *

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i,j,gap,rows)
			grid[i].append(spot)
	
	return grid

def draw_grid(win,rows,width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap))
		for j in range(rows):
			pygame.draw.line(win,GREY,(j*gap,0),(j*gap,width))

def draw(win,grid,rows,width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)
	
	draw_grid(win,rows,width)
	pygame.display.update()

def get_clicked_pos(pos,rows,width):
	gap = width // rows
	y,x = pos

	row = y // gap
	col = x // gap

	return row,col

def update_grid(grid):
	for row in grid:
		for spot in row:
			spot.update_neighbors(grid)
