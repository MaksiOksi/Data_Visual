from random import randint

class GamblingCube:

    # Initialize cube
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    # Create a random num of cube side
    def roll(self):
        return randint(1, self.num_sides)
