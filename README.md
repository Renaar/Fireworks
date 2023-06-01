# Fireworks
Mon langage pour le cours de Langage & Compilation

Il faut créer son propre langage de programmation.
A l'aide de la bibliothèque PLY sur python.

L'idée de mon langage est de créer des animations de feux d'artifices à partir d'instructions.
L'instruction se compose d'abord d'une couleur, représentée par son élément chimique.
Vient ensuite la taille de l'explosion.
Puis la forme.
Et enfin le mot qui permet la mise à feu.

Voilà l'expression régulière de mon langage :

commande : couleurs SIZE SHAPE BOOM

couleurs : COULEUR
         | couleurs COULEUR

COULEUR : 'Sr' | 'Ba' | 'Cu' | 'Na' | 'K' | 'Ca' | 'Mg'
SIZE : 'BIG' | 'SMALL'
SHAPE : 'SQUARE' | 'CIRCLE'
BOOM : 'BOOM'


Sr = Rouge   (Strontium)
Ba = Vert    (Baryum)
Cu = Bleu    (Cuivre)
Na = Jaune   (Sodium)
K  = Violet  (Potassium)
Ca = Orange  (Calcium)
Mg = Blanc   (Magnésium)
