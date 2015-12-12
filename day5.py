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

'''--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

Your puzzle answer was 258.

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?'''