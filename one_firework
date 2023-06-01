import pygame
import random
import math

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

time_since_last_explosion = 0.0

# Classe de particules
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(2, 6)
        self.speed = random.uniform(2, 6)
        self.angle = random.uniform(0, 2 * math.pi)
        self.life = random.randint(30, 60)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= 1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Classe de feu d'artifice
class Firework:
    def __init__(self, x, y, color, explosion_size):
        self.x = x
        self.y = y
        self.color = color
        self.exploded = False
        self.particles = []
        self.explosion_size = explosion_size

    def move(self):
        if not self.exploded:
            self.explode()

        if self.exploded:
            for particle in self.particles:
                particle.move()

            self.particles = [particle for particle in self.particles if particle.life > 0]

    def draw(self):
        if self.exploded:
            for particle in self.particles:
                particle.draw()

    def explode(self):
        self.exploded = True
        num_particles = random.randint(100, 150)

        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(0, self.explosion_size)
            dx = distance * math.cos(angle)
            dy = distance * math.sin(angle)

            particle = Particle(self.x + dx, self.y + dy, self.color)
            particle.life = random.randint(30, 60)
            self.particles.append(particle)

# Demande à l'utilisateur de saisir la couleur des explosions
color_input = input("Couleur des explosions (RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, ORANGE, WHITE, BLACK) : ")
color_input = color_input.upper()

# Définition de la couleur choisie
if color_input == "RED":
    primary_color = (255, 0, 0)
elif color_input == "GREEN":
    primary_color = (0, 255, 0)
elif color_input == "BLUE":
    primary_color = (0, 0, 255)
elif color_input == "YELLOW":
    primary_color = (255, 255, 0)
elif color_input == "PURPLE":
    primary_color = (255, 0, 255)
elif color_input == "CYAN":
    primary_color = (0, 255, 255)
elif color_input == "ORANGE":
    primary_color = (255, 128, 0)
elif color_input == "WHITE":
    primary_color = (255, 255, 255)
else:
    primary_color = (0, 0, 0)

# Liste pour stocker les explosions en cours
fireworks = []

# Fonction pour générer une explosion
def explode():
    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    firework = Firework(x, y, primary_color, random.uniform(100, 300))
    fireworks.append(firework)

# Boucle principale
running = True
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60) / 1000.0

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Efface l'écran
    screen.fill(BLACK)

    # Anime et dessine les explosions en cours
    for firework in fireworks:
        firework.move()
        firework.draw()

    # Supprime les explosions terminées de la liste
    fireworks = [firework for firework in fireworks if not firework.exploded or len(firework.particles) > 0]

    # Temps écoulé depuis la dernière explosion
    time_since_last_explosion += dt

    # Génère une nouvelle explosion si le temps requis est écoulé
    if time_since_last_explosion >= 1.0:
        explode()
        time_since_last_explosion = 0

    # Met à jour l'affichage
    pygame.display.flip()

# Quitte le jeu
pygame.quit()
