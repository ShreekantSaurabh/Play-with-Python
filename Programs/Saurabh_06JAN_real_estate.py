class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("Property Details")
        print("="*10)
        


class Agent:
    property_list = []
    
    def list_properties(self, show_all = False):
        self.show_all = show_all
        

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies= ("yes", "no", "solarium")
    
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
        
        
    