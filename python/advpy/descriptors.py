__author__ = 'Parthan'

import re

class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self._phone = "00000000"

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname

    def get_phone(self):
        return self._phone

    def set_phone(self, value):
        if not re.match("^[ 0-9-]+$", value):
            raise ValueError("Invalid phone number: %r"% value)
        self._phone = value

    phone = property(get_phone, set_phone)

def tryperson():
    p = Person("Foo", "Bar")
    print p.fullname
    # descriptor
    print Person.fullname

class Constant(object):
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, type=None):
        print "Constant.__get__"
        return self.value

    def __set__(self, obj, value):
        raise  Exception("can't change a constant")

class Math(object):
    pi = Constant(3.14)

class Integer(object):
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, type=None):
        return self.value

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise Exception("Not an integer")
        self.value = value

class Number(object):
    val = Integer(0)

def test1():
    m = Math()
    print m.pi
    #m.pi = 1.1
    i = Number()
    print i.val
    i.val = 10
    print i.val
    i.val = 'apple'
    print i.val

class Foo(object):
    #@lazy_property
    def db(self):
        print "conntecting to database"
        return "dummy-descriptor"

class myproperty(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, type):
        if obj is None:
            return self
        print "__get__", obj, type
        return self.f(obj)

class lazy_property(object):
    def __init__(self, f):
        self.f = f
        self.v = None

    def __get__(self, obj, type):
        if not self.v:
            self.v = self.f(obj)
        return self.v

class Persona(object):
    @myproperty
    def fullname(self):
        return "xxxxx"

def test2():
    p = Persona()
    print p.fullname
    print Persona.fullname

if __name__ == "__main__":
    test2()