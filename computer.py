class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    # What methods will you need?
    """ 
    Updates the computer's price.
    """
    def update_price(self, new_price: int):
        self.price = new_price

    """ 
    Updates the computer's OS.
    """
    def update_os(self, new_os: str):
        self.operating_system = new_os
    
    """ 
    Refurbishes a computer by setting a new price based on the year made.
    """
    def refurbish(self):
        if int(self.year_made) < 2000:
            self.price = 0 # too old to sell, donation only
        elif int(self.year_made) < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif int(self.year_made) < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff
    
    """
    Prints the details of the computer.
    """
    def print_details(self):
        print(self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made, self.price)
        
   


