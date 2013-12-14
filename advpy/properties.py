__author__ = 'Parthan'

import re
from datetime import date

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self._phone = "0000000000"

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname

    def get_phone(self):
        return self._phone

    def set_phone(self, value):
        if not re.match("^[0-9-]+$"):
            raise ValueError("Not a valid phone number.")
        self._phone = value

# Problem: Add url property to the following class. The url of a post should be of the form
# /yyyy/mm/dd/title-with-spaces-replaced-with-hyphens"""

class Post(object):
    def __init__(self, year, month, day, title):
        self.year = year
        self.month = month
        self.day = day
        self.title = title

    @property
    def url(self):
        post_date = date(self.year, self.month, self.day).strftime("/%Y/%m/%d")
        post_title = '-'.join(self.title.split())
        return "%s/%s" % (post_date, post_title)

def main():
    p = Post(2013, 12, 14, 'the fourteenth of december')
    print p.url