
niveau1 = b"\x74\x6f\x6d\x61\x74\x65"
dictionnaire = ["cerise", "poire", "tomate", "ecureuil", "minecraft", "vroomvroom", "supermotdepasse", "impossibletutrouve"]

niveau2 = b"\x31\x31\x33"
chiffres = ["1", "2", "3"]

niveau3 = b"\x79\x6f\x75\x70\x69"
alphabet = ["p", "y", "u", "i", "o"]

def bruteforce1(dictionnaire, motDePasse):
    # boucler sur le dictionnaire et tester toutes les possibilitées
    return

def bruteforce2(chiffres, motDePasse):
    # comment faire pour afficher toutes les possibilitées avec 1, 2 et 3 ?
    # (peut être utiliser plusieurs boucles) 
    return
                

def bruteforce3(debut, alphabet, longueur, motDePasse):
    # généraliser le raisonnement (plus difficile)
    return

def testerMotdePasse(essai, motDePasse):
    if (essai == motDePasse.decode()):
        print("mot de passe trouvé : " + essai)
    return


bruteforce1(dictionnaire, niveau1)
bruteforce2(chiffres, niveau2)
bruteforce3("", alphabet, 5, niveau3)
