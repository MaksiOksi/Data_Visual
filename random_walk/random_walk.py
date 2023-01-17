from random import choice


class RandomWalk:

    def __init__(self, num_points=5000):

        self.num_points = num_points

        # Start walk
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):

        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = distance * direction
        return step

    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            y_step = self.get_step()
            x_step = self.get_step()

            # Discard zero steps
            if x_step == 0 and y_step == 0:
                continue

            # Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
