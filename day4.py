#!/usr/bin/python
from hashlib import md5

def main():
    key = 'yzbqklnj'
    num = 0
    while md5(key+str(num)).hexdigest()[0:6] != '000000':
        num += 1
    print num

if __name__ == "__main__":
    main()