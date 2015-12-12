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
    def count(self,n):
        return self.grid.count(n)
    def out(self):
        return self.grid
    def dims(self):
        return len(self.grid[1]),len(self.grid)

def main():
    lights = light_grid(1000,1000)
    print lights.dims()
    with open('./day6input', 'r') as infile:
        for line in infile:
            parse_line = line.split()
            if parse_line[0] == 'toggle':
                x1,y1 = parse_line[1].split(',')
                x2,y2 = parse_line[3].split(',')
                for x in range(int(x1),int(x2)+1):
                    for y in range(int(y1),int(y2)+1):
                        lights.toggle(int(x),int(y))
            elif parse_line[0] == 'turn':
                x1,y1 = parse_line[2].split(',')
                x2,y2 = parse_line[4].split(',')
                if parse_line[1] == 'on':
                    for x in range(int(x1),int(x2)+1):
                        for y in range(int(y1),int(y2)+1):
                            lights.on(x,y)
                elif parse_line[1] == 'off':
                    for x in range(int(x1),int(x2)+1):
                        for y in range(int(y1),int(y2)+1):
                            lights.off(x,y)
                else:
                    print 'ERR: ' + line
            else:
                print 'ERR: ' + line
    out = lights.out()
    light_count = 0
    for row in out:
        for val in row:
            #print '{}'.format(val),
            light_count += val
        #print
    print light_count


if __name__ == "__main__":
    main()