import os
import numpy as np


class wing:

    def __init__(self, name, span, width, thickness, density, price):

        # Initialize

        # Specs
        self.name = name
        self.span = span # m
        self.width = width # m
        self.thickness = thickness # m
        self.density = density # kg / m^3
        self.weight = span * width * thickness * density # kg
        self.displaced_volume = span * width # m^3
        self.drag_partial = 0.05 * self.span * self.width # flat plate (https://www.princeton.edu/~maelabs/hpt/mechanics/mecha_54.htm) # N/(rho*v^2/2)
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
        string = string + 'span: ' + str(round(self.span,3)) + ' [m]' + '\n'
        string = string + 'width: ' + str(round(self.width,3)) + ' [m]' + '\n'
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


wing_small = wing('wing_small', 0.3, 0.05, 0.003, 8050, 20)