import ply.lex as lex
import ply.yacc as yacc

# Définition des tokens
tokens = [
    'COLOR',
    'SIZE',
    'SHAPE',
    'BOOM',
]

# Règles des tokens
t_COLOR = r'(Sr|Ba|Cu|Na|K|Ca|Mg)'
t_SIZE = r'(BIG|SMALL)'
t_SHAPE = r'(SQUARE|CIRCLE)'
t_BOOM = r'BOOM'

# Ignorer les espaces et tabulations
t_ignore = ' \t'

# Gestion des erreurs de token
def t_error(t):
    print("Caractère non valide : '%s'" % t.value[0])
    t.lexer.skip(1)

# Création de l'analyseur lexical (lexer)
lexer = lex.lex()

# Définition des règles de la grammaire
def p_command(p):
    '''command : COLOR SIZE SHAPE BOOM'''
    print("Commande exécutée :", p[1], p[2], p[3])

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

# Exemple d'utilisation
command = input("Entrez une commande de type (Couleur Taille Forme BOOM): ")
run_command(command)
