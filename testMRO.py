#__mro__ is only defined for new-style classes. In Python 2, a class is only new-style
# if it inherits from object (or from a built in type, which in turn inherits from object),
# while all classes in Python 3 are new-style no matter what.


class A(object):
    aa = 0

    def __init__(self):
        print "a initialized!"


class B(A):

    def ohMyFunc1():
        print "B: oh my func1"
    pass


class C(A):

    def ohMyFunc1():
        super(A, C)
        print "32"
    pass


class D(B, C):

    def __init__(self):
        print "D init"

    def ohMyFunc1():
        super(A, C)
        print "32"

    def ohMyfunc(self):
        print "D: oh my func"

Dobj = D()
print D.__dict__
type(D.ohMyFunc1())
D.ohMyfunc()
print D.__mro__
