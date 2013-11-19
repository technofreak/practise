__author__ = 'Parthan'

"""Cipher Map
Help Sofia write a decrypter for the passwords that Nikola will encrypt through the cipher map. A cipher grille is a 4 ×
 4 square of paper with four windows cut out. Placing the grille on a paper sheet of the same size, the encoder writes
down the first four symbols of his password inside the windows (see fig. below). After that, the encoder turns the
grille 90 degrees clockwise. The symbols written earlier become hidden under the grille and clean paper appears inside
the windows. The encoder then writes down the next four symbols of the password in the windows and turns the grille 90
degrees again. Then, they write down the following four symbols and turns the grille once more. Lastly, they write down
the final four symbols of the password. Without the same cipher grille, it is difficult to discern the password from
the resulting square comprised of 16 symbols. Thus, the encoder can be confident that no hooligan will easily gain
access to the locked door.

Write a module that enables the robots to easily recall their passwords through codes when they return home.

"""

def checkio(inpt):
    password = ''
    grill, text = inpt
    for i in range(len(grill)):
        newpassword = getpassword([grill, text])
        password += newpassword
        grill = rotate90(grill)
        print i, newpassword, password, grill
    return password

def getpassword(inpt):
    grill, text = inpt
    password = ''
    for index, seq in enumerate(grill):
        for idx, char in enumerate(seq):
            if char == "X":
                password += text[index][idx]
    return password

def rotate90(grill):
    res = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    inpt = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for index, seq in enumerate(grill):
        for idx, char in enumerate(seq):
            if char == 'X':
                inpt[index][idx] = 1
    res = zip(*inpt)
    res = [list(seq) for seq in res]
    for i in xrange(len(res)):
        res[i].reverse()
    for indx, grp in enumerate(res):
        temp = ''.join([str(i) for i in grp])
        temp = temp.replace('0', '.').replace('1', 'X')
        res[indx] = temp
    return res

if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
    print('All ok')
