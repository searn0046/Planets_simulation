from config import *
from classes import *

window = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.WINDOWMAXIMIZED | pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("Solar System Simulation")

def main():
    global window
    run = True
    clock = pygame.time.Clock()

    sun = CelestialBody(
                        name="Sun",
                        type=Type("SuN"),
                        position=(0, 0),
                        radius=30,
                        mass=1.98892 * 10**30
                        )
    mercury = CelestialBody(
                        name="Mercury",
                        type=Type("PLANET"),
                        position=(0.387 * AU, 0),
                        radius=7,
                        mass=3.3 * 10**23,
                        orbits="sun"
                        )
    venus = CelestialBody(
                        name="Venus",
                        type=Type("PlAnEt"),
                        position=(0.723 * AU, 0),
                        radius=9, 
                        mass=4.8685 * 10**24,
                        orbits="sun"
                        )
    earth = CelestialBody(
                        name="Earth",
                        type=Type("pLanEt"),
                        position=(1 * AU, 0),
                        radius=10,
                        mass=5.9742 * 10**24,
                        orbits="sun"
                        )
    mars = CelestialBody(
                        name="Mars",
                        type=Type("planet"),
                        position=(1.524 * AU, 0),
                        radius=9,
                        mass=6.39 * 10**23,
                        orbits="sun"
                        )
    jupiter = CelestialBody(
                        name="Jupiter",
                        type=Type("planet"),
                        position=(-5.2 * AU, 0),
                        radius=20,
                        mass=1.89813 * 10**27,
                        orbits="sun"
                        )
    saturn = CelestialBody(
                        name="Saturn",
                        type=Type("planet"),
                        position=(-9.55 * AU, 0),
                        radius=14,
                        mass=5.683 * 10**26,
                        orbits="sun"
                        )
    uranus = CelestialBody(
                        name="Uranus",
                        type=Type("planet"),
                        position=(-19.2 * AU, 0),
                        radius=12,
                        mass=8.681 * 10**25,
                        orbits="sun"
                        )
    neptune = CelestialBody(
                        name="Neptune",
                        type=Type("planet"),
                        position=(-30 * AU, 0),
                        radius=12,
                        mass=1.024 * 10**26,
                        orbits="sun"
                        )
    pluto = CelestialBody(
                        name="Pluto",
                        type=Type("dwarf"),
                        position=(-39.5 * AU, 0),
                        radius=2,
                        mass=1.309 * 10**22,
                        orbits="sun"
                        )
    
    while run:
        clock.tick(FRAMERATE)
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((event.w, event.h), pygame.DOUBLEBUF | pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and pygame.display.is_fullscreen():
                    pygame.display.toggle_fullscreen()

        [(body.update_pos(cel_bodies), body.draw(window)) for body in cel_bodies]

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()