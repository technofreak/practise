__author__ = 'Parthan'

"""Morse Clock

Help Stephen to automate his task by creating a module. As you can see in below illustration, gray circle means on, and
white circle means off. Every digit in the time string contains a different number of slots. The first digit for the
hour has a length of 2 while the second digit for the hour has a length of 4. The first digits for the minute and second
 not have a length of 3 while the second digits for the minute and second have a length of 4. Every digit in the time is
  converted to binary representation. You will convert every on ( or 1 ) signal to dash ( - ) and every off ( or 0 )
  signal to dot ( . )

Illustration:

  HH : MM : SS
   . :  . :  .  > 8
   . : .- : -.  > 4
  .. : -- : ..  > 2
  -. : -- : .-  > 1
  ____________
  10 : 37 : 49

"""

def checkio(data):
    morse = {
        '0': '.',
        '1': '-',
        '2': '-.',
        '3': '--',
        '4': '-..',
        '5': '-.-',
        '6': '--.',
        '7': '---',
        '8': '-...',
        '9': '-..-',
    }
    hour, min, sec = [item.rjust(2, '0') for item in data.split(':')]
    mhour = ' '.join([morse[hour[0]].rjust(2,'.'), morse[hour[1]].rjust(4,'.')])
    mmin = ' '.join([morse[min[0]].rjust(3,'.'), morse[min[1]].rjust(4,'.')])
    msec = ' '.join([morse[sec[0]].rjust(3,'.'), morse[sec[1]].rjust(4,'.')])
    return " : ".join([mhour, mmin, msec])

if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
