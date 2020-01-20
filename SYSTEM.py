import os
import numpy as np
import TUBE
import WING
import BUOYANCY_ENGINE



class system:

    def __init__(self, name, my_tube, my_wing, my_buoyancy_engine, weight_max, pitch_angle):

        # Generate folder for results (only for highest level file)
        self.path = 'specifications'
        os.makedirs(self.path, exist_ok=True)

        # Initialize
        self.my_tube = my_tube
        self.my_wing = my_wing
        self.my_buoyancy_engine = my_buoyancy_engine

        # Specs
        self.name = name
        self.density_water = 997 # kg/m^3
        self.density_air = 1.225  # kg/m^3
        self.weight = self.my_tube.weight + 2 * self.my_wing.weight + self.my_buoyancy_engine.weight# kg
        self.weight_max = weight_max # kg
        self.displaced_volume = self.my_tube.displaced_volume + 2 * self.my_wing.displaced_volume # m^3
        self.displaced_weight = self.displaced_volume * self.density_water # kg
        self.drag = (self.my_tube.drag_partial + 2 * self.my_wing.drag_partial) * self.density_water * 2# N/(v^2)
        self.pitch_angle = pitch_angle / 360 * 2 * np.pi # degrees
        self.velocity = np.sqrt(np.sin(self.pitch_angle) * 0.5 * my_buoyancy_engine.volume * (self.density_water - self.density_air) / self.drag) # * 0.5 since it's neutrally buoyant when half full
        self.drag = self.drag * self.velocity ** 2  # N
        self.price = self.my_tube.price + 2 * self.my_wing.price + self.my_buoyancy_engine.price # CHF

        # Error
        self.error_weight()


    def error_weight(self):
        if self.weight <= self.weight_max:
            pass
        else:
            print(str(__class__.__name__) + ': error_weight')


    def specifications(self):

        # Initialize
        string = ''

        # Name
        string = string + '-----------------------------------------' + '\n'
        string = string + __class__.__name__ + ': ' + self.name + '\n'
        string = string + '- - - - - - - - - - - - - - - - - - - - -' + '\n'

        # Specs
        string = string + 'my_tube: ' + str(self.my_tube.__class__.__name__) + '\n'
        string = string + 'weight: ' + str(round(self.weight,3)) + ' [kg]' + '\n'
        string = string + 'weight_max: ' + str(round(self.weight_max, 3)) + ' [kg]' + '\n'
        string = string + 'displaced_volume: ' + str(round(self.displaced_volume, 3)) + ' [m^3]' + '\n'
        string = string + 'displaced_weight: ' + str(round(self.displaced_weight, 3)) + ' [kg]' + '\n'
        string = string + 'drag: ' + str(round(self.drag, 3)) + ' [N]' + '\n'
        string = string + 'velocity: ' + str(round(self.velocity, 3)) + ' [m/s]' + '\n'
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


    def write_all(self):
        # (Only for highest level file)

        # Clear file
        file_name = "/overview.txt"
        #file_name = '/' + self.my_tube.name + '.txt'
        file = open(self.path + file_name, "w")
        file.close()
        os.remove(self.path + file_name)

        # Write file
        file = open(self.path + file_name, "w")
        file.write(self.specifications())
        file.write(self.my_tube.specifications())
        file.write(self.my_wing.specifications())
        file.close()



my_system = system('seaglider', TUBE.tube_small, WING.wing_small, BUOYANCY_ENGINE.buoyancy_engine_small, 20, 20)
my_system.write_all()