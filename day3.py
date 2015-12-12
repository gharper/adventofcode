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