import math
import pygame
from queue import PriorityQueue
from collections import deque
from queue import Queue

def h(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	return abs(x1-x2) + abs(y1-y2)


def reconstruct_path(came_from,current,draw):
	while(current in came_from):
		current = came_from[current]
		current.make_path()
		draw()


def dijktra(draw, grid, start, end):
	open_set = PriorityQueue()
	open_set.put((0,start))
	came_from = {}
	dis = {spot : float("inf") for row in grid for spot in row}
	dis[start] = 0

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		current = open_set.get()[1]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from,end,draw)
			end.make_end()
			start.make_start()
			return True
		
		if current != start:
			current.make_closed()
		
		for neighbor in current.neighbors:
			if (dis[current] + 1 < dis[neighbor]):
				came_from[neighbor] = current
				dis[neighbor] = dis[current] + 1
				
				if neighbor not in open_set_hash:
					open_set.put((dis[neighbor],neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()
				
		draw()	
	return False

def bfs(draw, grid, start, end):
	q = Queue(maxsize = 10000)
	q.put(start)
	came_from = {}
	open_set_hash = {start}

	while q.qsize()!= 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		current = q.get()
		
		if current == end:
			reconstruct_path(came_from,end,draw)
			end.make_end()
			start.make_start()
			return True
		
		if(current!=start):
			current.make_closed()
		
		for neighbor in current.neighbors:
			if neighbor not in open_set_hash:
				q.put(neighbor)
				open_set_hash.add(neighbor)
				came_from[neighbor] = current
				neighbor.make_open()
				
		draw()
	return False

def dfs(draw, grid, start, end):
	q = deque()
	q.append(start)
	came_from = {}
	open_set_hash = {start}
	
	while len(q)!= 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		current = q.pop()
		
		if current == end:
			reconstruct_path(came_from,end,draw)
			end.make_end()
			start.make_start()
			return True
		
		if(current!=start):
			current.make_open()
		
		for neighbor in current.neighbors:
			if neighbor not in open_set_hash:
				q.append(neighbor)
				open_set_hash.add(neighbor)
				came_from[neighbor] = current
				
		draw()

	return False

def Astar(draw, grid, start, end):
	open_set = PriorityQueue()
	count = 0
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot : float("inf") for row in grid for spot in row}
	g_score[start] = 0

	f_score = {spot : float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(),end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from,end,draw)
			end.make_end()
			start.make_start()
			return True
		
		if current != start:
			current.make_closed()
		
		for neighbor in current.neighbors:
			if (g_score[current] + 1 < g_score[neighbor]):
				came_from[neighbor] = current
				g_score[neighbor] = g_score[current] + 1
				f_score[neighbor] = g_score[current] + 1 + h(neighbor.get_pos(),end.get_pos())
				
				if neighbor not in open_set_hash:
					count+=1
					open_set.put((f_score[neighbor],count,neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()
				
		draw()
		
	return False
