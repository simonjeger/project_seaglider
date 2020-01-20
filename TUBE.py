import os
import numpy as np


class tube:

    def __init__(self, name, diameter, length, thickness, density, price):

        # Initialize

        # Specs
        self.name = name
        self.diameter = diameter # m
        self.length = length # m
        self.thickness = thickness # m
        self.density = density # kg / m^3
        self.weight = (diameter ** 2 - (diameter - 2 * thickness) ** 2) / 4 * np.pi * length * density # kg
        self.displaced_volume = diameter ** 2 / 4 * np.pi * length # m^3
        self.drag_partial = diameter ** 2 / 4 * np.pi * 0.82 # long cylinder # N / (rho * v^2 / 2)
        self.price = price

        # Error



    def specifications(self):

        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'diameter: ' + str(round(self.diameter,3)) + ' [m]' + '\n'
        string = string + 'length: ' + str(round(self.length,3)) + ' [m]' + '\n'
        string = string + 'weight: ' + str(round(self.weight,3)) + ' [kg]' + '\n'
        string = string + 'displaced_volume: ' + str(round(self.displaced_volume,3)) + ' [m^3]' + '\n'
        string = string + 'drag_partial: ' + str(round(self.drag_partial, 3)) + ' [N/(rho*v^2/2)]' + '\n'
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


tube_small = tube('tube_small', 0.1016, 1, 0.002, 1180, 50)