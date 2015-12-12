#!/usr/bin/python

def vowel_count(s):
    n = 0
    v = ['a','e','i','o','u']
    for i in range(0,len(s)):
        if s[i] in v:
            n += 1
    return n

def double_chars(s):
    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def double_char_pairs(s):
    for i in range(0,len(s)-2):
        if s.count(s[i:i+2]) > 1:
            #print 'dub %s: %s' % (s,s[i:i+2])
            return True
    return False

def repeats_sep_by_char(s):
    for i in range(0,len(s)-2):
        if s[i] == s[i+2]:
            #print 'rep %s: %s' % (s,s[i:i+3])
            return True
    return False

def bad_strings(s):
    bad_str = ['ab', 'cd', 'pq', 'xy']
    if any([x in s for x in bad_str]):
        return True
    else:
        return False

def main():
    nice = []
    naughty_vowel = []
    naughty_double = []
    naughty_string = []
    total = 0
    with open('./day5input','r') as infile:
        print 'rule1'
        for line in infile:
            if vowel_count(line) < 3:
                naughty_vowel.append(line)
            elif not double_chars(line):
                naughty_double.append(line)
            elif bad_strings(line):
                naughty_string.append(line)
            else:
                nice.append(line)
        print str(len(nice)) + str(nice)
        print str(len(naughty_vowel)) + str(naughty_vowel)
        print str(len(naughty_double)) + str(naughty_double)
        print str(len(naughty_string)) + str(naughty_string)
        nice = []
        naughty_doublechar = []
        naughty_repeats = []
        print 'rule2'
    with open('./day5input','r') as infile:
        for line in infile:
            if not double_char_pairs(line):
                naughty_doublechar.append(line)
            elif not repeats_sep_by_char(line):
                naughty_repeats.append(line)
            else:
                nice.append(line)
        print 'nice' + str(len(nice)) + str(nice)
        print 'naughty doubles' + str(len(naughty_doublechar)) + str(naughty_doublechar)
        print 'naughty repeats' + str(len(naughty_repeats)) + str(naughty_repeats)

if __name__ == "__main__":
    main()