import pygame
pygame.init()

WINDOW_W, WINDOW_H = int(pygame.display.get_desktop_sizes()[0][0] * 0.95), int(pygame.display.get_desktop_sizes()[0][1] * 0.95)
FRAMERATE = 60
AU = 149.6e6 * 1000 # Number of meters the Earth is from the Sun.
G = 6.67428e-11
SCALE = 120 / AU    # 1AU = 100 pixels
TIMESTEP = 60 * 60 * 24 * 60 / FRAMERATE    # 1 day = 86400 seconds

colors = {
    "sun": (255, 223, 34),
    "mercury": (212, 191, 101),
    "venus": (173, 141, 84),
    "earth": (0, 0, 160),
    "mars": (199,125,78),
    "jupiter": (209, 167, 127),
    "saturn": (234, 214, 184),
    "uranus": (172, 229, 238),
    "neptune": (91, 93, 223),
    "pluto": (255, 241, 213),
    "gray": (100, 100, 100)
}

velocities = {
    "sun": 0,
    "mercury": -47.4 * 1000,
    "venus": -35.02 * 1000,
    "earth": -29.783 * 1000,
    "mars": -24.077 * 1000,
    "jupiter": 13.07 * 1000,
    "saturn": 9.69 * 1000,
    "uranus": 6.81 * 1000,
    "neptune": 5.43 * 1000,
    "pluto": 4.666 * 1000 
}