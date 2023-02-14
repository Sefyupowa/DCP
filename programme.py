'''
Le but est d'effectuer un programme pour jouer tic-tac-toe entre deux joueurs.

    [ 1 | 2 | 3 ]

[1] [ . | . | . ]

[2] [ . | . | . ]

[3] [ . | . | . ]

Le joueur pourra choisir une ligne et une colonne pour affecter le caractère "x" ou "o"
Par exemple, si un joueur choisi la ligne 3 colonne 2 l'affichage sera comme suit : 
    [ 1 | 2 | 3 ]

[1] [ . | . | . ]

[2] [ . | . | . ]

[3] [ . | x | . ]



La plupart des fonctionnalités sont codées, vous avez à compléter le code, ou utiliser les fonctions déjà faites.
Vous allez coder la fonction choisirCase qui prend en paramètre un tableau, un joueur qui sera sous forme d'un nombre 0 ou 1 et caractère 'x' ou 'o'
Vous allez aussi appeler les fonctions pour compléter le jeu.
Vous allez remarquer que le programme affiche seulement le tableau vide, à vous de jouer ;)
Bon courage 
'''
import random

tableau = [['.', '.','.'],
		   ['.', '.','.'],
		   ['.', '.','.']]


def afficherTableau(tableau):
	print("    [ 1 | 2 | 3 ]")
	print()
	for i,case in enumerate(tableau):
		print("[" +str(i+1) +"]", "[" , end = " ")
		for j , element in enumerate(case) :
				print(element, end="")
				if j != len(tableau)-1:
					print(" |", end=" ")
		print(" ]")
		print()


def verifierEgalite(tableau):
	for i in range(len(tableau)):
		for j in range(len(tableau)):
			if tableau[i][j]=='.':
				return False
	return True


def verifierLignes(tableau):
	#verifier colonnes
	for i in range(0, len(tableau)):
		gagnant=True
		for j in range(0 , len(tableau)):
			if j==2 :
				continue
			if tableau[i][j] == '.' :
				gagnant = False
				break
			if tableau[i][j] != tableau[i][j+1]:
				gagnant = False
		if gagnant ==True:
			return gagnant
	#verifier lignes
	for i in range(0, len(tableau)):
		gagnant=True
		for j in range(0 , len(tableau)):
			if j==2 :
				continue
			if tableau[j][i] == '.' :
				gagnant = False
				break
			if tableau[j][i] != tableau[j+1][i]:
				gagnant = False
		if gagnant ==True:
			return gagnant

	#verifier la diagonale 
	gagnant=True
	for i in range(0, len(tableau)):
		if i==2 :
			continue
		if tableau[i][i] == '.' :
			gagnant = False
			break
		if tableau[i][i] != tableau[i+1][i+1]:
			gagnant = False
	if gagnant ==True:
		return gagnant

	tab = [tableau[2][0] , tableau[1][1] , tableau[0][2]]
	gagnant=True

	for i in range (0 , len(tab)) :
		if i ==2 :
			continue
		if tab[i] == ".":
			return False 

		if tab[i]!=tab[i+1]:
			return False 
	return gagnant


def choisirCase(tableau, joueur , caractere):
    input()
	#Demandez à l'utilisateur de choisir une ligne et une colonne.
#==>
	#Verifiez que  la ligne et la colonne est bien un chiffre entre 1 et 3.
#==>	
	#Verifiez que la case n'est pas remplie. pour accéder à une case d'un tableau vous utiliserez la syntaxe suivante :  variable = tableau[ligne-1][colonne-1]  
#==>
    #Affecter le caractère passé en paramètre au tableau[ligne-1][colonne-1]  
#==>
    pass 
	


def jouer(tableau):
	 #le joueur et le caractère sont choisis aléatoirement sous forme d'un entier (1 ou 2) et un char ('x' ou 'o')
	joueur = random.randint(1,2)
	caractere = random.choice(["x" , "o"])
	while True :
		#Affichez le joueur en utilisant un print.
    #==>

		print()
		afficherTableau(tableau)

        
		choisirCase(tableau , joueur , caractere)

        
		gagnant = verifierLignes(tableau)

		if gagnant :
			print("joueur " , joueur , "à gagné, Bravo !")
			afficherTableau(tableau)
			return
		if verifierEgalite(tableau) :
			print("Egalité :\\")
			afficherTableau(tableau)
			return

		#Changez le tours des joueurs
	#==>

		#Changez caractère
		
    #==>


#Appel à la fonction principale
jouer(tableau)