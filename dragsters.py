from libs.vehicle import Vehicle
from libs.render import Render
from libs.race import Race
import sys


# Funzione
def coc_arg(idx, default):
    # Condizione
    if len(sys.argv) >= idx + 1:
        return sys.argv[idx]
    else:
        return default

# Istruzione
# (Assegnazione di) Variabile
path_len = int(coc_arg(1, 1000))

# Oggetto (istanza)
race = Race(
    render = Render(path_len, 200),
    path_len = path_len
)

# Chiamata a un Metodo
race.with_player(
        Vehicle("Audi", acceleration=3, max_velocity=50)
    ).with_player(
        Vehicle("Cadillac", acceleration=2, max_velocity=60, img="[ ) ]")
    ).with_player(
        Vehicle("Yamaha", acceleration=4, max_velocity=70, img="  =o=")
    ).with_player(
        Vehicle("Solar wind", acceleration=1, max_velocity=99999, img="  ))>")
    )

race.run()
