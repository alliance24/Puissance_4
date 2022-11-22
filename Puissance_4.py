'''
 Duo: Nathan, Julien
 Quatuor: Nathan, Julien, Reian, Chayan
 Certaines parties possèdent des bouts de codes qui sont utilitaires 
 (meilleure visualisation graphique) ou nécessaires pour faire les tests
'''


# g --> grille principale qui va evoluer en fonction de la partie 
# g = [[0 for c in range(7)] for l in range(6)]

# grille temporaire pour faire les tests
g = [
     [1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 0],
     ]

# l --> ligne (valeur entre 0 et 5)
# c --> colonne (valeur entre 0 et 6)
# j --> joueur (valeur entre 1 ou 2)
# 0 --> case vide | 1 ou 2 --> joueur correspondant

# 1 --> X
# 2 --> O

# Affiche la grille vide
def grille_vide():
    return [[0 for c in range(7)] for l in range(6)]
        
def affiche(g):
    print() # Permet de sauter une ligne (+ propre visuellement parlant)
    # On remplace les valeurs par qqch de plus graphique
    for l in range(len(g)):

        # Aide visuelle
        print("  ", end='')
        print(l, end='')
        
        for c in range(7):
            if g[l][c] == 0:
                print("  .", end='')
            elif g[l][c] == 1:
                print("  X", end='')
            elif g[l][c] == 2:
                print("  O", end='')
        print("\n")
        
def coup_possible(g, c): # c doit etre l'index
    if g[0][c] == 0:
        return True
    else:
        return False

def jouer(g,j,c): # c doit etre l'index
    max = 0
    if coup_possible(g, c) == True:
        for l in range(len(g)):
            if g[l][c] == 0:
                max = l
        g[max][c] = j

def horiz(g,j,l,c): # c doit etre l'index
    if g[l][c] == j:
        
        total = 1 # nb de valeurs egales a (j)
        # l index du tableau et c index de la case
 
        for e in range(c+1, len(g[l])):
            if g[l][e] == g[l][c]:
                total +=1
            else:
                break

        for e in range(c-1, 0, -1):
            if g[l][e] == g[l][c]:
                total +=1
            else:
                break

        if total >= 4:
            return True
        else:
            return False

# vert() ne marche pas encore --> retourne False tout le temps
def vert(g, j, l, c):
    if g[l][c] == j:

        total = 1 # nb de valeurs egales a (j) donc si total=4 alors (j) a gagné
        # l index du tableau et c index de la case

        for e in range(l+1, len(g), 1):
            if g[e][c] == g[l][c]:
                total +=1
            else:
                break

        for e in range(l-1, 0, -1):
            if g[e][c] == g[l][c]:
                total +=1
            else:
                break

        if total >= 4:
            return True
        else:
            return False

# g[l][c]
# g[2][0]

affiche(g)
horiz(g, 1, 5, 1)


def match_nul(g):
    max=0
    for e in range(7):
        if g[0][e] == 1 or 2:
            total +=1

    if total == 7:
        return True
    else:
        return False
    
    
        
    
    










        
    
    
            
                


    