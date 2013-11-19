__author__ = 'Parthan'

"""Most Wanted Letter

You are given a text, which contains different english letters and punctuation symbols. You should find the most
frequent letter in the text. The letter returned must be in lower case.

While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make
sure you do not count punctuation symbols and whitespaces, only letters. If you have two or more letters with the same
frequency, then return the letter which comes first in the alphabet. (Ex: we have "b" and "f" as the most frequent, then
 return "b")
"""

def checkio(text):
    #chars = [char.lower() for char in text if char.isalpha()]
    #cnt = {ch: 0 for ch in set(chars)}
    #for ch in chars:
    #    cnt[ch] += 1
    #maxcnt = max(cnt.values())
    #maxch = [key for key, val in cnt.iteritems() if val == maxcnt]
    #maxch.sort()
    #return maxch[0]
    return max(set([char.lower() for char in text if char.isalpha()]), key=text.lower().count)

if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
