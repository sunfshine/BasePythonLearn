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

    def increaseSerious(self):
        self.serious += 1
    def __test__(self, testValue):
        pprint.pprint(testValue)
    def __testPrivate(self, testValue):
        print(testValue)
    #start one score mean the function is internal access

shipContainer1 = shipContainer("111","222")
shipContainer1.increaseSerious()
print(shipContainer1.serious)
shipContainer1.increaseSerious()
print(shipContainer1.serious)
shipContainer1.increaseSerious()
print(shipContainer1.serious)
shipContainer1.__test__(1111111111111111111111)
shipContainer2 = shipContainer("111","222")
print shipContainer2.serious
shipContainer3 = shipContainer("111","222")
print shipContainer3.serious