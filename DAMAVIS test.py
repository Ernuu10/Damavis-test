# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:45:46 2023

@author: ernu1
"""

class cell:
    def __init__(self, condition):
        self.block = condition
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False
    
class maze():
    def __init__(self,labyrinth_map):
        self.maze = []
        self.rows = len(labyrinth_map)
        self.columns = len(labyrinth_map[0])
        self.dictionari={}
        self.minimum = float('inf')
        
        for line in labyrinth_map:
            temp = []
            for value in line:
                temp.append(cell(value))
            
            self.maze.append(temp.copy())
            
        for x in range(self.rows):
            for y in range(self.columns):
                node = self.maze[x][y]
                if x != 0:
                    node.top = self.maze[x-1][y]
                if x != (self.rows - 1):
                    node.bottom = self.maze[x+1][y]
                if y != 0:
                    node.left = self.maze[x][y-1]
                if y != (self.columns - 1):
                    node.right = self.maze[x][y+1]
        if self.maze[0][0].block == "#":
            print('Entrance blocked')
        if self.maze[-1][-1].block == "#":
            print('Exit blocked')
            
    def check_position(self,x,y,orientation, rotation=False):
        if orientation == "h" or rotation:
            if y <= 0 or y >= (self.columns - 1) or x >= self.rows or x <0:
                return False
            if self.maze[x][y].block == "#" or self.maze[x][y-1].block == "#" or self.maze[x][y+1].block == "#":
                return False
            if not rotation:
                return True
        if orientation == "v" or rotation:
            if x <= 0 or x >= (self.rows - 1) or y >= self.columns or y < 0:
                return False
            if self.maze[x][y].block == "#" or self.maze[x-1][y].block == "#" or self.maze[x+1][y].block == "#":
                return False
            if not rotation:
                return True  
        if self.maze[x-1][y-1].block == "#" or self.maze[x-1][y+1].block == "#" or self.maze[x-1][y+1].block == "#" or self.maze[x+1][y+1].block == "#":
            return False
        return True
    
    def check_end(self, x, y):
        if (x == (self.rows-1) and y == (self.columns-2)) or (x == (self.rows-2) and y == (self.columns-1)):
            return True
        return False
    def step_dictionari(self, step, steps):
        
        if steps -1 > self.minimum:
            return False
        if step in self.dictionari.keys():
            if self.dictionari[step] > steps:
                self.dictionari[step], steps
                return True
            return False
        else:
            self.dictionari[step] = steps
            return True
        
def iterator(maze,steps,x,y,orientation,last_move,has_rotated=False):
    if maze.check_position(x, y, orientation,has_rotated):
        step_made = str(x)+","+str(y)+"," + orientation 
        if maze.step_dictionari(step_made, len(steps)):
            steps.append(step_made)
            if maze.check_end(x,y):
                # for step in steps:
                #     print(step)
                    
                # print("Total Steps: ", len(steps) -1)
                if maze.minimum > len(steps)-1:
                    maze.minimum = len(steps)-1
                return len(steps)-1
            else:               
                if has_rotated:
                    if last_move == "right":
                        iterator(maze, steps.copy(), x, y-1, orientation, "right")
                        iterator(maze, steps.copy(), x-1, y, orientation, "down")
                        iterator(maze, steps.copy(), x+1, y, orientation, "up")
                    elif last_move == "left":
                        iterator(maze, steps.copy(), x, y+1, orientation, "left")
                        iterator(maze, steps.copy(), x-1, y, orientation, "down")
                        iterator(maze, steps.copy(), x+1, y, orientation, "up")
                    elif last_move == "down":
                        iterator(maze, steps.copy(), x-1, y, orientation, "down")
                        iterator(maze, steps.copy(), x, y+1, orientation, "left")
                        iterator(maze, steps.copy(), x, y-1, orientation, "right")
                    elif last_move == "up":
                        iterator(maze, steps.copy(), x+1, y, orientation, "up")
                        iterator(maze, steps.copy(), x, y+1, orientation, "left")
                        iterator(maze, steps.copy(), x, y-1, orientation, "right")
                    else:
                        iterator(maze, steps.copy(), x-1, y, orientation, "down")
                        iterator(maze, steps.copy(), x+1, y, orientation, "up")
                        iterator(maze, steps.copy(), x, y+1, orientation, "left")
                        iterator(maze, steps.copy(), x, y-1, orientation, "right")
                else:
                    if orientation == "h":
                        orientation2 = "v"
                    else:
                        orientation2 = "h"
                    if last_move == "right":
                        iterator(maze, steps.copy(), x, y-1, orientation, "right")
                        iterator(maze, steps.copy(), x-1, y, orientation, "down")
                        iterator(maze, steps.copy(), x+1, y, orientation, "up")
                        iterator(maze, steps.copy(), x, y, orientation2, False,has_rotated = True)
                    elif last_move == "left":
                        iterator(maze, steps.copy(), x, y+1, orientation, "left")
                        iterator(maze, steps.copy(), x-1, y, orientation, "down")
                        iterator(maze, steps.copy(), x+1, y, orientation, "up")
                        iterator(maze, steps.copy(), x, y, orientation2, False,has_rotated = True)
                    elif last_move == "down":
                        iterator(maze, steps.copy(), x-1, y, orientation, "down")
                        iterator(maze, steps.copy(), x, y+1, orientation, "left")
                        iterator(maze, steps.copy(), x, y-1, orientation, "right")
                        iterator(maze, steps.copy(), x, y, orientation2, False,has_rotated = True)
                    elif last_move == "up":
                        iterator(maze, steps.copy(), x+1, y, orientation, "up")
                        iterator(maze, steps.copy(), x, y+1, orientation, "left")
                        iterator(maze, steps.copy(), x, y-1, orientation, "right")
                        iterator(maze, steps.copy(), x, y, orientation2, False,has_rotated = True)
                
                    else:
                        iterator(maze, steps.copy(), x-1, y, orientation, "down")
                        iterator(maze, steps.copy(), x+1, y, orientation, "up")
                        iterator(maze, steps.copy(), x, y+1, orientation, "left")
                        iterator(maze, steps.copy(), x, y-1, orientation, "right")
        else:
            return float('inf')
    else:
        return float('inf')
    
    
def solution(labyrinth):
    lab_map = maze(labyrinth)
    iterator(lab_map, [],0,1,'h',False)
    iterator(lab_map, [],1,0,'v',False)
    print("\n - Labyrinth")
    for row in labyrinth:
        print(row)
    if lab_map.minimum == float('inf'):
        print("\nMinimum steps required to complete the labyrinth: -1")
    else:
        print("\nMinimum steps required to complete the labyrinth: ", lab_map.minimum)
    return






print("----- SOLUTION EVALUATION ----")
print("\n TEST 1:\n")
labyrinth =  [[".",".",".",".",".",".",".",".","."], 
              ["#",".",".",".","#",".",".",".","."], 
              [".",".",".",".","#",".",".",".","."], 
              [".","#",".",".",".",".",".","#","."], 
              [".","#",".",".",".",".",".","#","."]] 
solution(labyrinth)
print("\n TEST 2:\n")
labyrinth =  [[".",".",".",".",".",".",".",".","."], 
              ["#",".",".",".","#",".",".","#","."], 
              [".",".",".",".","#",".",".",".","."], 
              [".","#",".",".",".",".",".","#","."], 
              [".","#",".",".",".",".",".","#","."]] 
solution(labyrinth)
print("\n TEST 3:\n")
labyrinth =  [[".",".","."], 
              [".",".","."], 
              [".",".","."]] 
solution(labyrinth)
print("\n TEST 4:\n")
labyrinth = [[".",".",".",".",".",".",".",".",".","."], 
             [".","#",".",".",".",".","#",".",".","."], 
             [".","#",".",".",".",".",".",".",".","."], 
             [".",".",".",".",".",".",".",".",".","."], 
             [".",".",".",".",".",".",".",".",".","."], 
             [".","#",".",".",".",".",".",".",".","."], 
             [".","#",".",".",".","#",".",".",".","."], 
             [".",".",".",".",".",".","#",".",".","."], 
             [".",".",".",".",".",".",".",".",".","."], 
             [".",".",".",".",".",".",".",".",".","."]] 
solution(labyrinth)

