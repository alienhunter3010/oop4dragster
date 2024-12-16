class Players:

    def __init__(self):
        self.vehicles = []

    def with_player(self, vehicle):
        self.vehicles.append(vehicle)
        return self
