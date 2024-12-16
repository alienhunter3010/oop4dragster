class Players:
    vehicles = []

    def __init__(self):
        pass

    @staticmethod
    def with_player(vehicle):
        Players.vehicles.append(vehicle)
        return Players
