import os

class Render:
    def __init__(self, path_len, path_on_screen=50):
        self.path_len = path_len
        self.vehicles = []
        self.path_on_screen = path_on_screen

    def add_player(self, vehicle):
        self.vehicles.append(vehicle)

    def players(self, duration):
        self.clear_terminal()
        print(f"Time {duration}:\n")
        for vehicle in self.vehicles:
            position = int((vehicle.position / self.path_len) * self.path_on_screen)
            row = " " * position + vehicle.img + " " * (self.path_on_screen - position)
            print("▓" + row + "▓")

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
