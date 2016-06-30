class  Base(object):
    a = 1
    def __init__(self):
        print "Base initialize"

class SubClassB(Base):
    def __init__(self):
        self.myObjAttr = 1
        super(SubClassB).__init__()
        print "Sub class initialize"

    @classmethod
    def testClassMethod(cls):
        print "testClassMethod"

class SubClassC(Base):
    def __init__(self):
        self.myObjAttr = 1
        super(SubClassC).__init__()
        print "Sub class initialize"

    @classmethod
    def testClassMethod(cls):
        print "testClassMethod"

print "SubClassB a id: ",id(SubClassB.a)
SubClassB.a = 2
print "SubClassB a id: ", id(SubClassB.a)

print "Base a id: ",id(Base.a)
print "SubClassC a id: ", id(SubClassC.a)


Base.a = 2
print "Base a id: ", id(Base.a)
print "SubClassC a id: ", id(SubClassC.a)

