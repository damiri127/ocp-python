from product_delivery import ProductDelivery 

class MediumProduct(ProductDelivery):
    
    def __init__(self, price: int, name: str):
        super().__init__(price, name)
        
    def calculate_delivery(self):
        return self.get_price() + 2500