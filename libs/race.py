import time


class Race:
    def __init__(self, render, path_len, ffwd=1):
        self.render = render
        self.path_len = path_len
        self.vehicles = []
        self.ffwd = ffwd

    def with_player(self, vehicle):
        self.vehicles.append(vehicle)
        self.render.add_player(vehicle)
        return self

    def run(self):
        duration = 0
        while True:
            for vehicle in self.vehicles:
                vehicle.update()
                if vehicle.position >= self.path_len:
                    self.render.players(duration)
                    print(f"\n{vehicle.name} win the race in {duration} secs!")
                    return
            self.render.players(duration)
            duration += 1
            time.sleep(1 / self.ffwd)
