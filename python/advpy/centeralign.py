__author__ = 'Parthan'

"""Write a function make_centralign, that takes width as argument and returns a function that takes a string as argument
 and center align that
"""

def make_centeralign(width, sep=' '):
    def center(text):
        fill_width = width - len(text)
        fill_front = fill_width/2 + fill_width%2
        fill_back = fill_width/2
        return fill_front*sep + text + fill_back*sep
    return center

def main(text, width):
    return make_centeralign(width)(text)
