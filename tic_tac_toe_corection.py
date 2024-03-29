#Le but du programme est d'effectué un programme pour jouer tic-tac-toe entre deux joueurs.
#le joueur pourra choisir une ligne et une colonne pour affecter le caractère "x" ou "o"
#la plupart des fonctionnalités sont codées, vous avez à compléter le code, ou utiliser les fonctions déjà faites.
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


def choisirCase(tableau, joueur , character):
	#Demandez à l'utilisateur de choisir une line et une colonne.
	ligne=int(input("Entrez le numero de la ligne : "))
	colonne=int(input("Entrez le numero de la colone : "))
	#verifiez que le la ligne et la colonne est bien un chiffre entre 1 et 3.
	if ligne not in [1,2,3]:
		print("impossible de choisir cette ligne ... :(")
		choisirCase(tableau , joueur, character)
	elif colonne not in [1,2,3]:
		print("impossible de choisir cette colonne ... :(")
	#Verifiez que la case n'est pas remplie. pour accéder à une case d'un tableau 
	#vous utiliserz la syntaxe suivante :  variable = tableau[ligne-1][colonne-1]  
	elif tableau[ligne-1][colonne-1] != '.':
		print("impossible de choisir cette case ... :(")
		choisirCase(tableau , joueur, character)
	else :
		tableau[ligne-1][colonne-1] = character


def jouer(tableau):
	joueur = random.randint(1,2)
	character = random.choice(["x" , "o"])
	while True :
		#Affichez le joueur en utilisant un print.
		print("c'est le tours du joueur" , joueur)
		print()
		#Appelez la fonction pour afficher le tableau.
		afficherTableau(tableau)
		choisirCase(tableau , joueur , character)
		gagnant = verifierLignes(tableau)

		if gagnant :
			print("joueur " , joueur , "à gagné, Bravo !")
			afficherTableau(tableau)
			return
		if verifierEgalite(tableau) :
			print("Egalité :\\")
			afficherTableau(tableau)
			return

		#Changez le tours du joueur
		if joueur ==1:
			joueur =2
		else :
			joueur =1

		#Changez caractère
		if character == "x":
			character = "o"
		else :
			character = "x"

jouer(tableau)
