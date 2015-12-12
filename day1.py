#!/usr/bin/python

position = 0
step = 0
firstbasement = 0
with open('./day1input', 'r') as infile:
    while True:
        char = infile.read(1)
        step += 1
	if not char:
            break
        if char == '(':
            position += 1
        elif char == ')':
            position -= 1
	if position < 0 and firstbasement == 0:
	    firstbasement = step
        print 'step %s\npos %s' % (step, position)
    print 'first into basement %s' % firstbasement

