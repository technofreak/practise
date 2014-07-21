__author__ = 'Parthan'

"""Striped Words

Our robots are always working to build their linguistic skills. For this mission, they are researching the latin
alphabet and its applications.

The alphabet contains both vowel and consonant letters (Yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with various different words. These words are separated by whitespaces and punctuation
marks. Numbers are not considered words in this mission (a mix of letters and digits is not a word too). You should
count the number of words (striped words) where the vowels with consonants are alternating, that is; words that you
count cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- do
not count it. Case is not significant for this mission.

"""

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    res = []

    def check(word):
        if not word or len(word) == 1:
            return False
        if not word[len(word)-1].isalpha():
            word = word[:-1]
        if not word.isalpha():
            return False
        for idx in xrange(len(word)-1):
            if word[idx].upper() in VOWELS:
                if word[idx+1].upper() in VOWELS:
                    return False
            else:
                if word[idx+1].upper() in CONSONANTS:
                    return False
        return True

    #for word in [word.strip(',').strip('.') for word in text.split() if word.strip(',').strip('.').isalpha()]:
    textlist = [ptext for stext in text.split() for ctext in stext.split(',') for ptext in ctext.split('.')]
    for word in textlist:
        if check(word):
            res.append(word)
    return len(res)

if __name__ == '__main__':
    assert checkio(u"My name is ...") == 2, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"