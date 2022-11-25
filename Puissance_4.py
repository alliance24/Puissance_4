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
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1],
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


def horiz(g, j, l, c):
    if g[l][c] ==j:
        
        total = 1 # nb de valeurs egales a (j)
        
        # l index du tableau et c index de la case

        for i in range(c+1, len(g[l])):
            if g[l][i] == j:
                total+=1
            else:
                break
                
        if total >=4:
            return True
        else:
            for i in range(c-1, -1, -1):
                if g[l][i] == j:
                    total+=1
                else:
                    break
            
            if total >=4:
                return True
            else:
                return False
    else:
        return False              


def vert(g, j, l, c):
    if g[l][c] ==j:
        
        total = 1 # nb de valeurs egales a (j)
        
        # l index du tableau et c index de la case

        for i in range(l+1, len(g[l])):
            if g[i][c] == j:
                total+=1
            else:
                break
                
        if total >=4:
            return True
        else:
            for i in range(l-1, -1, -1):
                if g[i][c] == j:
                    total+=1
                else:
                    break
            
            if total >=4:
                return True
            else:
                return False
    else:
        return False


def diag(g,j,l,c):
    if g[l][c] ==j:
        
        # on utilise des variables secondaires car on veut conserver les valeurs d'entrée
        l_prime = l
        c_prime = c
        total = 1
        
        for i in range(3):
            
            l_prime-=1
            c_prime+=1
            
            if l_prime >5 or c_prime >6 or l_prime < 0 or c_prime <0:
                break
            else:
                if g[l_prime][c_prime] == j:
                    total+=1
                else:
                    break
                
        if total >=4:
            return True

            
        l_prime = l
        c_prime = c
        
        for i in range(3):
            if total >=4:
                break # On casse la boucle de 3 si total est supérieur à 4
                        # On évite les potentielles erreurs en sortant de la liste
            
            l_prime+=1
            c_prime-=1
            
            if l_prime >5 or c_prime >6 or l_prime < 0 or c_prime <0:
                break
            else:
                if g[l_prime][c_prime] == j:
                    total+=1
                else:
                    break
            
            if total >=4:
                return True
        
        total = 1

        for i in range(3):
            if total >=4:
                break

            l_prime-=1
            c_prime-=1

            if l_prime >5 or c_prime >6 or l_prime < 0 or c_prime <0:
                break
            else:
                if g[l_prime][c_prime] == j:
                    total+=1
                else:
                    break
            
            if total >=4:
                return True

        for i in range(3):
            if total >=4:
                break # On casse la boucle de 3 si total est supérieur à 4
                        # On évite les potentielles erreurs en sortant de la liste
            
            l_prime+=1
            c_prime+=1
            
            if l_prime >5 or c_prime >6 or l_prime < 0 or c_prime <0:
                break
            else:
                if g[l_prime][c_prime] == j:
                    total+=1
                else:
                    break
            
        if total >=4:
            return True
        else:
            return False




    else:
        return False
    
# en bas à gauche - en haut à droite
# g[5][0]
# g[4][1]
# g[3][2]
# g[2][3]
# g[1][4]
# g[0][5]

# en bas à droite - en haut à gauche
# g[5][6]
# g[4][5]
# g[3][4]
# g[2][3]
# g[1][2]
# g[0][1]

affiche(g)
print(diag(g, 1, 5,6))

# def victoire(g,j):  
    

def match_nul(g):
    total=0
    for e in range(7):
        if g[0][e] == 1 or 2:
            total+=1

    if total == 7:
        return True
    else:
        return False
    
    
    
    
        
    
    










        
    
    
            
                


    