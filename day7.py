#!/usr/bin/python

class light_grid(object):
    def __init__(self,x,y):
        self.grid = [[0 for row in range(x)] for col in range(y)]
    def on(self,x,y):
        self.grid[x][y] += 1
    def off(self,x,y):
        if self.grid[x][y] > 0:
            self.grid[x][y] -= 1
    def toggle(self,x,y):
        self.grid[x][y] += 2


def main():
    with open('./day7input', 'r') as infile:
        for line in infile:

if __name__ == "__main__":
    main()