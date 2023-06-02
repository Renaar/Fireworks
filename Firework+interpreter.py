import ply.lex as lex
import ply.yacc as yacc
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
ORANGE = (255, 128, 0)

# Définition des tokens
tokens = [
    'COLOR',
    'SIZE',
    'BOOM',
    'COMMA',
]

# Règles des tokens
t_COMMA = r','
t_BOOM = r'BOOM'

def t_COLOR(t):
    r'(Sr|Ba|Cu|Na|K|Ca|Mg)'
    t.value = assign_color(t.value)
    return t

def t_SIZE(t):
    r'(BIG|SMALL)'
    t.value = assign_size(t.value)
    return t

# Ignorer les espaces et tabulations
t_ignore = ' \t'

# Gestion des erreurs de token
def t_error(t):
    print("Caractère non valide : '%s'" % t.value[0])
    t.lexer.skip(1)

# Fonction pour associer les options de couleur à des couleurs réelles
def assign_color(color_option):
    if color_option == 'Sr':
        return RED
    elif color_option == 'Ba':
        return GREEN
    elif color_option == 'Cu':
        return BLUE
    elif color_option == 'Na':
        return YELLOW
    elif color_option == 'K':
        return PURPLE
    elif color_option == 'Ca':
        return ORANGE
    elif color_option == 'Mg':
        return WHITE

# Fonction pour associer les options de taille à des tailles réelles
def assign_size(size_option):
    if size_option == 'BIG':
        return 'BIG'
    elif size_option == 'SMALL':
        return 'SMALL'

# Création de l'analyseur lexical (lexer)
lexer = lex.lex()

# Définition des règles de la grammaire
def p_command(p):
    '''command : COLORS SIZE BOOM'''
    colors = p[1]
    size = p[2]
    run_fireworks(colors, size)

def p_colors(p):
    '''COLORS : COLOR
              | COLORS COMMA COLOR'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# Gestion des erreurs de syntaxe
def p_error(p):
    if p:
        print("Erreur de syntaxe près de :", p.value)
    else:
        print("Erreur de syntaxe à la fin de la commande")

# Création de l'analyseur syntaxique (parser)
parser = yacc.yacc()

# Fonction d'entrée pour exécuter une commande
def run_command(command):
    parser.parse(command)

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
    def __init__(self, x, y, colors, size):
        self.x = x
        self.y = y
        self.colors = colors
        self.size = 3
        self.exploded = False
        self.particles = []
        if size == "SMALL":
            self.explosion_size = random.randint(2, 6)
        elif size == "BIG":
            self.explosion_size = random.randint(10, 20)
        self.explosion_height = random.randint(100, 300)

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

# Fonction pour exécuter les feux d'artifice
def run_fireworks(colors, size):
    fireworks = []
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        if random.uniform(0, 1) < 0.05:
            x = random.uniform(0, WINDOW_WIDTH)
            fireworks.append(Firework(x, WINDOW_HEIGHT, colors, size))

        for firework in fireworks:
            firework.move()
            firework.draw()

        pygame.display.flip()

    pygame.quit()

# Exemple d'utilisation
command = input("Entrez une commande de type (Couleur1,Couleur2,Couleur3 Taille BOOM): ")
run_command(command)
