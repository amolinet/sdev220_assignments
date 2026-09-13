# Ashleigh Molinet
# Car_Info_Printer_App
# SDEV220 Created 2026-09-12

# Program will have the superclass Vehicle and the subclass Automobile
# Vehicle will contain attribute type
# Automobile will contain attributes year, make, model, doors, roof
# App will accept user input for a vehicle attributes and store them 
# app will accept user input for automobile attributes and store them
# app will output data in easy to read format

class Vehicle:
    def __init__(self):
        self.type = input('Please input type of vehicle: ')

class Automobile(Vehicle):
    def __init__(self):
        super().__init__() #keeps superclass initialization

        #info input
        self.year = input('Please input year of automobile: ')
        self.make =
        input('Please input make of automobile: ')
        self.model = input('Please input model of automobile: ')
        self.doors = int(input('Please input number of doors: '))
        self.roof = input('Please input roof type (solid or sun roof): ')

    # display information input
    def display_inputs(self):
        print("---VEHICLE DETAILS---")
        print(f"Vehicle Type: {self.type} \nYear: {self.year} \nMake: {self.make} \nModel: {self.model} \nDoors: {self.doors} \nRoof Type: {self.roof}")

print("Welcome to the Car_Info_Printer_App by Ashleigh Molinet") #program header
car = Automobile() #prompts user for input & stores it
car.display_inputs() #displays stored information
print ("Thank you for using the Car_Info_Printer_App, hope you have a printer-ific day!") #program footer
