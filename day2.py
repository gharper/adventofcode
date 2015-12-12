#!/usr/bin/python

l=w=h=box=total=totrib=0
with open('./day2input', 'r') as infile:
    for line in infile:
        box += 1
        l,w,h = [int(i) for i in line.split('x')]
        slack = int(min(l*w, w*h, h*l))
        area = 2*l*w + 2*w*h + 2*h*l + slack
        ribbon = 2*l+2*w+2*h-max(2*l,2*w,2*h)+l*w*h
        total += area
        totrib += ribbon
        print 'box{} l{} w{} h{} s{} a{}'.format(box,l,w,h,slack,area)
    print 'total %s' % total
    print 'ribbon %s' % totrib