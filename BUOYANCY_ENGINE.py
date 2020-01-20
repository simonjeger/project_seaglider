import os
import numpy as np


class tube:

    def __init__(self, name, weight, volume, price):

        # Initialize

        # Specs
        self.name = name
        self.weight = weight  # kg
        self.volume = volume # m^3
        self.price = price # CHF

        # Error



    def specifications(self):

        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'weight: ' + str(round(self.weight, 3)) + ' [kg]' + '\n'
        string = string + 'volume: ' + str(round(self.volume,3)) + ' [m^3]' + '\n'
        string = string + 'price: ' + str(round(self.price, 2)) + ' [CHF]' + '\n'
        string = string + '\n' + '\n'

        return string


    def display(self):
        print(self.specifications())


    def write(self):
        # Clear file
        file = open(self.path + '/' + __class__.__name__ + ".txt", "w")
        file.close()
        os.remove(self.path + '/' + __class__.__name__ + ".txt")

        # Write file
        file = open(self.path + '/' + __class__.__name__ + ".txt", "w")
        file.write(self.specifications())
        file.close()


buoyancy_engine_small = tube('buoyancy_engine_small', 0.2, 6*50*10**-6, 10)