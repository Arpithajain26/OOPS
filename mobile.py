class Mobile:
    def __init__(self,brand,price=0):
        self.brand=brand
        self.price=price
    def display_brand(self):
        print(f" the brand of the car:{self.brand}")
    def display_price(self):
        print(f" the price of the car is :{self.price}")
mobile1=Mobile("vivo",12000)
mobile2=Mobile("redmi",15000)
mobile1.display_brand()
mobile1.display_price()
mobile2.display_price()
mobile2.display_brand()