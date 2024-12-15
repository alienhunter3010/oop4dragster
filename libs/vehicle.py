# Classe
class Vehicle:
    # Costruttore
    def __init__(self, name, acceleration, max_velocity, img="[( )]"):
        # Proprietà (Variabile)
        self.name = name
        self.acceleration = acceleration
        self.max_velocity = max_velocity
        self.cur_velocity = 0
        self.position = 0  # in m
        self.img = img

    # Metodo (funzione)
    def update(self):
        self.cur_velocity = min(self.cur_velocity + self.acceleration, self.max_velocity)
        self.position += self.cur_velocity

    # (Ri)definizione di metodo standard
    def __str__(self):
        return f"{self.name}: Velocity={self.cur_velocity:.2f} m/s, Position={self.position:.2f} m"
