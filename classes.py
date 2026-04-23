import math
from config import *

class Star(): pass
class Planet(): pass
class Dwarf(): pass
class Moon(): pass
class Comet(): pass
class Asteroid(): pass

cel_bodies = []
types = {
    "star": Star,
    "sun": Star,
    "planet": Planet,
    "dwarf": Dwarf,
    "dwarf_planet": Dwarf,
    "dwarf planet": Dwarf,
    "moon": Moon,
    "comet": Comet,
    "asteroid": Asteroid
}

class Type():
    def __init__(self, type: str):
        self.type = type
        self.return_type()

    def return_type(self):
        if self.type.lower() in types.keys():
            return types[self.type.lower()]
        else:
            print(f"\n\x1b[1;31mError\x1b[1;0m:\fInvalid type: {self.type}\x1b[0m\n")
            exit()

class CelestialBody():
    def __init__(self, name: str,type: Type, position: tuple[int | float, int | float], radius: int | float, mass: int | float, color=None, orbits: str=""):
        self.name = name
        self.type = type
        self.position = position
        self.radius = radius
        self.mass = mass

        self.orbits = Type(orbits.lower()) if (orbits != None and len(orbits) > 0) else None
        self.orbit = []
        self.orbit_dist = 0

        self.orbit_vel = velocities[self.name.lower()] if self.name.lower() in velocities.keys() else 200
        self.velocity = (0, self.orbit_vel)

        if name.lower() in colors.keys():
            self.color = colors[name.lower()]
        elif (not color) or (not isinstance(color, tuple)) or (isinstance(color, tuple) and (len(color) < 3 or len(color) > 4)):
            self.color = colors["gray"]
        else:
            self.color = color
            

        cel_bodies.append(self)

    def draw(self, window):
        window_w, window_h = window.get_size()
        pos = (self.position[0] * SCALE + window_w // 2,
               self.position[1] * SCALE + window_h // 2)
        pygame.draw.circle(window, self.color, pos, self.radius)

    def attraction(self, other):
        distances = [self.position[0], self.position[1]]
        for i, d in enumerate(distances):
            distances[i] = other.position[i] - d

        distance = math.sqrt(distances[0]**2 + distances[1]**2)

        if other.type == Star:
            self.distance_to_star = distance
        force = G * self.mass * other.mass / distance**2
        angle = math.atan2(distances[1], distances[0])
        force_vector = (math.cos(angle) * force, math.sin(angle) * force)

        return force_vector
    
    def update_pos(self, cel_bodies):
        total_force = [0, 0]
        for cel_body in cel_bodies:
            if self == cel_body:
                continue
            force = self.attraction(cel_body)
            for i, f in enumerate(force):
                total_force[i] += f  # Or just "="? Or just cut out the middle-man (total_force)?
        self.velocity = (self.velocity[0] + total_force[0] / self.mass * TIMESTEP,
                         self.velocity[1] + total_force[1] / self.mass * TIMESTEP)
        self.position = (self.position[0] + self.velocity[0] * TIMESTEP,
                         self.position[1] + self.velocity[1] * TIMESTEP)
        self.orbit.append(self.position)

    def __str__(self):
        return self.name