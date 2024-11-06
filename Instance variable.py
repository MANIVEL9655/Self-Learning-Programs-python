class Car:
    def __init__(self, discount):
        self.discount = discount
        print("Corporate discount", self.discount)
    def chennaiDealer(self, price):
        totalPrice  = price - self.discount
        print("Chennai Dealer Price", totalPrice)
    def maduraiDealer(self, price):
        totalPrice = price - self.discount
        print("Madurai Dealer Price", totalPrice)
carObj = Car(500)
carObj.chennaiDealer(1500)
carObj.maduraiDealer(2000)
