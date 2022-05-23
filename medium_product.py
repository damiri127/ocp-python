from product_delivery import ProductDelivery

class MediumProduct:
    
    def __init__(self, price: int, name: str):
        super().__init__(name, price)
        
    def calculate_delivery(self):
        return self.get_price() + 2500