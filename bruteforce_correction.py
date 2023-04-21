
niveau1 = b"\x74\x6f\x6d\x61\x74\x65"
dictionnaire = ["cerise", "poire", "tomate", "ecureuil", "minecraft", "vroomvroom", "supermotdepasse", "impossibletutrouve"]

niveau2 = b"\x31\x31\x33"
chiffres = ["1", "2", "3"]

niveau3 = b"\x79\x6f\x75\x70\x69"
alphabet = ["p", "y", "u", "i", "o"]

def bruteforce1(dictionnaire, motDePasse):
    for el in dictionnaire:
        testerMotdePasse(el, motDePasse)

def bruteforce2(chiffres, motDePasse):
    for el1 in chiffres:
        testerMotdePasse(el1, motDePasse)
        for el2 in chiffres:
            testerMotdePasse(el1 + el2, motDePasse)
            for el3 in chiffres:
                testerMotdePasse(el1 + el2 + el3, motDePasse)
                

def bruteforce3(debut, alphabet, longueur, motDePasse):    
    if len(debut) == longueur:
        return
    for el in alphabet:
        essai = debut + el
        testerMotdePasse(essai, motDePasse)
        bruteforce3(essai, alphabet, longueur, motDePasse)

def testerMotdePasse(essai, motDePasse):
    if (essai == motDePasse.decode()):
        print("mot de passe trouvé : " + essai)
    return


bruteforce1(dictionnaire, niveau1)
bruteforce2(chiffres, niveau2)
bruteforce3("", alphabet, 5, niveau3)
