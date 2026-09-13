# Ashleigh Molinet
# Car_Printer_App
# SDEV220 Created 2026-09-12

# Program will have the superclass Vehicle and the subclass Automobile
# Vehicle will contain attribute type
# Automobile will contain attributes year, make, model, doors, roof
# App will accept user input for a vehicle attributes and store them 
# app will accept user input for automobile attributes and store them
# app will output data in easy to read format

class Vehicle:
    def __init__(self, type):
        self.type = input('Please input type of vehicle: ')
        print("Vehicle Type: ", self.type)

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super.__init__()
        self.year = input('Please input year of automobile: ')
        self.make = input('Please input make of automobile: ')
        self.model = input('Please input model of automobile: ')
        self.doors = int(input('Please input number of doors: '))
        self.roof = input('Please input roof type (solid or sun roof): ')
    def display_i
        
