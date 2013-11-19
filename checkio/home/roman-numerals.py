__author__ = 'Parthan'

"""Convert Number to Roman Numerals

Symbol Value:
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)

Reference: http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
"""

def checkio(data):
    nos = len(str(data))
    res = ''

    def handler(num, place):
        num = int(num)
        if num <= 3:
            if place == 4:
                return 'M'*num
            elif place == 3:
                return 'C'*num
            elif place == 2:
                return 'X'*num
            else:
                return 'I'*num
        elif num == 4:
            if place == 3:
                return 'CD'
            elif place == 2:
                return 'XL'
            else:
                return 'IV'
        elif num == 5:
            if place == 3:
                return 'D'
            elif place == 2:
                return 'L'
            else:
                return 'V'
        elif num <=8:
            if place == 3:
                return 'D'+('C'*(num-5))
            elif place == 2:
                return 'L'+('X'*(num-5))
            else:
                return 'V'+('I'*(num-5))
        elif num == 9:
            if place == 3:
                return 'CM'
            if place == 2:
                return 'XC'
            else:
                return 'IX'

    for pos, num in enumerate(str(data)):
        res += handler(num, nos-pos)
    return res

if __name__ == "__main__":
    assert checkio(9) == 'IX', 'ones'
    assert checkio(64) == 'LXIV', 'tens'
    assert checkio(854) == 'DCCCLIV', 'hundreds'
    assert checkio(3999) == 'MMMCMXCIX', 'thousands'
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'