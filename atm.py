class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def cashWithdrawl():
        print('You have withdrawn the cash')

    def balanceEnquiry():
        print('you should check your balance')

card1=Atm(123456,4125)
print(card1.pinNumber)


