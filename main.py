import curses
from curses import wrapper
import queue
import time

maze = maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]
def print_maze(stdscr, maze, path=None):
    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            stdscr.addstr(i, j*2, cell, GREEN)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return (i, j)

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, []))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        if maze[row][col] == end:
            return path
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if (n_row, n_col) not in visited and maze[n_row][n_col] != "#":
                visited.add((n_row, n_col))
                new_path = path + [current_pos]
                q.put((neighbor, new_path))
                stdscr.addstr(n_row, n_col * 2, " ", curses.color_pair(1))
                stdscr.refresh()
                time.sleep(0.1)

def find_neighbors(maze,row,col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < len(maze) - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < len(maze[0]) - 1:
        neighbors.append((row, col + 1))
    
    return neighbors
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    green_and_black = curses.color_pair(1)
    stdscr.clear()
    print_maze(stdscr, maze)
    stdscr.refresh()
    stdscr.getch()  # Wait for user input to start

wrapper(main)