class Bank(object):
    crisis = False
    Index = 0
    def create_atm(self):
        while not self.crisis and self.Index < 10000:
            self.Index += 1
            yield "$100"
hsBank = Bank()
corner_stread_atm = hsBank.create_atm()
print (list(corner_stread_atm)) 
