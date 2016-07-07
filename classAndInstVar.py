class  A(object):
    static_data = 1
    def __init__(self):
        self.data = 1
Aobj = A()
Aobj.data1 = 2
print Aobj.data1



class B(A):
    def __init__(self):
        A.__init__(self)
        self.data2 = 1



Bobj = B()
Bobj.static_data = 3
B.static_data = 3

print A.static_data
print B.static_data
print Bobj.static_data