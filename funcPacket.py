class funcPacket:
    a = 1
    def __init__(self):
        self.mylocal = "1323"
    @staticmethod
    def TestFuncPacket():
        t  = 22
        print t
        def packetFunc():
            t = 8
            t += 1
        return packetFunc


A = funcPacket()
print funcPacket.TestFuncPacket()