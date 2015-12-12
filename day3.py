#!/usr/bin/python

class santa:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move_n(self):
        self.y += 1
        return self.x,self.y
    def move_s(self):
        self.y -= 1
        return self.x,self.y
    def move_e(self):
        self.x +=1
        return self.x,self.y
    def move_w(self):
        self.x -= 1
        return self.x,self.y
    def get_position(self):
        return self.x,self.y

def main():
    real_santa = santa(0,0)
    robo_santa = santa(0,0)
    houses = []
    step=0
    with open('./day3input', 'r') as infile:
        while True:
            move = infile.read(1)
            if not move: break
            if move == '^':
                if step % 2 == 0:
                    houses.append(real_santa.move_n())
                else:
                    houses.append(robo_santa.move_n())
            if move == 'v':
                if step % 2 == 0:
                    houses.append(real_santa.move_s())
                else:
                    houses.append(robo_santa.move_s())
            if move == '>':
                if step % 2 == 0:
                    houses.append(real_santa.move_e())
                else:
                    houses.append(robo_santa.move_e())
            if move == '<':
                if step % 2 == 0:
                    houses.append(real_santa.move_w())
                else:
                    houses.append(robo_santa.move_w())
            step += 1
    print len(set(houses))

if __name__ == "__main__":
    main()

'''
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
Your puzzle answer was 2592.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.'''