import pygame
import random

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Création de la fenêtre
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feux d'artifice")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 128, 0)

# Classe de particules
class Particle:
    def __init__(self, x, y, colors):
        self.x = x
        self.y = y
        self.colors = colors
        self.size = 3
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.life = random.randint(30, 60)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.life -= 1

    def draw(self):
        color = random.choice(self.colors)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.size)

# Classe de feu d'artifice
class Firework:
    def __init__(self, x, y, colors):
        self.x = x
        self.y = y
        self.colors = colors
        self.size = 3
        self.exploded = False
        self.particles = []
        self.explosion_height = random.randint(100, 300)
        self.explosion_size = random.randint(2, 6)

    def move(self):
        if not self.exploded:
            self.y -= 5
            if self.y <= self.explosion_height:
                self.explode()

        if self.exploded:
            for particle in self.particles:
                particle.move()

            self.particles = [particle for particle in self.particles if particle.life > 0]

    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

        if self.exploded:
            for particle in self.particles:
                particle.draw()

    def explode(self):
        self.exploded = True
        for i in range(100):
            particle = Particle(self.x, self.y, self.colors)
            particle.size = self.explosion_size
            self.particles.append(particle)

# Liste de feux d'artifice
fireworks = []

# Boucle principale
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Efface l'écran
    screen.fill(BLACK)

    # Génère une nouvelle fusée de façon aléatoire
    if random.uniform(0, 1) < 0.05:
        x = random.uniform(0, WINDOW_WIDTH)
        colors = random.sample([RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, ORANGE], random.randint(2, 4))
        fireworks.append(Firework(x, WINDOW_HEIGHT, colors))

    # Anime les feux d'artifice
    for firework in fireworks:
        firework.move()
        firework.draw()

    # Met à jour l'écran
    pygame.display.flip()

# Quitte le programme
pygame.quit()

