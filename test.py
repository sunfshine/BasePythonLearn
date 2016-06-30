class myTest:
    video_path = "hahahh"
    def __init__(self):
        self.testProperty = "1255"
    def getMyTestInfo(self):
        self.testProperty = "1255"
        video_path = "{}{}".format(11213, self.video_path) if self.video_path else self.video_path
        testVal = 1
        print(testVal)
        print(video_path)
        return ""

myTest1 = myTest()
myTest1.getMyTestInfo()

class A(object):
    x = 1
class B(A):
    pass
class C(A):
    pass


Aobj = A()
Bobj = B()
Cobj = C()

print A.x, B.x, C.x
print Aobj.x, Bobj.x, Cobj.x

print "b.x: ", id(B.x)
B.x = 2
print "b.x: ", id(B.x)

print A.x, B.x, C.x
print Aobj.x, Bobj.x, Cobj.x

A.x = 3
print A.x, B.x, C.x
print Aobj.x, Bobj.x, Cobj.x


C.x = 5
print A.x, B.x, C.x
print Aobj.x, Bobj.x, Cobj.x


