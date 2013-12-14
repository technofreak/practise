__author__ = 'Parthan'

"""Write a class UpperCaseFile that takes a file as argument and behaves like a file, but returns all the contents in
upper case"""

class UppercaseFile:
    def __init__(self, fileobj):
        self.file = fileobj

    def readlines(self):
        return [text.upper() for text in self.file.readlines()]

    def read(self):
        return self.file.read().upper()

    def readline(self):
        return self.file.readline().upper()

    def seek(self, idx):
        self.file.seek(idx)

def main():
    filename = "F:\\test.txt"
    ucf = UppercaseFile(open(filename))
    print ucf.readlines()
    ucf.seek(0)
    print ucf.read()
    ucf.seek(0)