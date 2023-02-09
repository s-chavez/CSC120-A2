from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
    
    # What methods will you need?
    """ 
    Buys a computer by adding the computer to the inventory.
    """
    def buy(self, computer: Computer):
        # 1. call Computer(...) constructor to create a new Computer instance
        computer = Computer()
        # 2. call inventory.append(...) to add the new Computer instance to the inventory
        self.inventory.append(computer)
    
    """ 
    Sells a computer by removing the computer from the inventory.
    """
    def sell(self, computer: Computer):
        computer = Computer()
        self.inventory.remove(computer)
  
    """ 
    Prints all the items in the inventory (if it isn't empty). Prints error otherwise.
    """
    def print_inventory(self):
        print(self.inventory)

    def main():
        test_computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
        test_computer2 = Computer("Acer", "3.5 GHc 6-Core Intel Xeon E5", 512, 32, "Windows 10", 2020, 900)  
    # COMPUTER CLASS: testing update price function
        # test_computer.update_price(2000)
        # test_computer.print_details()
    # COMPUTER CLASS: testing update os function
        # test_computer.update_os("new_macOS")
        # test_computer.print_details()
    # COMPUTER CLASS: testing refurbish function
        # test_computer.refurbish()
        # test_computer.print_details()
    # RESALE SHOP CLASS: testing buy function
    # RESALE SHOP CLASS: testing sell function
        
    main()