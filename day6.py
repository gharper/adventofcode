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

'''--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?

Your puzzle answer was 543903.

--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.'''