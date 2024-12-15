class Players:
    vehicles = []

    def __init__(self):
        pass

    def with_player(self, vehicle):
        self.vehicles.append(vehicle)
        return self
