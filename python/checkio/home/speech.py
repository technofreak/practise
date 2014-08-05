def checkio(number):
    revnumber = str(number)[::-1]
    result = ''

    def getDenom(index):
        return ['', '', ' hundred', ' thousand'][index]


    #        if denom == 1:
    #            res = numbers[word][1]
    #        else:
    #            res = numbers[word][0]
    #        if denom not in [0, 1] and res:
    #            res += getDenom(denom)
    #        return res
    #
    #    for index, word in enumerate(revnumber):
    #        txt = getWord(word, index)
    #        result = (txt and (index and txt+' ') or txt) + result

    def getWord(word, type):
        numbers = {'0':['','',''],
                   '1':['one','ten', 'eleven'],
                   '2':['two','twenty', 'twelve'],
                   '3':['three','thirty', 'thirteen'],
                   '4':['four','forty', 'fourteen'],
                   '5':['five','fifty', 'fifteen'],
                   '6':['six','sixty', 'sixteen'],
                   '7':['seven','seventy', 'seventeen'],
                   '8':['eight','eighty','eighteen'],
                   '9':['nine','ninety','nineteen'],
                   }
        return numbers[word][type]

    for index, word in enumerate(revnumber):
        res = ''
        if index==0 and (len(revnumber)>1 and revnumber[1]=='1'):
            res = getWord(word, 2)
        elif index==1 and revnumber[1]=='1':
            continue
        elif index==1:
            res = getWord(word, 1)
        else:
            res = getWord(word, 0)
        if index not in [0,1] and res:
            res += getDenom(index)
        if index==1 and revnumber[0]!='0':
            res += ' '
        elif index==2 and (revnumber[1]!='0' and revnumber[0]!='0'):
            res += ' '
        elif index==3 and (revnumber[2]!='0' and revnumber[1]!='0' and revnumber[0]!='0'):
            res += ' '
        result = res + result

    return result

if __name__ == "__main__":
    #number = 3002
    #print number, "==", checkio(number)
    assert checkio(4) == 'four', ("First", checkio(4))
    assert checkio(133) == 'one hundred thirty three', ("Second", checkio(133))
    assert checkio(12)=='twelve', ("Third", checkio(12))
    assert checkio(101)=='one hundred one', ("Fifth", checkio(101))
    assert checkio(212)=='two hundred twelve', "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"

    print 'All ok'