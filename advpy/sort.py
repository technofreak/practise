__author__ = 'Parthan'

"""Write a function to sort given names without considering the case"""


def isorted(element):
    def lowerof(item):
        #return item[0].lower()+item[1:]
        return item.lower()
    return sorted(element, key=lowerof)
    #return sorted(element, lambda: x.lower())

if __name__ == "__main__":
    test = ['C', 'c++', 'Python', 'perl', 'java']
    print isorted(test)