__author__ = 'Parthan'

import fileinput, sys
from fractions import gcd

if __name__ == "__main__":
    tc = 0
    for line in fileinput.input():
        if not tc:
            tc = line
            continue
        a, b = line.strip().split()
        curra, currb = a, b
        currplayer = 'a'
        while curra != 1 or currb != 1:
            res = gcd(curra, currb)
            if res == 1:
                if currplayer == 'a':
                    currb -= 1
                else:
                    curra -= 1
                continue
            else:
                if currplayer == 'a':
                    currb -= 1
                    currb = int(currb / res) or 1
                else:
                    curra -= 1
                    curra = int(curra / res) or 1
        sys.stdout.write(curra == 1 and 'Chandu Don' or 'Arjit')