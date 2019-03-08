'''
Class :
old style class Foo:
new style class Foo(object): or class Foo():

Left to right look up on inheritance

Method Resolution Order : MRO __mro___
Class.__mro__

__init__ is the constructor for objects. Self is this pointer.

obj.method() same as Class.method(obj)

Class Variables - like static, assigned within class
Instance Variables - attached to object, within __init__

pass- null statement, for syntax

double_score : private : __example   , cant be accessed by any object outside. it shows as _Class__example
double_double_score : public : __example__

its not strictly private, cos of the Name Mangling happening in the interpreter

__repr__
__str__ ways to print an object. If __str__ is not defined, __repr__ is used.
If both are undefined, default print used which prints the reference, like the Obj type


object()
base class for every class created in Python
Attributes cant be added to the object
dir gives listing of all attributes

== compares values, "is" compares references

Differences :

print operation
division operation - use floats
Exception - as keyword
from __future__ import <>
Unicode - Py2 has string type ASCII but Py3 treats as Unicode
xrange - deprecated used to giv generator


Multiple inheritance, supported like C++ evaluated from Left to right
Earliest match is returned

base constructor:
Base.__init__() or super(Derived,self).__init__()

LEGB scope resolution : Local Enclosed{} Global Builtin

'''

class Old(object):
    def test(self):
        print('Old')

class Sub1(Old):
     '''
          def test(self):
        print('Sub1')

     '''


class Sub2(Old):
     def test(self):
        print('Sub2')

class Diamond(Sub1,Sub2):
    '''
        def test(self):
        print('Diamond')

    '''


o1 = Diamond()
o1.test()
#print(Diamond.__mro__)


# Python example to show working of multiple
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print
        "Base1"


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print
        "Base2"


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print
        "Derived"

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()