'''
 Duo: Nathan, Julien
 Quatuor: Nathan, Julien, Reian, Chayan
 Certaines parties possèdent des bouts de codes qui sont utilitaires 
 (meilleure visualisation graphique) ou nécessaires pour faire les tests
 
 Note que chacun se donne:
 - Julien (5/5)
 - Nathan (3/5)
 - Reian (4/5)
 - Chayan (3/5)
 
'''

from random import randint


# grille temporaire pour faire les tests
# g = [
#      [1, 2, 1, 2, 2, 1, 1],
#      [0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 1],
#      ]

# l --> ligne (valeur entre 0 et 5)
# c --> colonne (valeur entre 0 et 6)
# j --> joueur (valeur entre 1 ou 2)
# 0 --> case vide | 1 ou 2 --> joueur correspondant

# 1 --> X
# 2 --> O

# Créer la grille vide
def grille_vide():
    return [[0 for c in range(7)] for l in range(6)]

# Nathan
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

# Reian
def coup_possible(g, c): # c doit etre l'index
    if g[0][c] == 0:
        return True
    else:
        return False

# Chayan
def jouer(g, j, c): # c doit etre l'index
    max = 0
    for l in range(len(g)):
        if g[l][c] == 0:
            max = l
    g[max][c] = j

# Julien
def horiz(g, j, l, c):
    if g[l][c] ==j:
        
        total = 1 # nb de valeurs egales a (j)
        
        # l index du tableau et c index de la case

        for i in range(c+1, len(g[l])):
            if i>6 or i<0:
                break
            else:
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

# Julien
def vert(g, j, l, c):
    if g[l][c] ==j:
        
        total = 1 # nb de valeurs egales a (j)
        
        # l index du tableau et c index de la case

        for i in range(l+1, len(g[l])):
            if i>5 or i<0:
                break
            else:
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

# Julien
def diag(g, j, l, c):
    if g[l][c] ==j:
        
        
        #   | ---------------------------------------------------- |
        #   | Partie diagonale --> bas à gauche - en haut à droite |
        #   | ---------------------------------------------------- |
        
        # on utilise des variables secondaires car on veut conserver les valeurs d'entrée
        l_prime = l
        c_prime = c
        total = 1
        
        for i in range(3):
            
            l_prime-=1
            c_prime+=1
            
            if l_prime >5 or c_prime >6 or l_prime <0 or c_prime <0:
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
            
            l_prime+=1
            c_prime-=1
            
            if l_prime >5 or c_prime >6 or l_prime <0 or c_prime <0:
                break
            else:
                if g[l_prime][c_prime] == j:
                    total+=1
                else:
                    break
            
        if total >=4:
                return True

            
        #   | ---------------------------------------------------- |
        #   | Partie diagonale --> bas à droite - en haut à gauche |
        #   | ---------------------------------------------------- |
        
        total = 1
        l_prime = l
        c_prime = c

        for i in range(3):

            l_prime-=1
            c_prime-=1

            if l_prime >5 or c_prime >6 or l_prime <0 or c_prime <0:
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
            
            l_prime+=1
            c_prime+=1
            
            if l_prime >5 or c_prime >6 or l_prime <0 or c_prime <0:
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


#Reian 
def victoire(g, j): 
    for l in range(len(g)):
        for c in range(len(g[l])):
            if vert(g, j, l, c) or horiz(g, j, l, c) or diag(g, j, l, c) == True:
                return True
    return False
    
# Chayan
def match_nul(g):
    total=0
    for c in range(7):
        if g[0][c] == 1 or 2:
            total+=1

    if total == 7:
        return True
    else:
        return False

# Chayan
def coup_aleatoire(g, j):
    while True:
        c = randint(0, 6)
        if coup_possible(g, c):
            jouer(g, j, c)
            return 



#   | ------------------------ |
#   | Joueur contre ordinateur |
#   | ------------------------ |

# Le programme empêche les erreurs lorsque l'on entre des colonnes inexistantes

# Nathan et Julien
def main():
    g = grille_vide()
    player = 1
    bot = 2
    colonne = 10 
    
    affiche(g)
    
    print("Vous allez jouer au puissance 4 contre l'ordinateur")
    print("Souhaitez-vous commencer ? Si oui, tapez 1, si non, tapez 2...")
    print("Vous pouvez aussi laisser le hasard choisir en tapant 3...\n")
    
    result = int(input())
    turn = 2 # On déclare la variable avec une valeur qui ne gênera pas 
    if result == 3:
        turn = randint(0, 1) # 0 est le joueur et 1 est le bot
    
    if turn == 1 or result == 2:
        coup_aleatoire(g, bot)
        affiche(g)
        win = bot
        victoire(g, win)
        match_nul(g)
        
        # On fait jouer une première fois le joueur ici pour éviter des coups d'affilés plus tard
        colonne = int(input("Dans quel colonne souhaitez-vous jouer ? "))
        while colonne >7 and coup_possible(g, colonne-1):
            print("Il semblerait que vous essayez de jouer dans une colonne inexistante...")
            colonne = int(input("Dans quel colonne souhaitez-vous jouer ? "))
            
        colonne-=1 # car les fonctions prennent en paramètre l'index
        jouer(g, player, colonne)
        affiche(g)
        win = player
        victoire(g, win)
        match_nul(g) 
    else:
        affiche(g)
        colonne = int(input("Dans quel colonne souhaitez-vous jouer ? "))
        while colonne >7 and coup_possible(g, colonne-1):
            print("Il semblerait que vous essayez de jouer dans une colonne inexistante...")
            colonne = int(input("Dans quel colonne souhaitez-vous jouer ? "))
            
        colonne-=1 # car les fonctions prennent en paramètre l'index
        jouer(g, player, colonne)
        affiche(g)
        win = player
        victoire(g, win)
        match_nul(g) 
    
    while match_nul(g) != True or victoire(g, win) != True:

        coup_aleatoire(g, bot)
        affiche(g)
        win = bot
        victoire(g, win)
        match_nul(g) 
        colonne = 10
        colonne = int(input("Dans quel colonne souhaitez-vous jouer ? "))
        while colonne >7 and coup_possible(g, colonne-1):
            print("Il semblerait que vous essayez de jouer dans une colonne inexistante...")
            colonne = int(input("Dans quel colonne souhaitez-vous jouer ? "))
            
        colonne-=1 # car les fonctions prennent en paramètre l'index
        jouer(g, player, colonne)
        affiche(g)
        win = player
        victoire(g, win)
        match_nul(g)      
    
    if win == player:
        print("Bravo !!! Vous avez gagné !")    
    elif win == bot:
        print("Quel dommage, vous avez perdu... Vous ferez mieux la prochaine fois")  
    else:
        print("Vous avez fait égalité...")
        


# Reian
def main_2():
    g = grille_vide()
    joueur_1 = 1
    joueur_2 = 2
    
    affiche(g)
    win = joueur_1 # On déclare la variable (joueur_1 par défaut, ne change pas grand chose au programme)
    
    while match_nul(g) != True or victoire(g, win) != True:

        coup_aleatoire(g, joueur_1)
        affiche(g)
        win = joueur_1
        victoire(g, win)
        match_nul(g) 
        
        coup_aleatoire(g, joueur_2)
        affiche(g)
        win = joueur_2
        victoire(g, win)
        match_nul(g)      
    
    print(f"Le joueur {win} a gagné ! ")  



main()
# main_2() 
        
    
    
    
    
    
        
    
    










        
    
    
            
                


    