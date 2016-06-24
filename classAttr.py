import pprint
class shipContainer:
    serious = 1337
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serious +=1
        pprint.pprint(self)
        pprint.pprint(shipContainer)
        shipContainer.serious += 1
        pprint.pprint(shipContainer.serious)
shipContainer1 = shipContainer("111","222")
shipContainer1.serious
shipContainer2 = shipContainer("111","222")
shipContainer2.serious
shipContainer3 = shipContainer("111","222")
shipContainer3.serious