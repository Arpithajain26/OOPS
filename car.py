class Car:
    def __init__(self,car_id,name,year,price_per_day,status="available",rented_days=0):
        self.car_id=car_id
        self.name=name
        self.year=year
        self.prcie_per_day=price_per_day
        self.status=status
        self.rented_days=rented_days
    def display_details(self):
        print(f"car id :{self.car_id},name:{self.name}, year:{self.year},price_per_day:{self.prcie_per_day}.status={self.status}")
    def update_status(self,new_status):
        self.status=new_status
        print(f" {self.car_id} updated to  new status {self.status}")
    def calculate_price(self):
        total_price=self.prcie_per_day* self.rented_days
        print(f" total rental price for {self.name}:${total_price}")
car1=Car(1,"swift",2028,8400,"available",9)
car2=Car(2,"safari",2024,8300,"available",6)
car3=Car(3,"benz",2026,8001,"available",8)




car1.display_details()
car2.calculate_price()
